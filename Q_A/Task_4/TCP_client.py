import socket
import time

tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_client.connect(('localhost', 12345))
start_time = time.perf_counter()
tcp_client.sendall(b"Test")
tcp_client.recv(1024)
end_time = time.perf_counter()

print("TCP reaction time:", end_time - start_time)
