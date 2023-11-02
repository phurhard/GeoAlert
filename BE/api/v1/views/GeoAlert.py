#!/usr/bin/python3
''' Objects that will handle all default RESTful API for GeoAlert'''
from BE.models.user import User
from BE.models.todo import Todo
from BE.models.location import Location
from BE.models import storage
from BE.models.locationreminder import LocationReminder
from datetime import datetime
from hashlib import md5
import BE
from BE import api_rest, app_views
from flask_restx import Resource, fields, Namespace, reqparse, inputs
from flask import abort, jsonify, make_response, request
from flask_jwt_extended import (
    create_access_token, jwt_required, get_jwt_identity
)
from sqlalchemy.exc import IntegrityError


# Namespace creation for user, todo, location and locationreminder
user = api_rest.namespace(
    'user',
    description="Users login and authentication for the app",
    validate=True
    )
todo = BE.api_rest.namespace(
    'todo',
    description="Tasks operations"
    )
location = BE.api_rest.namespace(
    'location',
    description="Location based operations"
)
locationReminder = BE.api_rest.namespace(
    'locationReminder',
    description="Associating todos with their respective locations"
)

# Models for serialization
# user_model = user.model(
#     'User',
#     {
#         'username': fields.String(
#             required=True,
#             description='A chosen username to identify the user with'
#             ),
#         'firstname': fields.String(
#             required=True,
#             description='A firstname to identify the user with'
#             ),
#         'lastname': fields.String(
#             required=True,
#             description='Lastname of user'
#             ),
#         'email': fields.String(
#             required=True,
#             description='A genuine email address'
#             ),
#         'password': fields.String(
#             required=True,
#             description='A genuine email address'
#             )
#     }
# )

user_model = user.model(
    'User',
    {
        'username': fields.String(
            # required=True,
            description='A chosen username to identify the user with'
            ),
        'firstname': fields.String(
            # required=True,
            description='A firstname to identify the user with'
            ),
        'lastname': fields.String(
            # required=True,
            description='Lastname of user'
            ),
        'email': fields.String(
            # required=True,
            description='A genuine email address'
            ),
        'password': fields.String(
            # required=True,
            description='A genuine email address'
            )
    }
)

todo_model = BE.api_rest.model(
    'Todo',
    {
        'user_name': fields.String(
            required=True,
            description='A chosen username to identify the user with'
            ),
        'title': fields.String(
            required=True,
            description='A firstname to identify the user with'
            ),
        'description': fields.String(
            required=True,
            description='Lastname of user'
            ),
        'due_date': fields.DateTime(
            required=True,
            description='When the task should be due'
            ),
        'completed': fields.Boolean(
            default=False,
            required=True,
            description='Has the task been done'
            )
    }
)

location_model = BE.api_rest.model(
    'Location',
    {
        'user_name': fields.String(
            required=True,
            description='A chosen username to identify the user with'
            ),
        'name': fields.String(
            required=True,
            description='The name of the location'
            ),
        'address': fields.String(
            required=True,
            description='The location address'
            ),
        'longitude': fields.String(
            required=True,
            description='Longitude value'
            ),
        'latitude': fields.String(
            required=True,
            description='Latitude value'
            )
    }
)

locationReminder_model = BE.api_rest.model(
    'LocationReminder',
    {
        'user_name': fields.String(
            required=True,
            description='The user who has the task'
            ),
        'location_id': fields.String(
            required=True,
            description='The id of the chosen location'
            ),
        'todo_id': fields.String(
            required=True,
            description='the task id'
            ),
        'accuracy': fields.String(
            description='The accuracy of the Reminder'
            ),
        'activated': fields.String(
            description='Has the tasks been done?'
            )
    }
)

# input parser
parser = reqparse.RequestParser()
parser.add_argument('email', type=inputs.email, help='Email address')
parser.add_argument('username', type=str, help='Username')
parser.add_argument('firstname', type=str, help='Firstname')
parser.add_argument('lastname', type=str, help='Lastname')
parser.add_argument('password', type=str, help='Password')

