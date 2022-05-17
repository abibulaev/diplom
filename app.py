from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os


app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)




login_manager=LoginManager(app)

ALLOWED_EXTENSIONS = {'png'}


def create_project(name):
	os.makedirs('static/'+'project/'+name)

def create_avatars(name):
	os.makedirs('static/'+'img/'+name)

def allowed_file(filename, ALLOWED_EXTENSIONS):
	return '.' in filename and \
	filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS