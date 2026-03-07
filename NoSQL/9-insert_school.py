#!/usr/bin/env python3
""" Task 9: Insert a document in Python """


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs
    Returns the new _id
    """
    new_school = mongo_collection.insert_one(kwargs)
    return new_school.inserted_id
