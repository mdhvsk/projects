from mysqlConnector import MySQL


def callList():
    print("callList worked")
    query = ''' SELECT * FROM inventory;'''

    mysql = MySQL.getInstance()
    cursor = mysql.get_cursor()
    cursor.execute(query)
    response = cursor.fetchall()

    return response
