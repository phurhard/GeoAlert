#!/usr/bin/python3
"""Index"""
from BE.models.user import User
from BE.models.todo import Todo
from BE.models.location import Location
from BE.models.locationreminder import LocationReminder
from BE.models import storage
from BE import app_views
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

    objs = {}
    for i in range(len(classes)):
        objs[names[i]] = storage.count(classes[i])
    return jsonify(objs)
