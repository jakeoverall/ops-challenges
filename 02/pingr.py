#!/usr/bin/env python3

# Title: ops-401d1: Challenge 01
# Author: Jake Overall
# Date: 10/6/2020
# Purpose: Ping Test with log writter

import sys
import getopt
import time
import datetime
import threading
import asyncio
from pythonping import ping
from colors import colors

loop = asyncio.get_event_loop()
monitoring = {}


def setup(device):
    device.log.append(
        "\n----------------------PINGR_START----------------------\n")
    start_message = f"[ATTEMPTING TO PING] {device.address}\n"
    device.log.append(start_message)
    print(f"{colors.OKBLUE} {start_message}")


async def status_check(device):
    while True:
        now = datetime.datetime.now()
        status = str(ping(device.address, count=1, verbose=False, out=None))

        check = status.startswith("Reply") == True
        color = colors.OKGREEN if check else colors.FAIL
        emote = "✅" if check else "❌"

        entry = f" [{now}] {emote} {status} | {device.address}\n"
        print(f"{color} {entry}")
        device.log.append(entry)
        device.active = check

        if device.active == False:
            device.on_fail_to_reach_system(entry)

        await asyncio.sleep(device.interval)


def add_device(device):
    monitoring[device.address] = device
    setup(device)


def start_monitoring():
    for device in monitoring.values():
        asyncio.ensure_future(status_check(device))
    loop.run_forever()


def stop(device):
    device.log.append(
        "----------------------PINGR_END----------------------\n")
    file = open(f"./logs/{device.address}-log.txt", "a")
    file.writelines(device.log)
    file.close()
    del monitoring[device.address]


def stop_monitoring():
    for device in monitoring:
        stop(device)

    loop.close()
