import mysql.connector

class MySQL:
    connectionObject = None
    __instance = None
    cursor = None
    @staticmethod
    def getInstance():
        if MySQL.__instance == None:
            MySQL()
        return MySQL.__instance

    def __init__(self):
        if MySQL.__instance != None:
            raise Exception("This class is a singleton")
        else:
            MySQL.__instance = self

    def open_connection(self):
        self.connectionObject = mysql.connector.connect(host="localhost", user="root", password="password",
                                                        database='OMS', autocommit=True)
        self.cursor = self.connectionObject.cursor()

    def get_cursor(self):
        return self.cursor

    def commit(self):
        return self.commit

    def close_connection(self):
        self.connectionObject.close()


