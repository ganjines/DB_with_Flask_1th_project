from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Load configuration from .env file
app.config.from_envvar('APP_CONFIG_FILE')

db = SQLAlchemy(app)

from app import routes

