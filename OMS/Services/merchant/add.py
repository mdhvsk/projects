from mysqlConnector import MySQL
from datetime import datetime

def callAdd(productCode, productDesc, price, quantity):
    print("callAdd worked")
    mysql = MySQL.getInstance()
    cursor = mysql.get_cursor()



    timestamp = datetime.now()
    insert_data = "INSERT into inventory (product_code,product_description,price, quantity,create_ts, Update_ts) \
    values (%s,%s,%s, %s,%s,%s)"
    cursor.execute(insert_data, (productCode, productDesc, price, quantity, timestamp, timestamp))
    mysql.commit()


    return

    # do i need to return values if it is just an add, can't user receive values from list?
