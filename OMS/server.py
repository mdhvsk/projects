#!/usr/bin/env python3

import socket
from Services.merchant import list
from mysqlConnector import MySQL
import functools
import operator


def convertTuple(tup):
    str = functools.reduce(operator.add, (tup))
    return str
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 60000       # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    response = "EMPTY"
    mysql = MySQL.getInstance()
    mysql.open_connection()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            print(data)
            if not data:
                break
            #if data == "1|":
            response = list.callList()
            r = convertTuple(response[0])
            print(r)
            conn.sendall(r.encode())
            print(data)
    mysql.close_connection()
