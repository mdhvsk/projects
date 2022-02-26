import unittest
from webServer import UpdateRequest


class TestStringMethods(unittest.TestCase):

    def test_id(self):
        test_input = '{ "id":101, "quantity":30, "price": 20, "code":"TNBL"}'
        rqst = UpdateRequest(test_input)
        self.assertEqual(rqst.get_id(), 101)

    def test_id_none(self):
        test_input = '{ "quantity":30, "price": 20, "code":"TNBL"}'
        rqst = UpdateRequest(test_input)
        self.assertEqual(rqst.get_desc(), None)

    def test_invalid_json(self):
        test_input = '{ "quantity":30 "price": 20, "code":"TNBL"}'
        # the call to create update_request should raise an Exception as
        # json in invalid (missing comma before price). json.loads should fail
        self.assertRaises(Exception, UpdateRequest, (test_input))

