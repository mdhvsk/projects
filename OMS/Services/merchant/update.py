from mysqlConnector import MySQL
from datetime import datetime
def callUpdate(inventory_id, product_code, product_desc, price, quantity):
    print("callUpdate worked")
    mysql = MySQL.getInstance()
    cursor = mysql.get_cursor()
    valid_inputs =[]
    if product_code != None:
        valid_inputs.append("product_code = \"" + product_code + "\", ")
    if product_desc != None:
        valid_inputs.append("product_description = \"" + product_desc + "\", ")
    if price != None:
        valid_inputs.append("price = " + str(price) + ", ")
    if quantity != None:
        valid_inputs.append("quantity = " + str(quantity) + ", ")

    string_query =""
    for i in range(len(valid_inputs)):
        string_query += valid_inputs[i]
    final_query = string_query[:len(string_query)-2]
    query = "UPDATE inventory SET {}WHERE inventory_id = \"{}\" ".format(final_query, inventory_id )
    print(query)
    cursor.execute(query)
    return