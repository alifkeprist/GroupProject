import socket
import os
from _thread import *

ServerSocket = socket.socket(family  = socket.AF_INET, type = socket.SOCK_STREAM)
host = '192.168.114.6'
port = 8888
ThreadCount = 0

try:
   ServerSocket.bind((host, port))
except socket.error as e:
   print(str(e))

print('Waiting for Connection..')
ServerSocket.listen(5)

def threaded_client(connection):
   connection.send(str.encode('Welcome To SOP Mart\n'))
   while True:
      data = connection.recv(2048)
      reply = 'Customer Recorded: ' + data.decode('utf-8')
      if not data:
         break
      connection.sendall(str.encode(reply))

   connection.close()

while True:
   Client, address = ServerSocket.accept()
   print('Connected to:' + address[0] + ':' + str(address[1]))
   start_new_thread(threaded_client, (Client, ))
   ThreadCount += 1
   print('Day: ' + str(ThreadCount))
ServerSocket.close()
