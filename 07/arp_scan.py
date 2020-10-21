#! /usr/bin/env python3

# Title: Network ICMP Sweep
# Author: Jake Overall
# Date: 10/19/2020
# Purpose: Discover pingable hosts on a network

import random
import ipaddress
import signal
import scapy.all as scapy
import port_scanner

logs = []

def start_discovery(network = '192.168.0.0/24', dst = 'ff:ff:ff:ff:ff:ff'):
    request = scapy.ARP()
    request.pdst = network
    broadcast = scapy.Ether()
    broadcast.dst = dst
    request_broadcast = broadcast / request
    clients = scapy.srp(request_broadcast, timeout = 1)[0]
    for host in clients:
        for address in host:
            address.psrc
            
            logs.append(f"\n----------START {address.psrc}------------\n")
            logSet = port_scanner.start_discovery(address.psrc, 20, 25)
            for entry in logSet:
                logs.append(entry)
            logs.append(f"\n----------END {address.psrc}------------\n")
    print_log(network)

def main():
    try:
        network = input("What network would you like to scan?: ") or "192.168.1.0/24"
        start_discovery(network)
        print_log(network)
    except Exception as err:
        print(err)


def print_log(host):
    file = open(f"./logs-arp-{host.replace('/', '.')}.txt", "a")
    for logset in logs:
        file.writelines(logset)
    file.close()


def quit():
    print(" Okay, Bye 👋 ")
    exit(0)


def signal_handler(signal, frame):
    quit()

def test():
    start_discovery("192.168.1.0/29")

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    test()
    main()

