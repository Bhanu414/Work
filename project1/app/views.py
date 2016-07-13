from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')

@app.route('/index')
def index():
	user = {'name' : 'bikki'}
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

@app.route('/login',methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login request for OpenID = "%s", remember_me=%s' %(form.openid.data,str(form.remember_me.data)))
		return redirect('/index')
	return render_template('login.html', 
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])