import socket

port = 54321
s = socket.socket()
host = '93.133.18.167'

s.connect((host, port))

filename='Data/test.zip'
f = open(filename,'rb')
l = f.read(1024)
while l:
    s.send(l)
    l = f.read(1024)
    print("next sent.")
f.close()
s.close()

print('Done sending')