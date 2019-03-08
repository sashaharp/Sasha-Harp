import socket

s = socket.socket()             # Create a socket object
host = '192.168.1.205'     # Get local machine name
port = 54321                    # Reserve a port for your service.
s.bind((host, port))
s.listen(3)

while True:
    conn, addr = s.accept()
    while True:
        print('receiving data...')
        data = s.recv(16384)
        if not data:
            break
        # write data to a file
        with open('Data\\file.txt', 'wb') as f:
            f.write(data)

f.close()
print('Successfully get the file')
s.close()
print('connection closed')