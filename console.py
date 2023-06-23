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

    classes = {"User": User, "Location": Location, "Todo": Todo, "LocationReminder": LocationReminder}

    def do_create(self, line):
        """Creates a new instance of classes"""
        args = line.split()
        if len(args) == 0:
            print('Class name is missing ')
            print('Allowed classes are \n\tUser\
                    \n\tLocation\n\tTodo\n\tLocationReminder')
            return False
        elif not (args[0] in self.classes):
            print("Class doesn't exist")
            print(f"Allowed classes are \n\tUser\
                    \n\tLocation\n\tTodo\n\tLocationReminder")
            return False
        else:
            new_dict = self._key_value_parser(args[1:])
            objs = models.storage.all()
            try:
                if objs:
                    for obj in objs:
                        if new_dict['username'] in obj:
                            print('User already exists')
                            return False
                        else:
                            continue
            except Exception as e:
                pass
            new_instance = self.classes[args[0]](**new_dict)
            new_instance.save()
            print(new_instance)
            if new_instance.__class__.__name__ == "User":
                print(f"{new_instance.__class__.__name__}.{new_instance.username}")
            else:
                print(f'{new_instance.__class__.__name__}.{new_instance.id}')

    def do_show(self, line):
        '''Shows all entries in the database'''
        args = shlex.split(line)
        if len(args) == 0:
            print('Class name is missing')
            return False
        if args[0] in self.classes:
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

    def do_remove(self, arg):
        '''removes'''
        models.storage.removed(eval(arg))
    def do_delete(self, arg):
        '''deletes an instance of the class'''
        args = shlex.split(arg)
        if len(args) == 0:
            print('class name missing')
        elif args[0] in self.classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    models.storage.delete(key)
                    models.storage.save()
                else:
                    print('Instance not found')
            else:
                print('Instance id missing')
        else:
            print(' class does not exists')

    def do_update(self, arg):
        """Update an instance based on the class name, id, attribute & value"""
        args = shlex.split(arg)
        strings = ["title", "description", "due_date", "lastname", "email", "password"]
        floats = ["latitude", "longitude"]
        boolean = ["completed"]
        dates = ["due_dates"]

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in self.classes:
            if len(args) > 1:
                k = args[0] + "." + args[1]
                if k in models.storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            print(models.storage.all()[k].__dir__())
                            
                            if args[0] == "Todo":
                                if args[2] in strings:
                                    try:
                                        args[3] = str(args[3])
                                    except:
                                        args[3] = ""
                                elif args[2] in boolean:
                                    try:
                                        args[3] = bool(args[3])
                                    except:
                                        args[3] = 0.0
                                elif args[2] in dates:
                                    try:
                                        args[3] = datetime.strftime(args[3])
                                    except:
                                        args[3] = datetime.utcnow

                            setattr(models.storage.all()[k], args[2], args[3])
                            setattr(models.storage.all()[k], str(models.storage.all()[k].updated_at), datetime.utcnow)
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
 
    def do_EOF(self, arg):
        ''' Closes the console'''
        return True

    def emptyline(self):
        '''Nothing should happen if no input'''
        return False

    def do_quit(self, arg):
        '''Quit command to close the console'''
        return True

    
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
                    value = shlex.split(value)[0].replace('_', ' ')# work on fixing this code such that even if there is space in the title and description declaration, it wont split it
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

    
    def do_all(self, arg):
        """Returns all the datas in database"""
        args = shlex.split(arg)
        obj_list = []
        if len(arg) == 0:
            obj_dict = models.storage.all()
        elif args[0] in self.classes:
            obj_dict = models.storage.all(eval(args[0]))
        else:
            print('class doesnt exist')
            return False
        for k in obj_dict:
            obj_list.append(str(obj_dict[k]))
        print("[", end="")
        print(", ".join(obj_list), end="")
        print("]")

    def do_reload(self, arg):
        '''reloads the current instance and updates it'''
        print('Got here')
        models.storage.reload()
        print('Reloaded')

if __name__ == '__main__':
    GeoAlert().cmdloop()
