import signal
import complexity
import password_generator
import ssh_brute
import sys
import banners
import password_checker

running = "Y"

switcher = {
    "1": complexity.main,
    "2": password_generator.generate_password,
    "3": ssh_brute.main,
    "4": quit,
}


def main():
    banners.clear_screen()
    running = "Y"
    while running == "Y":
        try:
            print("""
1. Check Password Complexity
2. Generate Password
3. SSH BRUTE
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
    password_checker.load_passwords()
    main()
