from mysqlConnector import MySQL


def showList():
    print("showList worked")
    query = ''' SELECT product_code, product_description, price FROM inventory;'''

    mysql = MySQL.getInstance()
    cursor = mysql.get_cursor()
    cursor.execute(query)
    response = cursor.fetchall()
    return response