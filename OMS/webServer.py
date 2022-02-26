import json
from os import stat
from flask import Flask, jsonify, request, Response
from UI.merchant.inputUpdate import ask_update_values
from Services.merchant.list import callList
from mysqlConnector import MySQL

app = Flask(__name__)
#app.run()


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/students")
def get_students():
    students = [
        {'name': 'Ajoy', 'age': 25},
        {'name': 'Madhav ', 'age': 20}
    ]
    return jsonify(students)


def convert_to_json(result):
    str = ""
    i = 0
    for r in result:
        print(r)
        if (i > 0):
            str = str + ","
        i = i + 1

        cstr = "{{\"product_code\":\"{}\",\"product_description\":\"{}\",\"price\":{},\"quantity\":{}}}"
        str = str + cstr.format(r[0], r[1], r[2], r[3])
    str = "[" + str + "]"
    return str


@app.route("/inventory/update", methods=['POST'])
class UpdateRequest:
    def __init__(self, json_str):
        self.json_obj = json.loads(json_str)

    def get_id(self):
        output = None
        try:
            output = self.json_obj["id"]
        except:
            output = None
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


def inventory_update():
    data = request.get_json()


    print(data)
    inventory_id, product_code, product_desc, price, quantity = ask_update_values()
    result = [inventory_id, product_code, product_desc, price, quantity]
    #[("TNBL", "Tennis Ball", 2.19, 50), ("IPHONE", "IPHONE 13", 899.99, 5)]
    r = convert_to_json(result)
    print(r)

    print("------------")

    response = Response(r, status=200, mimetype='application/json')

    return response

@app.route("/inventory/list", methods = ['GET'])
def inventory_list():
    mysql = MySQL.getInstance()
    mysql.open_connection()
    data = request.get_json()
    result = callList()
    r = convert_to_json(result)
    print(r)
    print("------------")

    response = Response(r, status=200, mimetype='application/json')
    mysql.close_connection()
    return response
if __name__ == '__main__':
    app.run(debug=True, port=5000)