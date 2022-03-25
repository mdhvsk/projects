import json


class UpdateRequest:
    def __init__(self, json_obj, json_str=None):
        self.json_obj = json_obj
        if json_str != None:
            self.json_obj = json.loads(json_str)

    def get_id(self):
        output = None
        try:
            output = self.json_obj["id"]
        except:
            output = None
        return output

    def get_id_with_exception(self):
        try:
            output = self.json_obj["id"]
        except:
            raise Exception("ID not present")
        return output

    def get_code(self):
        output = None
        try:
            output = self.json_obj["product_code"]
        except:
            output = None
        return output

    def get_desc(self):
        output = None
        try:
            output = self.json_obj["product_description"]
        except:
            output = None
        return output

    def get_price(self):
        output = None
        try:
            output = self.json_obj["price"]
        except:
            output = None
        return output

    def get_quantity(self):
        output = None
        try:
            output = self.json_obj["quantity"]
        except:
            output = None
        return output
