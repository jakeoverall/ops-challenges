import signal
import complexity
import password_generator

running = "Y"

switcher = {
    "1": complexity.main,
    "2": password_generator.generate_password,
    "3": quit,
}

def main():
    running = "Y"
    while running == "Y":
        try:
            print("""
1. Check Password Complexity
2. Generate Password
3. Quit 
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