@user.route('/')
class UserView(Resource):
    '''Basic authentication operations necessary for a user'''
    @user.doc('Admin get all users')
    def get(self):
        """Returns all users in the db
        This is just for testing, removed later"""
        all_users = storage.all(User).values()
        list_users = [user.to_dict() for user in all_users]
        
        return {
            'status': 200,
            'success': True,
            'message': 'List of all users',
            'data': list_users
                }

    @user.doc('sign up')
    @user.expect(user_model, validate=True)
    def post(self):
        '''signup: creates a new user'''
        if not request.get_json():
            abort(400, description="Error, not valid")
        if 'email' not in request.get_json():
            abort(400, description="Email is missing")
        if 'password' not in request.get_json():
            abort(400, description="Missing password")

        try:
            data = request.get_json()
            username = data['username']
            user = storage.get(User, username)
            if user:
                return {
                    'status': 400,
                    'success': False,
                    'message': 'This username already exists'
                }, 400
            user = User(**data)
            user = user.to_dict()
            return {
                'status': 200,
                'success': True,
                'message': 'User created',
                'data': user
                }, 200
        except Exception as e:
            print(f'An error was raised {e}')
            return {
                'status': 500,
                'success': False,
                'message': e
            }, 500
        


@user.route('/<string:username>')
@user.param('username', 'Username of the user')
class UserActivity(Resource):
    '''Make use of flask login and flask user'''
    @user.doc('Get user Profile')
    def get(self, username):
        '''Returns the profile details of the user'''
        if user := storage.get(User, username):
            return {
                'status': 200,
                'success': True,
                'message': f'Details of user {username}',
                'data': user.to_dict()
                }, 200
        return {
            'status': 400,
            'success': False,
            'message': 'No user found with that name'
        }, 404
        

    @user.doc('Delete a user account')
    def delete(self, username):
        '''Deletes a user'''
        user = storage.get(User, username)

        if not user:
            return {
            'status': 400,
            'success': False,
            'message': 'No user found with that name'
        }, 404

        storage.delete(user)
        storage.save()

        return make_response(jsonify({}), 200)

    @user.doc('update user credentials')
    @user.expect(user_model, validate=True)
    def put(self, username):
        '''Updates a user'''
        user = storage.get(User, username)
        if not user:
            abort(404)
        if not request.get_json():
            abort(400, description="Not a JSON")
        ignore = ['username', 'created_at', 'updated_at', 'id']
        
        data = request.get_json()
        if username != data['username']:
            return {
                'message': 'invalid request'
            }, 400
        
        for k, v in data.items():
            if k not in ignore:
                setattr(user, k, v)
        storage.save()
        return make_response(jsonify(user.to_dict()), 200)


@todo.route('/')
class TodoView(Resource):
    '''Users tasks activities'''
    @todo.doc('Admin: get all todos')
    # @todo.marshal_with(todo_model, 200)
    def get(self):
        '''Get all todo in the db'''
        all_tasks = storage.all(Todo).values()
        tasks = [task.to_dict() for task in all_tasks]
        return tasks, 200

    @todo.doc('Create a new todo')
    @todo.expect(todo_model, validate=True)
    # @todo.marshal_with(todo_model)
    def post(self):
        '''Creates a new todo for a user
        username will be sent as part of payload'''
        data = request.get_json()
        if not data:
            print('Not a valid JSON')
        username = data['user_name']
        user = storage.get(User, username)
        if not user:
            return {
                'status': 404,
                'success': False,
                'message': 'No user found'
            }, 404
        data['due_date'] = datetime.strptime(data['due_date'], "%Y-%m-%d %H:%M:%S")
        
        todo = Todo(**data)
        return {
            'status': 201,
            'success': True,
            'message': 'A new task has been created',
            'data': todo.to_dict()
        }, 201


@todo.route('/<string:id>')
@todo.param('id', 'task id')
class TodoTasks(Resource):
    '''Tasks'''
    
    @todo.doc('Get a single todo')
    def get(self, id):
        '''Gets a single task'''
        # k = 1
        # Todo = {}
        # if not user:
        #     abort(404)
        # for todo in user.todos:
        #     Todo[k] = todo.to_dict()
        #     k += 1
        # return jsonify(Todo)
        if task := storage.get(Todo, id):
            return {
                'status': 200,
                'success': True,
                'message': 'Requested task found',
                'data': task.to_dict()
            }, 200
        else:
            return {
                'status': 404,
                'success': False,
                'message': 'requested task not found'
            }, 404

    @todo.doc('Delete a todo')
    def delete(self, id):
        '''This method deletes a todo based on it's ID'''
        if task := storage.get(Todo, id):
            storage.delete(task)
            storage.save()
            return {
                'status': 204,
                'success': True,
                'message': 'Requested task has been deleted succefully'
            }, 204
        return {
            'status': 404,
            'success': False,
            'message': 'Requested task not found'
        }, 404

    @todo.doc('Update a todo')
    @todo.expect(todo_model, validate=True)
    def put(self, id):
        '''Updates the todo with given parameters'''
        task = storage.get(Todo, id)
        ignore = ['user_name', 'id', '__class__', 'created_at', 'updated_at']
        if not task:
            return {
                'status': 404,
                'success': False,
                'message': 'Requested task not found'
                }, 404
        
        data = request.get_json()
        if not data:
            return {"Error": "Not a JSON"}, 400
        for k, v in data.items():
            if k not in ignore:
                setattr(todo, k, v)
        todo.to_dict()['updated_at'] = datetime.now()
        todo.save()
        return {
            'status': 200,
            'success': True,
            'message': 'Requested task updated successfully',
            'data': todo.to_dict()
            }, 200


