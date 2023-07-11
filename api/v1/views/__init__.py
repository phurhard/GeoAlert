#!/usr/bin/python3
""" Blueprint"""
from flask import Blueprint
from flask_cors import CORS

app_views = Blueprint('app_views', __name__, url_prefix='/api/')

CORS(app_views)

from api.v1.views.index import *
from api.v1.views.GeoAlert import *
