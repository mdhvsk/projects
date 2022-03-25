import json
from os import stat
from flask import Flask, jsonify, request, Response
from UI.merchant.inputUpdate import ask_update_values
from Services.merchant.list import callList
from mysqlConnector import MySQL
from Services.merchant.update_request import UpdateRequest
from Services.merchant.update import callUpdate

app = Flask(__name__,static_url_path='',static_folder='web')
#app.run()
@app.before_request
def init_db_connection():
    mysql = MySQL.getInstance()
    mysql.open_connection()
    print("DB: connected")
  # here I connect to my DB

@app.teardown_request
def destroy_db(exception):
    mysql = MySQL.getInstance()
    mysql.close_connection()
    print("DB: closed")

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
def inventory_update():
    update = UpdateRequest(request.get_json())

    callUpdate(update.get_id(), update.get_code(), update.get_desc(), update.get_price(),
               update.get_quantity())

    response = Response("{}", status=200, mimetype='application/json')

    return response

@app.route("/inventory/list", methods = ['GET'])
def inventory_list():
    mysql = MySQL.getInstance()
    mysql.open_connection()
    result = callList()
    r = convert_to_json(result)
    print(r)
    print("------------")

    response = Response(r, status=200, mimetype='application/json')
    mysql.close_connection()
    return response
if __name__ == '__main__':
    app.run(debug=True, port=5000)