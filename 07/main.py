import signal
import network_sweeper
import port_scanner
import arp_scan

running = "Y"

switcher = {
    "1": network_sweeper.main,
    "2": port_scanner.main,
    "3": arp_scan.main,
    "4": quit,
}

def main():
    running = "Y"
    while running == "Y":
        try:
            print("""
1. Network Sweep
2. Port Scan
3. Intense Scan
4. Quit 
            """)
            option = input("> : ")
            if option in switcher:
                switcher[option]()
                print("Do you wish to continue?")
            running = input("Y/n: ").capitalize()
        except Exception as e:
            print(e)
    quit()

def quit():
    running = ""
    print(" Okay, Bye 👋 ")
    exit(0)


def signal_handler(signal, frame):
    quit()


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    main()
