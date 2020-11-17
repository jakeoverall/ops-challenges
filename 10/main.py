import signal
import banners
import find_module

switcher = {
    "1": find_module.main,
    "5": quit
}


def main():
    banners.start_banner()
    running = "Y"
    while running == "Y":
        try:
            print("""
1. Hash Files
5. Quit 
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


if __name__ == "__main__":
    main()
