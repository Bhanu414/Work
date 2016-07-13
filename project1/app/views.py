from flask import render_template
from app import app

@app.route('/')

@app.route('/index')
def index():
	user = {'name' : 'bhanu'}
	teams = [
		{
			'person' : {'name' : 'bhanu'},
			'age' : '20'
		},
		{
			'person' : {'name' : 'prakash'},
			'age' : '23'
		}
	]
	return render_template('index.html',
							title = 'My page',
							user = user,
							teams = teams)
