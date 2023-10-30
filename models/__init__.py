#!/usr/bin/python3
"""
Initializes storage
"""


from models.engine.db_storage import DBStorage
storage = DBStorage()
storage.reload()
