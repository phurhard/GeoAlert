#!/usr/bin/python3
""" Objects that will handle all default RESTful API for GeoAlert"""
from models.user import User
from models.todo import Todo
from models.location import Location
from models import storage
from models.locationreminder import LocationReminder
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/users', methods=['GET'], strict_slashes=False)
# @swag_from('documentation/user/all_users.yml')
def get_users():
    """Retrieves a list of all users"""
    all_users = storage.all(User).values()
    list_users = []
    for user in all_users:
        list_users.append(user.to_dict())
    
    return jsonify(list_users)

@app_views.route('/users/<username>', methods=['GET'], strict_slashes=False)

def get_user(username):
    """Retrieves a user based on the user name"""
    user = storage.get(User, username)
    if not user:
        abort(404)

    return jsonify(user.to_dict())

@app_views.route('/users/<username>', methods=['DELETE'], strict_slashes=False)

def delete_user(username):
    """Deletes a user"""
    user = storage.get(User, username)

    if not user:
        abort(404)

    storage.delete(user)
    storage.save()

    return make_response(jsonify({}), 200)

@app_views.route('/users', methods=['POST'], strict_slashes=False)
def post_user():
    """Creates a new user"""
    if not request.get_json():
        abort(400, description="Error, not valid")
    if 'email' not in request.get_json():
        abort(400, description="Email is missing")
    if 'password' not in request.get_json():
        abort(400, description="Missing password")

    data = request.get_json()
    instance = User(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)

@app_views.route('/users/<username>', methods=['PUT'], strict_slashes=False)
def put_user(username):
    """Updates a user"""
    user = storage.get(User, username)
    if not user:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    ignore = ['username', 'created_at', 'updated_at', 'id']
    data = request.get_json()
    for k,v in data.items():
        if k not in ignore:
            setattr(user, k, v)
    storage.save()
    return make_response(jsonify(user.to_dict()), 200)

@app_views.route('/<username>/todos', strict_slashes=False)
def get_Todos(username):
    """Gets all todos relates to a user"""
    user = storage.get(User, username)
    Todo = []
    if not user:
        abort(404)
    for todo in user.todos:
        Todo.append(todo.to_dict())
    return jsonify(Todo)

''' To get the todos with a specific boolean, edit it with frontend'''

@app_views.route('/<username>/todo', strict_slashes=False)
def create_todo(username):
    """Creates a new todo for a user"""
    data = request.get_json()
    if user_name in data:
        data['user_name'] = username
    todo = Todo(**data)
    return jsonify(todo)


@app_views.route('/admin', strict_slashes=False)
def all():
    '''shows all entries in the database'''
    database = storage.all()
    data = {}
    for k, v in database.items():
        data[k] = v.to_dict()
    return jsonify(data)
