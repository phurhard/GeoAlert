#!/usr/bin/python3
""" This is a console ionterface for the geoalert app
It's duties is to serve as an admin page and also as a user page
users will bring out all users
user.id will bring out a specific user and so on"""

import cmd
from datetime import datetime
import models
import shlex
from models.user import User
from models.location import Location
from models.todo import Todo
from models.locationreminder import LocationReminder
import shlex


class GeoAlert(cmd.Cmd):
    """ The console for geoalert"""
    prompt = 'GeoAlert >> '

    classes = ['User', 'Location', 'Todo', 'LocationReminder']

    def do_create(self, line):
        """Creates a new instance of classes"""
        command = self.parseline(line)[0]
        if command == None:
            print('Class not found ')
            print('Allowed classes are \n\tUser\
                    \n\tLocation\n\tTodo\n\tLocationReminder')
        elif not (command in self.classes):
            print("Class doesn't exist")
            print(f"Allowed classes are {cls for cls in self.classes}")
        else:
            new_instance = eval(command)()
            new_instance.save()
            print(new_instance)
            print(f'{new_instance.__class__.__name__}.{new_instance.id}')

    def do_show(self, line):
        '''Shows all entries in the database'''
        args = shlex.split(line)
        if len(args) == 0:
            print('Class name is missing')
            return False
        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print('No instance found')
            else:
                print('instance i missing')
        else:
            print("class does not exist")

    def do_destroy(self, arg):
        '''deletes an instance of the class'''
        args = shlex.split(arg)
        if len(args) == 0:
            print('class name missing')
        elif args[0] in classes:
            if len(args) > 1:
                key == args[0] + "." + args[1]
                if key in models.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print('Instance not found')
            else:
                print('Instance id missing')
        else:
            print(' class does not exists')

                print("** class doesn't exist **")
            return False
        for key in obj_dict:
            obj_list.append(str(obj_dict[key]))
        print("[", end="")
        print(", ".join(obj_list), end="")
        print("]")

    '''def do_update(self, arg):
        """Update an instance based on the class name, id, attribute & value"""
        args = shlex.split(arg)
        integers = ["number_rooms", "number_bathrooms", "max_guest",
                    "price_by_night"]
        floats = ["latitude", "longitude"]
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                k = args[0] + "." + args[1]
                if k in models.storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            if args[0] == "Place":
                                if args[2] in integers:
                                    try:
                                        args[3] = int(args[3])
                                    except:
                                        args[3] = 0
                                elif args[2] in floats:
                                    try:
                                        args[3] = float(args[3])
                                    except:
                                        args[3] = 0.0
                            setattr(models.storage.all()[k], args[2], args[3])
                            models.storage.all()[k].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    '''
    def do_EOF(self, arg):
        ''' Closes the console'''
        return True

    def emptyline(self):
        '''Nothing should happen if no input'''
        return False

    def do_quit(self, arg):
        '''Quit command to close the console'''
        return True

    '''
    def _key_value_parser(self, args):
    """Creates a dictionary from a list of input strings.
    usage is
    user=fuhad
    user.id = 89238
    so it will create a new user with name user = fuhad
    """
    new_dict = {}
    for arg in args:
        if "=" in arg:
            kvp = arg.split('=', 1)
            key = kvp[0]
            value = kvp[1]
            if value[0] == value[-1] == '"':
                value = shlex.split(value)[0].replace('_', ' ')
            else:
                try:
                    value = int(value)
                except:
                    try:
                        value = float(value)
                    except:
                        continue
            new_dict[key] = value
    return new_dict

    '''
    def do_all(self, arg):
        """Returns all the datas in database"""
        args = shlex.split(arg)
        obj_list = []
        if len(arg) == 0:
            obj_dict = models.storage.all()
        elif args[0] in classes:
            obj_dict = models.storage.all(classes[args[0]])
        else:
            print('class doesnt exist')
            return False
        for k in obj_dict:
            obj_list.append(str(obj_dict[k]))
        print("[", end="")
        print(", ".join(obj_list), end="")
        print("]")

if __name__ == '__main__':
    GeoAlert().cmdloop()
