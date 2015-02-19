from app import db

class Wallpapers(db.Model):
	__tablename__ = 'wallpapers'

	id = db.Column(db.Integer, primary_key=True)
	path = db.Column(db.String())
	url = db.Column(db.String())
	last_used = db.Column(db.Integer())

	def __init__(self, path, url, last_used):
		self.path = path
		self.url = url
		self.last_used = last_used

	def __repr__(self):
		return '<id {}>'.format(self.id)
