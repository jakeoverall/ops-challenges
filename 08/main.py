import signal
import complexity
import password_generator
import ssh_brute
import zip_brute
import sys
import banners
import password_checker

running = "Y"

switcher = {
    "1": ssh_brute.main,
    "2": zip_brute.main,
    "3": complexity.main,
    "4": password_generator.generate_password,
    "5": quit,
}


def main():
    banners.brute_banner()
    running = "Y"
    while running == "Y":
        try:
            print("""
1. SSH Brute
2. Zip Brute
3. Check Password Complexity
4. Generate Password
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
    running = ""
    print(" Okay, Bye 👋 ")
    exit(0)


def signal_handler(signal, frame):
    quit()


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    password_checker.load_passwords()
    main()
