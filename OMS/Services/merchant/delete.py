from mysqlConnector import MySQL


def callDelete(inventoryID):
    print("callDelete worked")

    mysql = MySQL.getInstance()
    cursor = mysql.get_cursor()
    query = "DELETE FROM inventory WHERE inventory_id = %s"%inventoryID
    cursor.execute(query)
    return