@location.route('/location')
class LocationView(Resource):
    '''Location based details
    location details is sent from the client and saved on the db
    to reduce successive calls to the Google API'''
    def get_Locations():
        '''Gets all the location data. will edit
        it to get only location based on a user'''
        data = storage.all(Location)
        dictLocation = {k: v.to_dict() for k, v in data.items()}
        return jsonify({"contents": dictLocation})

    def create_L(self):
        '''Creates a location class for a user '''
        # user = storage.get(User, username)
        data = request.get_json()
        data['user_name'] = self
        location = Location(**data)
        location.save()
        return jsonify(location.to_dict())

    def get_L(self, locationId):
        '''Gets a location based on it id'''
        location = storage.get(Location, locationId)
        return jsonify(location.to_dict())
        # return jsonify({"Error": "There is no Location data for this user"})

    def update_L(self, locationId):
        '''Updates location detail'''
        user = storage.get(User, self)
        location = storage.get(Location, locationId)
        if self == location.user_name:
            data = request.get_json()
            for k, v in data.items():
                setattr(location, k, v)
        location.to_dict()['updated_at'] = datetime.utcnow()
        user.save()
        return jsonify(location.to_dict())

    def delete_L(self, locationId):
        '''Deletes a location resource'''
        user = storage.get(User, self)
        locations = user.locations
        for location in locations:
            if location.to_dict()['id'] == locationId:
                location.delete()
        user.save()
        return jsonify({})


@locationReminder.route('/locationreminder')
class LocationReminderView(Resource):
    '''This class combines tasks with locations'''
    def create_LR():
        '''Creates a location based task reminder '''
        data = request.get_json()
        if not data:
            return jsonify({"Error": "Not a valid JSON"})
        # data['user_name'] = username
        # data['todo_id'] = todoId
        # data['location_id'] = locationId

        locaRemind = LocationReminder(**data)
        locaRemind.save()
        return jsonify(locaRemind.to_dict())

    def delete_LR(self, locationReminderId):
        '''Removes a location reminder from the storage'''
        user = storage.get(User, self)
        locoRemind = user.locationReminder
        for lr in locoRemind:
            if lr.to_dict()['id'] == locationReminderId:
                lr.delete()
                user.save()
                return jsonify({"Success": "Location Reminder deleted"})
        return jsonify({"Error": "Location Reminder could not be found"})

    def update_LR(self, locationReminderId):
        '''Updates the location reminder'''
        ignore = ['updated_at', 'created_at', 'user_name', 'id']
        user = storage.get(User, self)
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


