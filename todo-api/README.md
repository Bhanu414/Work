# This is a practice api.

To run this application we have to execute app.py

$ flask/bin/pip install flask
$ chmod a+x app.py
$ ./app.py

now you can launch your web browser and type http://localhost:5000 to see this tiny application in action.

Total data: curl -i http://localhost:5000/todo/api/tasks

POST data: curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Read a book"}' http://localhost:5000/todo/api/tasks

If you are on Windows and use the Cygwin version of curl from bash then the above command will work just fine.However, if you are using the native version of curl from the regular command prompt there is a little dance that needs to be done to send double quotes inside the body of a request:

curl -i -H "Content-Type: application/json" -X POST -d "{"""title""":"""Read a book"""}" http://localhost:5000/todo/api/tasks

TO update : curl -i -H "Content-Type: application/json" -X PUT -d '{"done":true}' http://localhost:5000/todo/api/tasks/<int:task_id>