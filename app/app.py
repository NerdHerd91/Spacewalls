from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Sequence, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from flask.ext.heroku import Heroku

run = Flask(__name__)
# run.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/spacewalls'
heroku = Heroku(run)
db = SQLAlchemy(run)

engine = create_engine('postgresql://localhost/spacewalls', echo=True)
session = scoped_session(sessionmaker(bind = engine,
                                    autocommit = False,
                                    autoflush = False))
Base = declarative_base()
Base.query = session.query_property()

# database model
class Wallpapers(Base):
	__tablename__ = 'wallpapers'

	id = db.Column(db.Integer, primary_key=True)
	path = db.Column(db.String())
	url = db.Column(db.String())
	last_modified = db.Column(TIMESTAMP)

	def __init__(self, path, url, last_modified):
		self.path = path
		self.url = url
		self.last_modified = last_modified

	def __repr__(self):
		return '<id {}>'.format(self.id)

# routes
@run.route('/')
def index():
    return render_template('index.html')

@run.route('/api/images')
def get_next_image():
	return "next image"

# @run.route('/api/images/approve/<id>')
# def approve_image(id):
# # set flag for image as approved

# @run.route('/api/images/decline/<id>')
# def decline_image(id):
# set flag for image as declined

if __name__ == '__main__':
	run.debug = True
	run.run()
