import socket
import time

HOST = "localhost"
PORT = 33333

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind((HOST, PORT))

while True:
    received = s.recvfrom(4096)
    rMsg = received[0].decode('utf-8')
    rHost = received[1][0]
    rPort = received[1][1]

    if rMsg == 'ping':
        print(
            "Received: '{0}' from {1}:{2} - PONG!".format(rMsg, rHost, rPort))
    else:
        print(
            "Received: '{0}' from {1}:{2}".format(rMsg, rHost, rPort))

    time.sleep(1)
