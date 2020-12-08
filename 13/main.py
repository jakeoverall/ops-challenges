#!/usr/bin/python3

import socket

sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
timeout = 500

def portScanner():
    sockmod.settimeout(timeout)
    host = input("IP address to scan: ")
    port = input('Please select your target port: ')
    if sockmod.create_connection(host, port):
        print("Port open")
    else:
        print("Port closed")

portScanner()
