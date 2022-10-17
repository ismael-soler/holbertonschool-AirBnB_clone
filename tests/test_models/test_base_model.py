#!/usr/bin/python3
"""Tests for base class BaseModel"""
from time import sleep
import unittest
from models.base_model import BaseModel
from models import storage
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    ''' unittest class for checking BaseModel'''

    def test_save(self):
        ''' test save method '''
        storage.all().clear()
        model = BaseModel()
        try:
            oldDictValue = model.__dict__["test"]
        except Exception:
            oldDictValue = None
        model.__dict__["test"] = "assertTest"
        model.save()
        objDict = storage.all()
        objId = model.id
        objValue = objDict[f"BaseModel.{objId}"]
        self.assertNotEqual(objValue.__dict__["test"], oldDictValue)

    def test_to_dict(self):
        ''' test dictionary representation of object method'''
        model1 = BaseModel()
        m_dic = model1.to_dict()
        self.assertEqual(m_dic['id'], model1.id)
        self.assertEqual(m_dic['__class__'], model1.__class__.__name__)

    def test_self_id(self):
        ''' check instance id'''
        base_m = BaseModel()
        self.assertIs(str, type(base_m.id))

    def test_self_created_at(self):
        ''' check the created_at metod '''
        base_m1 = BaseModel()
        self.assertIs(datetime, type(base_m1.created_at))

    def test_str(self):
        """Test the string represtenation method of the instance"""
        b_m = BaseModel()
        self.assertEqual(f'[{type(b_m).__name__}] ({b_m.id}) {b_m.__dict__}',\
            str(b_m))

if __name__ == '__main__':
    unittest.main()
