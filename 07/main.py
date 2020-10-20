#! /usr/bin/env python3

# Title: Port Mapper
# Author: Jake Overall
# Date: 10/19/2020
# Purpose: Given a target check to see if a range of ports are open

import random
import ipaddress
import signal
from scapy.all import ICMP, IP, sr1, TCP

logs = []
RECIEVED = 0x12
CLOSED = 0x14


def isRecieved(res):
    return res.haslayer(TCP) and res.getlayer(TCP).flags == RECIEVED


def isClosed(res):
    return res.haslayer(TCP) and res.getlayer(TCP).flags == CLOSED


def start_discovery(host, low, high):
    for dport in range(low, high+1):
        try:
            sport = random.randint(100, 999)
            print(f"pinging..... {host}/[{dport}]|[{sport}]")
            ack = IP(dst=host)/TCP(sport=sport, dport=dport, flags="S")
            res = sr1(ack, timeout=1, verbose=0)
            message = f"HOST: {host} PORT: {dport} || "
            if isRecieved(res):
                message += "OPEN ✅"
                close_connection(host, sport, dport)
            elif isClosed(res):
                message += "CLOSED ❌"
            else:
                message += "FILTERED !?"
            print(message)
            message += ',\n'
            logs.append(message)
        except Exception as error:
            print("[ERROR]" + str(error))


def close_connection(host, sport, dport):
    fin = IP(dst=host)/TCP(sport=sport, dport=dport, flags='FA')
    fin_ack = sr1(fin, timeout=1)
    ack = IP(dst=host)/TCP(sport=sport, dport=dport, flags='A')
    sr1(ack)
    print('Disconnected')


def main():
    choice = "Y"
    while choice == "Y":
        host = input("What host would you like to scan?: ") or "scanme.nmap.org"
        low = int(input("What port should I start at? (inclusive): ") or "20") 
        high = int(input("What port should I end at? (inclusive): ") or "80")
        start_discovery(host, low, high)
        print_log(host)
        print("Do you want to try something else?")
        choice = input("[Y]/n ").capitalize()


def print_log(host):
    file = open(f"./logs-{host}.txt", "a")
    file.writelines(logs)
    file.close()


def quit():
    print(" Okay, Bye 👋 ")
    exit(0)


def signal_handler(signal, frame):
    quit()


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    main()
