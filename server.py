import socket
import time

HOST = "localhost"
PORT = 33333

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind((HOST, PORT))

while True:
    msg = s.recv(30).decode('utf-8')
    if msg == 'ping':
        print("pong")

    time.sleep(1)
