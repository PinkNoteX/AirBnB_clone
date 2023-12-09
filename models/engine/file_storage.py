#!/usr/bin/python3
""" serialize and deserialize to and from JSON file """
import json
import datetime


class FileStorage:
    """ FileStorage class """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ add new obj to json file """
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file """
        diction = {}
        for key, value in FileStorage.__objects.items():
            diction[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as f:
            json.dump(diction, f)

    def reload(self):
        """ deserializes the JSON file to __objects """
        dic = {}
        try:
            from models.base_model import BaseModel
            with open(self.__file_path, "r") as f:
                dic = json.load(f)
                for key, value in dic.items():
                    FileStorage.__objects[key] = BaseModel(**value)
        except IOError:
            pass
