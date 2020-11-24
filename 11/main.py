import signal
import banner_grabber
import cookie_intercepter

running = "Y"

switcher = {
    "1": banner_grabber.main,
    "2": cookie_intercepter.main,
    "4": quit,
}

def main():
    running = "Y"
    while running == "Y":
        try:
            print("""
1. Banner Grabbing
2. Cookies Yum Yum
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
    print(" Okay, Bye 👋 ")
    exit(0)


def signal_handler(signal, frame):
    quit()


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    main()
