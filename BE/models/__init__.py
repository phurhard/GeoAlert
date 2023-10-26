#!/usr/bin/python3
"""
Initializes storage
"""
from .engine.db_storage import DBStorage
storage = DBStorage()
storage.load()
