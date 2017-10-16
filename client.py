#!/usr/bin/env python
import socket
import dbus
from subprocess import call, Popen, PIPE
import time
import sys

switch_back=1
switch_delay=1

def client():
    TCP_IP = '127.0.0.1'
    TCP_PORT = 5005
    BUFFER_SIZE = 1024
    MESSAGE = "Server response!"

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(MESSAGE)
    data = s.recv(BUFFER_SIZE)
    s.close()
    print "Received data:", data

def main():
    try:
        client()
    except:
        print("Exiting")
        sys.exit(0)

main()
