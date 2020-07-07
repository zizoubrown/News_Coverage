from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap
from config import config_options

#initializing application
app =Flask(__name__,instance_relative_config=True)

# Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

#initializing Flask Extensions
bootstrap = Bootstrap()

def create_app(config_name):

    app Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    #initializing flask extensionss
    bootstrap.init_app(app)

    retun app

from app import views
from app import error