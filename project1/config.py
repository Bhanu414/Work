import os
basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_ENABLE = True
SECRET_KEY = 'haha-bobby'

OPENID_PROVIDERS = [

	# {'name':'Google','url':'http://www.google.com/accounts/o8/id'},
	{'name':'Yahoo','url':'http://me.yahoo.com'},
	{'name':'AOL','url':'http://openid.aol.com/<username>'},
	# {'name':'Flickr','url':'http://www.flickr.com/<username>'},
	{'name':'MyOpenID','url':'http://www.myopenid.com'}]



SQLALCHEMY_DATABASE_URI = 'sqlite:///'+ os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')


# mail server settings
MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = None
MAIL_PASSWORD = None

# administrator list
ADMINS = ['bhanupython@gmail.com']