"""


@app_views.route('/login', methods=['POST'], strict_slashes=False)
def login():
    '''User login'''
    data = request.get_json()
    if not data:
        print('Data is not JSON')
    username = data.get('username')
    password = data.get('password')
    user = storage.get(User, username)
    encrpyt_password = md5(password.encode()).hexdigest()
    if not user or (user.password != encrpyt_password
                    and user.password != password):
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
def get_users():
    '''Retrieves a list of all users'''
    all_users = storage.all(User).values()
    list_users = []
    for user in all_users:
        list_users.append(user.to_dict())

    return jsonify(list_users)


@app_views.route('/users/<username>', methods=['GET'], strict_slashes=False)
def get_user(username):
    '''Retrieves a user based on the user name'''
    user = storage.get(User, username)
    if not user:
        abort(404)

    return jsonify(user.to_dict())


@app_views.route('/users/<username>', methods=['DELETE'], strict_slashes=False)
def delete_user(username):
    '''Deletes a user'''
    user = storage.get(User, username)

    if not user:
        abort(404)

    storage.delete(user)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    '''Creates a new user'''
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
    '''Updates a user'''
    user = storage.get(User, username)
    if not user:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    ignore = ['username', 'created_at', 'updated_at', 'id']
    data = request.get_json()
    for k, v in data.items():
        if k not in ignore:
            setattr(user, k, v)
    storage.save()
    return make_response(jsonify(user.to_dict()), 200)

# TODOS


@app_views.route('/<username>/todos', methods=["GET"], strict_slashes=False)
def get_Todos(username):
    '''Gets all todos relates to a user'''
    user = storage.get(User, username)
    k = 1
    Todo = {}
    if not user:
        abort(404)
    for todo in user.todos:
        Todo[k] = todo.to_dict()
        k += 1
    return jsonify(Todo)


@app_views.route('/<username>/todo', methods=["POST"], strict_slashes=False)
def create_todo(username):
    '''Creates a new todo for a user'''
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
    '''This method deletes a todo based on it's ID'''
    user = storage.get(User, username)
    todos = user.todos
    for todo in todos:
        if todo.to_dict()['id'] == todoId:
            print(todo)
            todo.delete()
    user.save()
    return jsonify({})


@app_views.route('/<username>/todos/<todoId>',
                 methods=['PUT'], strict_slashes=False)
def updateTodo(username,  todoId):
    '''Updates the todo with given parameters'''
    user = storage.get(User, username)
    ignore = ['user_name', 'id', '__class__', 'created_at', 'updated_at']
    todos = user.todos
    for todo in todos:
        if todo.to_dict()['id'] == todoId:
            data = request.get_json()
            if not data:
                return jsonify({"Error": "Not a JSON"})
            for k, v in data.items():
                if k not in ignore:
                    setattr(todo, k, v)
            todo.to_dict()['updated_at'] = datetime.now()
    user.save()
    return jsonify(todo.to_dict())

Location


@app_views.route('/locations', strict_slashes=False)
def get_Locations():
    '''Gets all the location data. will edit
    it to get only location based on a user'''
    data = storage.all(Location)
    dictLocation = {}
    for k, v in data.items():
        dictLocation[k] = v.to_dict()
    return jsonify({"contentts": dictLocation})


@app_views.route('/<username>/location',
                 methods=['POST'], strict_slashes=False)
def create_L(username):
    '''Creates a location class for a user '''
    # user = storage.get(User, username)
    data = request.get_json()
    data['user_name'] = username
    location = Location(**data)
    location.save()
    return jsonify(location.to_dict())


@app_views.route('/<username>/location/<locationId>', strict_slashes=False)
def get_L(username, locationId):
    '''Gets a location based on it id'''
    user = storage.get(User, username)
    locations = user.locations
    for location in locations:
        if location.to_dict()['id'] == locationId:
            return jsonify(location.to_dict())
    # return jsonify({"Error": "There is no Location data for this user"})


@app_views.route('/<username>/location/<locationId>',
                 methods=['PUT'], strict_slashes=False)
def update_L(username, locationId):
    '''Updates location detail'''
    user = storage.get(User, username)
    locations = user.locations
    for location in locations:
        if location.to_dict()['id'] == locationId:
            # print(location.to_dict())
            data = request.get_json()
            for k, v in data.items():
                setattr(location, k, v)
            location.to_dict()['updated_at'] = datetime.utcnow()
            user.save()
            return jsonify(location.to_dict())


@app_views.route('/<username>/location/<locationId>',
                 methods=['DELETE'], strict_slashes=False)
def delete_L(username, locationId):
    '''Deletes a location resource'''
    user = storage.get(User, username)
    locations = user.locations
    for location in locations:
        if location.to_dict()['id'] == locationId:
            location.delete()
    user.save()
    return jsonify({})

# Location Reminder Endpoints


@app_views.route('/locationReminder',
                 methods=['POST'], strict_slashes=False)
def create_LR():
    '''Creates a location based task reminder '''
    data = request.get_json()
    if not data:
        return jsonify({"Error": "Not a valid JSON"})
    # data['user_name'] = username
    # data['todo_id'] = todoId
    # data['location_id'] = locationId

    locaRemind = LocationReminder(**data)
    locaRemind.save()
    return jsonify(locaRemind.to_dict())


@app_views.route('/<username>/<locationReminderId>',
                 methods=['DELETE'], strict_slashes=False)
def delete_LR(username, locationReminderId):
    '''Removes a location reminder from the storage'''
    user = storage.get(User, username)
    locoRemind = user.locationReminder
    for lr in locoRemind:
        if lr.to_dict()['id'] == locationReminderId:
            lr.delete()
            user.save()
            return jsonify({"Success": "Location Reminder deleted"})
    return jsonify({"Error": "Location Reminder could not be found"})


@app_views.route('/<username>/<locationReminderId>',
                 methods=["PUT"], strict_slashes=False)
def update_LR(username, locationReminderId):
    '''Updates the location reminder'''
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

"""


@app_views.route('/admin', strict_slashes=False)
def all():
    '''shows all entries in the database'''
    database = storage.all()
    data = {k: v.to_dict() for k, v in database.items()}
    return jsonify(data)
