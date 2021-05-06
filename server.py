import socket
import os
from _thread import *
new = []
j = 0

ServerSideSocket = socket.socket()
host = '127.0.0.1'
port = 2004
ThreadCount = 0
try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Socket is listening..')
ServerSideSocket.listen(5)

def multi_threaded_client(connection):
    connection.send(str.encode('Server is working:'))
    while True:
        data = connection.recv(2048)
        response = data.decode('utf-8')
        new.append(response)
        
        if not data:
            break
        connection.sendall(str.encode(response))
    connection.close()

while j < 4:
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
    print(new)
    j+=1

x = new
while("" in x) :
    x.remove("")
print(x)
g = 0.5*(float(x[2])) + 0.3*(float(x[1])) + 0.2*(float(x[0]))
print('The desired timestamp for the experiment is :  '+ str(g))

ServerSideSocket.close()