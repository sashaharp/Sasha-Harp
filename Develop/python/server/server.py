import socket

HOST = '192.168.1.205'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
__TEXT__ = 'text/html'


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            stri = """HTTP/1.1 200 OK
Content-Type: #content#; charset=utf-8
Content-Length: #len#
Connection: keep-alive
Content-Language: en-US
Server: meinheld/0.6.1

"""
            conn.sendall(stri.replace("#content#", __TEXT__).replace("#len#", str(len(stri.encode()))).encode())