import json
import unittest
from webServer import UpdateRequest


class TestStringMethods(unittest.TestCase):

    def test_id(self):
        test_input = '{ "id":101, "quantity":30, "price": 20, "code":"TNBL"}'
        test_obj = json.loads(test_input)
        rqst = UpdateRequest(test_obj)
        self.assertEqual(rqst.get_id(), 101)

    def test_id_none(self):
        test_input = '{ "quantity":30, "price": 20, "code":"TNBL"}'
        test_obj = json.loads(test_input)
        rqst = UpdateRequest(test_obj)
        self.assertEqual(rqst.get_id(), None)

    def test_id_with_json_string(self):
        test_input = '{ "id":101, "quantity":30, "price": 20, "code":"TNBL"}'
        #test_obj = json.loads(test_input)
        rqst = UpdateRequest(None, test_input)
        self.assertEqual(rqst.get_id(), 101)



