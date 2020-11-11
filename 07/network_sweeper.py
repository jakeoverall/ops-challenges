#! /usr/bin/env python3

# Title: Network ICMP Sweep
# Author: Jake Overall
# Date: 10/19/2020
# Purpose: Discover pingable hosts on a network

import random
import ipaddress
import signal
from scapy.all import ICMP, IP, sr1, TCP

logs = []
CODES = [1,2,3,9,10,13]

def isBlocked(res):
    return res.haslayer(ICMP) and res.getlayer(ICMP).type == 3 and res.getlayer(ICMP).code in CODES


def start_discovery(network):
    for host in network:
        try:
            print(f"pinging..... {host}")
            ack = IP(dst=host)/ICMP()
            res = sr1(ack, timeout=1, verbose=0)
            message = f"HOST: {host} || "
            if not res:
                message += "UNRESPONSIVE"
            elif isBlocked(res):
                message += "BLOCKED"
            else:
                message += "OPEN"
            
            print(message)
            message += ',\n'
            logs.append(message)
        except Exception as error:
            print("[ERROR]" + str(error))


def main():
    try:
        host = input("What network would you like to scan?: ") or "192.168.1.0/24"
        network = ipaddress.ip_network(host)
        start_discovery(network.hosts())
        print_log(host)
    except Exception as err:
        print(err)


def print_log(host):
    file = open(f"./logs-{host.replace('/', '.')}.txt", "a")
    file.writelines(logs)
    file.close()


def quit():
    print(" Okay, Bye 👋 ")
    exit(0)


def signal_handler(signal, frame):
    quit()


def test():
    start_discovery(["192.168.1.97"])

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    test()
    main()
