from google.appengine.ext import db

class User(db.Model):
	email = db.EmailProperty()
	password = db.StringProperty()
	user_activated = db.BooleanProperty(default=False)
	approved = db.BooleanProperty(default=False)
	creation_datetime = db.DateTimeProperty(auto_now_add=True)
	last_updatetime = db.DateTimeProperty(auto_now=True)
	
class User_Detail(db.Model):
	user_ref = db.ReferenceProperty(User)
	name = db.StringProperty()
	city = db.StringProperty()
	state = db.StringProperty()
	last_updatetime = db.DateTimeProperty(auto_now=True)
