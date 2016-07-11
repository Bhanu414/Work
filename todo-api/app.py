#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request, url_for
# from flask_httpauth import HTTPBasicAuth
from flask_httpauth import HTTPDigestAuth
# from functool import warps

app = Flask(__name__)
# auth = HTTPBasicAuth()
app.config['SECRET_KEY'] = 'secret key here'
auth = HTTPDigestAuth()

tasks = [

    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    },
    {
        'id': 3,
        'title': u'checking',
        'description': u'checking new data', 
        'done': True
    }
]

users= {
	"bhanu" : "bhanu",
	"kumar" : "python"
}

@auth.get_password
def get_password(username):
	if username in users:
		return users.get(username)
	return None

@auth.error_handler
def unauthorised():
	return make_response(jsonify({'error':'you are Unauthorised'}),401)

@app.route('/')
@auth.login_required
def index():
    return "hello, %s follow <br> /todo/api/tasks <br> /todo/api/tasks/int:task_id" %auth.username()

@app.route('/todo/api/tasks',methods=['GET'])
@auth.login_required
def get_tasks():
    return jsonify({'tasks':[make_public_task(task) for task in tasks]})

@app.route('/todo/api/tasks/<int:task_id>')
@auth.login_required
def get_task(task_id):
    task= [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
            abort(404)
    return jsonify({'task':task[0]})

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'no url'}),404)

@app.route('/todo/api/tasks',methods=['POST'])
@auth.login_required
def create_task():
	if not request.json or not 'title' in request.json:
		abort(400)
	task = {
		'id' : tasks[-1]['id'] + 1,
		'description' : request.json.get('description', ""),
		'title' : request.json['title'],
		'done' : False
	}
	tasks.append(task)
	return jsonify({'task': task}), 201

@app.route('/todo/api/tasks/<int:task_id>', methods =['PUT'])
@auth.login_required
def update_task(task_id):
	task = [task for task in tasks if task['id'] == task_id]
	if len(task) == 0:
		abort(400)
	if not request.json:
		abort(400)
	if 'description' in request.json and type(request.json['description']) is not unicode:
		abort(400)
	if 'title' in request.json and type(request.json['title']) != unicode:
		abort(400)
	if 'done' in request.json and type(request.json['done']) is not bool:
		abort(400)
	task[0]['description'] = request.json.get('description',task[0]['description'])
	task[0]['title'] = request.json.get('title',task[0]['title'])
	task[0]['done'] = request.json.get('done',task[0]['done'])
	return jsonify({'task':task[0]})

@app.route('/todo/api/tasks/<int:task_id>',methods=['DELETE'])
@auth.login_required
def remove_task(task_id):
	task = [task for task in tasks if task['id'] == task_id]
	if len(task) == 0:
		abort(404)
	task.remove(task[0])
	return jsonify({'result':True})

def make_public_task(task):
	new_task = {}
	for filed in task:
		if filed =='id':
			new_task['uri'] = url_for('get_task',task_id=task['id'],_external=True)
		else:
			new_task[filed] = task[filed]
	return new_task


if __name__ == '__main__':
	app.run(debug=True)
