passwords = {}


def load_passwords():
    with open("passdump.txt", "r", errors='ignore') as f:
        for line in f:
            key = line.strip()
            passwords[key] = True


def check_known_passwords(password):
    password = password.lower()
    if(len(passwords) == 0):
        load_passwords()
    if(password in passwords):
        return True
