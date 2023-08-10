#!/usr/bin/python3
""" Objects that will handle all default RESTful API for GeoAlert"""
from models.user import User
from models.todo import Todo
from models.location import Location
from models import storage
from models.locationreminder import LocationReminder
from api.v1.views import app_views
from datetime import datetime
from hashlib import md5
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)

@app_views.route('/login', methods=['POST'], strict_slashes=False)
def login():
    """User login"""
    data = request.get_json()
    if not data:
        print('Data is not JSON')
    username = data.get('username')
    password = data.get('password')
    user = storage.get(User, username)
    encrpyt_password =  md5(password.encode()).hexdigest()  
    if not user or (user.password != encrpyt_password and user.password != password):
        
        return jsonify({'error': 'Invalid username or password.'}), 401

    access_token = create_access_token(identity=user.username)
    return jsonify(access_token=access_token)


@app_views.route('/profile', methods=['GET'], strict_slashes=False)
@jwt_required()
def profile():
    '''users profile'''
    username = get_jwt_identity()
    user = storage.get(User, username)
    return jsonify(user.to_dict())
    
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

# should be used for signup
@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
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
    return jsonify({'message': 'User registered successfully.'}), 201

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
    k = 1
    Todo = {}
    if not user:
        abort(404)
    for todo in user.todos:
        Todo[k] = todo.to_dict()
        
        k += 1
    return jsonify(Todo)

''' To get the todos with a specific boolean, edit it with frontend'''

@app_views.route('/<username>/todo', methods=["POST"], strict_slashes=False)
def create_todo(username):
    """Creates a new todo for a user"""
    data = request.get_json()
    if not data:
        print('Not a valid JSON')
    data['user_name'] = username
    if "completed" in data:
        value = data['completed']
        if value == "False":
            data['completed'] = bool("False")
        else:
            data['completed'] = bool("True")
    todo = Todo(**data)
    todo.save()
    return jsonify(todo.to_dict())

@app_views.route('/<username>/<todoId>', methods=['GET'], strict_slashes=False)
def deleteTodo(username, todoId):
    """This method deletes a todo based on it's ID"""
    user = storage.get(User, username)
    todos = user.todos
    for todo in todos:
        
        if todo.to_dict()['id'] == todoId:
            print(todo)
            todo.delete()
    user.save()
    return jsonify({})

@app_views.route('/<username>/todos/<todoId>', methods=['PUT'], strict_slashes=False)
def updateTodo(username,  todoId):
    """Updates the todo with given parameters"""
    user = storage.get(User, username)
    ignore = ['user_name', 'id', '__class__', 'created_at', 'updated_at']
    todos = user.todos
    for todo in todos:
        if todo.to_dict()['id'] == todoId:
            data = request.get_json()
            if not data:
                return jsonify({"Error": "Not a JSON"})
            for k,v in data.items():
                if k not in ignore:
                    setattr(todo, k, v)
            todo.to_dict()['updated_at'] = datetime.now()
    user.save()
    return jsonify(todo.to_dict())

# Location
@app_views.route('/locations', strict_slashes=False)
def get_Locations():
    """Gets all the location data. will edit
    it to get only location based on a user"""
    data = storage.all(Location)
    dictLocation = {}
    for k, v in data.items():
        dictLocation[k] = v.to_dict()
    
    return jsonify({"contentts": dictLocation})
@app_views.route('/<username>/location', methods=['POST'], strict_slashes=False)
def create_L(username):
    """Creates a location class for a user """
    user = storage.get(User, username)
    data = request.get_json()
    data['user_name'] = username
    location = Location(**data)
    location.save()
    return jsonify(location.to_dict())

@app_views.route('/<username>/location/<locationId>', strict_slashes=False)
def get_L(username, locationId):
    """Gets a location based on it id"""
    user = storage.get(User, username)
    
    locations = user.locations
    for location in locations:
        if location.to_dict()['id'] == locationId:
            return jsonify(location.to_dict())
    #return jsonify({"Error": "There is no Location data for this user"})
@app_views.route('/<username>/location/<locationId>', methods=['PUT'], strict_slashes=False)
def update_L(username, locationId):
    """Updates location detail"""
    user = storage.get(User, username)
    locations = user.locations
    for location in locations:
        if location.to_dict()['id'] == locationId:
            #print(location.to_dict())
            data = request.get_json()
            for k, v in data.items():
                setattr(location, k, v)
            location.to_dict()['updated_at'] = datetime.utcnow()
            user.save()
            return jsonify(location.to_dict())

@app_views.route('/<username>/location/<locationId>', methods=['DELETE'], strict_slashes=False)
def delete_L(username, locationId):
    """Deletes a location resource"""
    user = storage.get(User, username)
    locations = user.locations
    for location in locations:
        if location.to_dict()['id'] == locationId:
            location.delete()
    user.save()
    return jsonify({})

# Location Reminder Endpoints
@app_views.route('/<username>/<todoId>/<locationId>/locationReminder', methods=['POST'], strict_slashes=False)
def create_LR(username, locationId, todoId):
    """Creates a location based task reminder """
    
    data = request.get_json()
    if not data:
        return jsonify({"Error": "Not a valid JSON"})
    
    data['user_name'] = username
    data['todo_id'] = todoId
    data['location_id'] = locationId

    locaRemind = LocationReminder(**data)
    locaRemind.save()
    return jsonify(locaRemind.to_dict())

@app_views.route('/<username>/<locationReminderId>', methods=['DELETE'], strict_slashes=False)
def delete_LR(username, locationReminderId):
    """Removes a location reminder from the storage"""
    user = storage.get(User, username)
    locoRemind = user.locationReminder
    for lr in locoRemind:
        if lr.to_dict()['id'] == locationReminderId:
            lr.delete()
            user.save()
            return jsonify({"Success": "Location Reminder deleted"})
    return jsonify({"Error": "Location Reminder could not be found"})
    
@app_views.route('/<username>/<locationReminderId>', methods=["PUT"], strict_slashes=False)
def update_LR(username, locationReminderId):
    """Updates the location reminder"""
    ignore = ['updated_at', 'created_at', 'user_name', 'id']
    user = storage.get(User, username)
    locationReminders = user.loctionReminder
    for locationRemind in locationReminders:
        if locationRemind.to_dict()['id'] == locationReminderId:
            data = request.get_json()
            if 'activated' in data:
                data['activated'] = bool(data['activated'])
            for k, v in data.items():
                if k not in ignore:
                    setattr(locationRemind, k, v)
            locationRemind['updated_at'] = datetime.utcnow()
        return jsonify(locationRemind.to_dict)

@app_views.route('/admin', strict_slashes=False)
def all():
    '''shows all entries in the database'''
    database = storage.all()
    data = {}
    for k, v in database.items():
        data[k] = v.to_dict()
    return jsonify(data)
