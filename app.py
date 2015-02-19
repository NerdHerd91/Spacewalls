from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from flast.ext.heroku import Heroku

app = Flask(__name__)
heroku = Heroku(app)
db = SQLAlchemy(app)

# database model
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

# routes
@app.route('/')
def hello():
    return "Hello World!"

@app.route('/next_image')
def get_next_image():
	return "next image"


if __name__ == '__main__':
	app.debug = True
	app.run()