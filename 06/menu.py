import os
import time


def printMenu():
    clear()
    print("""
            1 - Encrypt File
            2 - Decrypt File
            3 - Encrypt Message
            4 - Decrypt Message
            5 - Encrypt Directory 
            6 - Decrypt Directory
            7 - Quit
        """)
    choice = input("Please Select an option: ")
    choice = round(int(choice))
    return choice


def printError(e=""):
    clear()
    print(f"[SYSTEM_ERROR] Hang on, Something went wrong.... {e}")
    time.sleep(3)
    clear()


def clear():
    clear = "cls" if os.name == "nt" else "clear"
    os.system(clear)
