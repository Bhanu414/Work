#!flask/bin/python
import os
import unittest

from config import basedir
from app import app, db
from app.models import User


class TestCase(unittest.TestCase):
	def setUp(self):
		app.config['TESTING'] = True
		app.config['WTF_CSRF_ENABLE'] = False
		app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'test.db')
		self.app = app.test_client()
		db.create_all()

	def tearDown(self):
		db.session.remove()
		db.drop_all()

	def test_avatar(self):
		u = User(nickname = 'bhanu',email='bhanupython@gmail.com')
		avatar = u.avatar(128)
		expected = 'https://s.gravatar.com/avatar/36811e9f80f570e2f9c5778dffb5438c?s=80'
		assert avatar[0:len(expected)] == expected

	def test_make_unique_nickname(self):
		u = User(nickname='bhanu', email='bhanupython@gmail.com')
		db.session.add(u)
		db.session.commit()
		nickname = User.make_unique_nickname('bhanu')
		assert nickname != 'bhanu'
		u = User(nickname=nickname, email='bhanu@gmail.com')
		db.session.add(u)
		db.session.commit()
		nickname2 = User.make_unique_nickname('bhanu')
		assert nickname2 != 'bhanu'
		assert nickname2 != nickname

if __name__ == '__main__':
    unittest.main()
