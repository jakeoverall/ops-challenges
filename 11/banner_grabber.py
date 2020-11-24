import signal
import os
from colors import print_success, print_header, print_warning

def start_discovery(host, port):
    try:
        message = f"--- HOST: {host} PORT: {port} ---"
        print_header(message)
        
        print_warning("[~] curl")
        os.system(f"curl –s –I {host}")
        print_warning("[~] wget")
        os.system(f"wget –q –S {host}")
        print_warning("[~] netcat")
        os.system(f"nc {host} {port}")
        print_warning("[~] telnet")
        os.system(f"telnet {host} {port}")
        print_warning("[~] nmap")
        os.system(f"nmap -sV –p{port} {host}")
        
    except Exception as error:
        print("[ERROR]" + str(error))


def main():
    host = input("What host would you like to scan?: ") or "scanme.nmap.org"
    port = int(input("What port should I use?: ") or "80") 
    start_discovery(host, port)


def quit():
    print(" Okay, Bye 👋 ")
    exit(0)


def signal_handler(signal, frame):
    quit()


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    main()
