#!/usr/bin/python3
print("\t\t***Simple Server By Ayedi***")
import socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 8080
serversocket.bind((host, port))
serversocket.listen(5)

while True:
    clientsocket,address = serversocket.accept()
    print("Connection From : " % str(address))
    message = 'welcome in my server' + "\r\n"
    clientsocket.send(message)
    clientsocket.close()
