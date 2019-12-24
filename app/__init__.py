from flask import Flask
from flask_cors import CORS

from config import Config


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(Config)

# enable CORS
CORS(app)

from app import routes
