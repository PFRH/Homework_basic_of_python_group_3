import socket

udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server.bind(('localhost', 12345))

while True:
    message, addr = udp_server.recvfrom(1024)
    udp_server.sendto(message, addr)
