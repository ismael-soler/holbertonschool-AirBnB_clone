#!/usr/bin/python3
import uuid
from datetime import datetime
from models.__init__ import storage


class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        It creates a new instance of the class.
        """
        if kwargs is not None and kwargs != {}:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'my_number':
                    self.my_number = value
                elif key == 'created_at':
                    self.created_at = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == 'updated_at':
                    self.updated_at = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == 'name':
                    self.name = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = str(datetime.now())
            self.updated_at = str(datetime.now())
            storage.new(self)

    def __str__(self):
        """ returns string representation of the object """
        return (f"[{__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """
        `save` updates the `updated_at` attribute of the object to the current time
        """
        self.updated_at = str(datetime.now())
        storage.save()

    def to_dict(self):
        """
        It converts the object to a dictionary.
        """
        print(f"-----++------- {newDict}-----++----")
        self.updated_at = self.updated_at.isoformat("T")
        self.created_at = self.created_at.isoformat("T")
        newDict = self.__dict__
        newDict["__class__"] = __class__.__name__
        return newDict
