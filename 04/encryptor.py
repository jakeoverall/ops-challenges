from cryptography.fernet import Fernet


def getWritter():
    key = load_key()
    if key == None:
        key = write_key()
    return Fernet(key)


def encryptMessage():
    message = input("Please write your message: ")
    writter = getWritter()
    encrypted = writter.encrypt(message.encode())
    formatted = str(encrypted)[2:len(encrypted)-1]
    print(f"""
CIPHER:
-------------------------------------------
{formatted}
""")


def decryptMessage():
    cipher = input("Please paste your cipher text: ")
    writter = getWritter()
    decrypted = writter.decrypt(cipher.encode())
    print(decrypted)


def encryptFile():
    filePath = input("Please specify the file path: ")
    writter = getWritter()
    with open(filePath, "rb") as file:
        # read all file data
        content = file.read()
    cipher = writter.encrypt(content)
    with open(filePath, "wb") as file:
        file.write(cipher)


def decryptFile():
    filePath = input("Please specify the file path: ")
    writter = getWritter()
    with open(filePath, "rb") as file:
        # read the encrypted data
        content = file.read()
        text = writter.decrypt(content)
    with open(filePath, "wb") as file:
        file.write(text)


def write_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
        return key


def load_key():
    """
    Loads the key from the current directory named `key.key`
    """
    try:
        return open("key.key", "rb").read()
    except:
        return None
