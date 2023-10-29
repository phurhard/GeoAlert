#!/usr/bin/python3
"""Index"""
from models.user import User
from models.todo import Todo
from models.location import Location
from models.locationreminder import LocationReminder
from models import storage
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/', strict_slashes=False)
def status():
    """Returns the status of the flask app"""
    return jsonify({"status": "GeoAlert is running OK"})

@app_views.route('/stats', strict_slashes=False)
def stats():
    """Retrieve the no of each objects in storage"""
    classes = [User, Todo, Location, LocationReminder]
    names = ["users", "todos", "locations", "locationReminders"]

    objs = {names[i]: storage.count(classes[i]) for i in range(len(classes))}
    return jsonify(objs)
