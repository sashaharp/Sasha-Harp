import socket

port = 54321
s = socket.socket()
host = '192.168.1.205'

s.connect((host, port))

filename=input()
f = open(filename,'rb')
l = f.read(16384)
s.send(l)
f.close()

print('Done sending')