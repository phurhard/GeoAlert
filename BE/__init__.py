from werkzeug.middleware.proxy_fix import ProxyFix
from flask import Flask, Blueprint
from flask_jwt_extended import JWTManager
from flask_cors import CORS
# from BE.api.v1.views import app_views
from flask_restx import Api
# from BE.api.v1.views.index import *
# from BE.api.v1.views.GeoAlert import *


app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['JWT_SECRET_KEY'] = 'GeoAlert'  # Replace with your secret key
jwt = JWTManager(app)
app_views = Blueprint('app_views', __name__, url_prefix='/api/')

CORS(app, resources={r"/api/*": {"origins": "*"}})

api_rest = Api(app, version='1.0', title='GeoAlert',
               description='A Location based Todo app')


# CORS(app_views)

# from BE.api.v1.views import (index, GeoAlert)
