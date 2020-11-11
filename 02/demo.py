import signal
import sys
import pingr
import os
from device import Device 
import banners

devices = [
    Device("8.8.8.8", ["jake.codefellows@gmail.com"], interval= 5), 
    Device("8.8.8.12", ["jake.codefellows@gmail.com"], interval= 5)
]

def confirm_loop(message, action):
    print(message)
    again = input("Y/n: ")
    while again.capitalize() == "Y":
        action()
        print(f"Continue: {message}?")
        again = input("Y/n: ")

def create_system():
    print("ADDING SYSTEM TO MONITOR:")
    address = input("System Address: ")
    device = Device(address)
    devices.append(device)
    confirm_loop("Do you want to recieve notifications if the system is down?", device.add_monitor)

def main(args):
    os.system('cls')
    banners.print_main_banner()
    # confirm_loop("Add a system for monitoring", create_system) SKIP CREATION LOOPS

    for device in devices:
        pingr.add_device(device)
    pingr.start_monitoring()

def signal_handler(signal, frame):
    pingr.stop_monitoring()
    print(" Okay, Bye 👋 ")
    exit(0)


signal.signal(signal.SIGINT, signal_handler)
main(sys.argv)
