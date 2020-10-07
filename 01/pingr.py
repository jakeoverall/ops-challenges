#!/usr/bin/env python3

# Title: ops-401d1: Challenge 01
# Author: Jake Overall
# Date: 10/6/2020
# Purpose: Ping Test with log writter

import sys
import getopt
import time
import datetime
import signal
from pythonping import ping
from colors import colors

log = ["\n----------------------PINGR_START----------------------\n"]

def setup(args):
    ip = args.pop()
    exit_call(ip)
    start_message = f"[ATTEMPTING TO PING] {ip}"
    log.append(start_message)
    print(f"{colors.OKBLUE} {start_message}")
    return ip


def do_work(ip):
    now = datetime.datetime.now()
    delay()
    status = str(ping(ip, count=1, verbose=False, out=None))
    check = status.startswith("Reply") == True 
    color = colors.OKGREEN if check else colors.FAIL
    emote = "✅" if check else "❌"
    entry = f"[{now}] {emote} {status} | {ip}\n"
    print(f"{color} {entry}")
    log.append(entry)


def exit_call(ip):
    if ip == "" or ip.endswith(".py") == True:
        print(f"{colors.FAIL} please set an ip to ping")
        exit()

def delay():
    dotes = "...................."
    print(colors.WARNING)
    for dot in dotes:
        print(dot, end="", flush=True)
        time.sleep(0.1)

def main(args=[""]):
    ip = setup(args)
    while True:
        do_work(ip)


def signal_handler(signal, frame):
  log.append("----------------------PINGR_END----------------------\n")
  file = open("./pingr_logs.txt", "a")
  file.writelines(log)
  file.close()
  print(" Okay, Bye 👋 ")
  exit(0)



signal.signal(signal.SIGINT, signal_handler)
main(sys.argv)