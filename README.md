# UDP Ping Pong

## Usage

First you need to install the dependencies.

```sh
# Install Pipenv, a Python Virtual Enviroment Manager
$ python3 -m pip install pipenv

# Install the dependencies
$ pipenv install

# Go to the Virtual Enviroment
$ pipenv shell
```

Then you can run the UDP server and client

```sh
# Runnig the server
$ python3 server.py

# Using the client
$ python3 client.py
```

## Client Usage

```UDP Ping Pong

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

```

## MIT License
