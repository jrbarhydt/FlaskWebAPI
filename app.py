# flask packages
from flask import Flask, app
from flask_restful import Api
from flask_mongoengine import MongoEngine
from flask_jwt_extended import JWTManager

# local packages
from api.routes import create_routes

# external packages
import os

# default mongodb configuration
default_config = {'MONGODB_SETTINGS': {
                    'db': 'test_db',
                    'host': 'localhost',
                    'port': 27017,
                    'username': 'admin',
                    'password': 'password',
                    'authentication_source': 'admin'},
                  'JWT_SECRET_KEY': 'changeThisKeyFirst'}


def get_flask_app(config: dict = None) -> app.Flask:
    """
    Initializes Flask app with given configuration.
    Main entry point for wsgi (gunicorn) server.
    :param config: Configuration dictionary
    :return: app
    """
    # init flask
    flask_app = Flask(__name__)

    # configure app
    config = default_config if config is None else config
    flask_app.config.update(config)
    if 'MONGODB_URI' in os.environ:
        flask_app.config['MONGODB_SETTINGS'] = {'host': 'mongodb://admin:admin123@ds145128.mlab.com:45128/heroku_0ggqk6b1',
                                                'retryWrites': False}

    # init api and routes
    api = Api(app=flask_app)
    create_routes(api=api)

    # init mongoengine
    db = MongoEngine(app=flask_app)

    # init jwt manager
    jwt = JWTManager(app=flask_app)

    return flask_app


if __name__ == '__main__':
    # Main entry point when run in stand-alone mode.
    app = get_flask_app()
    app.run(debug=True)
