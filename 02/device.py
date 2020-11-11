import mailer
from email.message import EmailMessage

class Device:
    def __init__(self, address="", monitors=[], active=False, interval = 5):
        self.address = address
        self.monitors = monitors
        self.active = active
        self.interval = interval
        self.log = []
        self.failed_attempts = 0
    
    def add_monitor(self):
        email = input("Enter Email: ")
        self.monitors.append(email)

    def notify_monitors(self, message):
        mailer.send(self.monitors, message)

    def on_fail_to_reach_system(self, message=""):
        self.failed_attempts += 1
        if self.failed_attempts > 1:
            self.notify_monitors(message)
            self.interval = 60 * 60
            self.failed_attempts = 0
    
