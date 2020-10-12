# Title: ops-401d1: Challenge 04
# Author: Jake Overall
# Date: 10/12/2020
# Purpose: A tool to facilitate encrypting and decrypting files and messages
import signal
import sys
import menu
import encryptor

cont = "Y"

switcher = {
    1: encryptor.encryptFile,
    2: encryptor.decryptFile,
    3: encryptor.encryptMessage,
    4: encryptor.decryptMessage,
    5: quit
}

def main(cont):
    while cont == "Y":
        try:
            choice = menu.printMenu()
            fn = switcher.get(choice, "Invalid Choice")
            fn()
            cont = input("Do you wish to continue? [Y]/n ").capitalize()
        except Exception as err:
            menu.printError(err)
            
def quit():
    print(" Okay, Bye 👋 ")
    exit(0)

def signal_handler(signal, frame):
    quit()



    

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    main(cont)
