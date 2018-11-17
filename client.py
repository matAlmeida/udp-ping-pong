"""UDP Ping Pong

Usage:
  client.py [-m MSG] [-n TIMES] [-H HOST] [-P PORT] [-d DELAY | --delay DELAY]
  client.py (-h | --help)
  client.py --version

Options:
  -h --help         Show this screen.
  --version         Show version.
  -m MSG            Message to be sent [default: ping]
  -n TIMES          Times to run te ping [default: inf].
  -H HOST           Target Host [default: localhost]
  -P PORT           Target Post [default: 33333]
  -d --delay DELAY  Delay in seconds between packages sent [default: 1]

"""
from docopt import docopt
import socket
import time


if __name__ == '__main__':
    arguments = docopt(__doc__, version='Naval Fate 2.0')

    message = arguments['-m']
    repetitions = arguments['-n']
    HOST = arguments['-H']
    PORT = int(arguments['-P'])
    delay = int(arguments['--delay'])

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    if repetitions == 'inf':
        while True:
            s.sendto(message.encode(), (HOST, PORT))
            print("Sent '{0}' to {1}:{2}".format(message, HOST, PORT))
            time.sleep(delay)
    else:
        for i in range(int(repetitions)):
            s.sendto(message.encode(), (HOST, PORT))
            print("Sent '{0}' to {1}:{2}".format(message, HOST, PORT))
            time.sleep(delay)
