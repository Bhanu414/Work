WTF_CSRF_ENABLE = True
SECRET_KEY = 'haha-bobby'

OPENID_PROVIDERS = [

	{'name':'Google','url':'http://www.google.com/accounts/o8/id'},
	{'name':'Yahoo','url':'http://me.yahoo.com'},
	{'name':'AOL','url':'http://openid.aol.com/<username>'},
	{'name':'Flickr','url':'http://www.flickr.com/<username>'},
	{'name':'MyOpenID','url':'http://www.myopenid.com'}]