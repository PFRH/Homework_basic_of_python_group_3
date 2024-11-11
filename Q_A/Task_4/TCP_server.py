import socket

tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server.bind(('localhost', 12345))
tcp_server.listen(1)
conn, addr = tcp_server.accept()

while True:
    data = conn.recv(1024)
    conn.sendall(data)
