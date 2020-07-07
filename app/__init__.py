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

     # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting config
    from .requests import configure_request
    configure_request(app)

    return app

from app import views
from app import error