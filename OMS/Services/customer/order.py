from Services.customer.list import showList
from mysqlConnector import MySQL

def placeOrder():
    print("place order worked")
    showList()
    mysql = MySQL.getInstance()
    cursor = mysql.get_cursor()
    productCode = "PEN"
    productCode = input("3 Letter Product Code (All CAPS): ")
    quantity = int(input("How many?: "))

    query = "SELECT quantity FROM inventory WHERE product_code = \"{}\"".format(productCode)
    cursor.execute(query)

    x = cursor.fetchone()
    currentQuantity = x[0]

    if currentQuantity >= quantity:
        newQuantity = currentQuantity - quantity
        query = "UPDATE inventory SET quantity={} WHERE product_code = \"{}\"".format(newQuantity, productCode)
        print(query)
        cursor.execute(query)

