from flask import render_template, flash, redirect, sessions,url_for, request, g
from flask_login import login_user,logout_user,current_user,login_required
from app import app,db,lm,oid
from .forms import LoginForm
from .models import User

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

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
@oid.loginhandler
def login():
	if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login request for OpenID = "%s", remember_me=%s' %(form.openid.data,str(form.remember_me.data)))
		return redirect('/index')
	return render_template('login.html', 
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])