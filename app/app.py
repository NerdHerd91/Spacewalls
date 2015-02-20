from flask import Flask, json, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Sequence, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from flask.ext.heroku import Heroku

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/spacewalls'
heroku = Heroku(app)
db = SQLAlchemy(app)

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
	# TODO add boolean flags for approved/disapproved

	def __init__(self, path, url, last_modified):
		self.path = path
		self.url = url
		self.last_modified = last_modified

	def __repr__(self):
		return '<id {}>'.format(self.id)

# routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/images')
def get_images():
	images = {}
	for row in session.query(Wallpapers).all():
		images[row.id] = row.url
	return json.dumps(images)

# @app.route('/api/images/approve/<path:id>', methods = ['POST'])
# def approve_image(id):
# # set flag for image as approved
# 	query = session.query(Wallpapers).filter_by(id=id)


# @app.route('/api/images/decline/<id>', methods = ['POST'])
# def decline_image(id):
# 	query = session.query(Wallpapers).filter_by(id=id)

	
if __name__ == '__main__':
	app.debug = True
	app.run()
