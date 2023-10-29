#!/usr/bin/python3
""" Flask Application for GeoAlert"""
from BE.models import storage
from os import environ
from flask import make_response, jsonify
from BE import app
from BE.api.v1.views.index import *
from BE.api.v1.views.GeoAlert import *
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


app.register_blueprint(app_views)


@app.teardown_appcontext
def close_db(error):
    """Closes and exits the storage"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Callback for 404errors"""
    return make_response(jsonify({'error': "Not Found"}), 404)


@app.errorhandler(500)
def server_error(error):
    """Callback for 500 errors"""
    return make_response(jsonify({
        'error': "Sorry there is a server error"
        }), 500)


if __name__ == "__main__":
    '''Runs the flask app'''
    host = environ.get('HOST')
    port = environ.get('PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True, debug=1)
