import signal
import sys
import pingr
import os
from device import Device
import banners

devices = []


def confirm_loop(message, action):
    print(message)
    again = input("Y/n: ").capitalize()
    while again == "Y":
        action()
        print(f"Continue: {message}?")
        again = input("Y/n: ").capitalize()
        again = "Y" if again != 'N' else "n"


def create_system():
    print("ADDING SYSTEM TO MONITOR:")
    address = input("System Address: ")
    device = Device(address)
    devices.append(device)
    confirm_loop(
        "Do you want to recieve notifications if the system is down?", device.add_monitor)


def main(args):
    os.system('cls')
    banners.print_main_banner()
    confirm_loop("Add a system for monitoring", create_system)
    device_count = len(devices)
    if device_count == 0:
        quit()

    print(f"MONITORING {device_count} DEVICES")

    for device in devices:
        pingr.add_device(device)
    pingr.start_monitoring()


def quit():
    print(" Okay, Bye 👋 ")
    exit(0)

def signal_handler(signal, frame):
    pingr.stop_monitoring()
    quit()


signal.signal(signal.SIGINT, signal_handler)
main(sys.argv)
