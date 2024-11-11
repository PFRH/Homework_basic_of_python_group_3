import socket
import time

udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
start_time = time.perf_counter()
udp_client.sendto(b"Test", ('localhost', 12345))
udp_client.recvfrom(1024)
end_time = time.perf_counter()

print("UDP reaction time:", end_time - start_time)
