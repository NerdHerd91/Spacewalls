from flask import Flask
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/next_image')
def get_next_image():
	return "next image"


if __name__ == '__main__':
    app.run()