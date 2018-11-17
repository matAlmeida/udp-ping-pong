import socket
import time

HOST = "localhost"
PORT = 33333
message = "ping"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    s.sendto(message.encode(), (HOST, PORT))
    print("sent: {0}", message)
    time.sleep(1)
