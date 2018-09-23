from flask import Flask,render_template,url_for,json
from flask_bootstrap import Bootstrap
#from config import config


bootstrap = Bootstrap()

from app import api
from app import main

def create_app(config_anme):
    app = Flask(__name__)
    #app.config.from_object(config[config_name])
    #config[config_anme].init_app(app)

    bootstrap.init_app(app)

    app.register_blueprint(main.bp)
    app.register_blueprint(api.bp,url_prefix="/api")


    return app




