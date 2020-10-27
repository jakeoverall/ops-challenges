import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-=`~!@#$%^&*()_+[{]}'\"\\/?.,<>"


def generate_password():
    password = ""
    min_length = int(input("How many characters should the password be? "))
    options = list(chars)
    random.shuffle(options)
    random.shuffle(options)
    random.shuffle(options)
    random.shuffle(options)
    options = "".join(options)
    for c in range(min_length):
        password += random.choice(options)
    print(f"""
Password
------------------------
{password}
""")

if __name__ == "__main__":
    generate_password()
