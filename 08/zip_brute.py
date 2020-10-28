import signal
import colors
import banners
import password_checker
import zipfile


def unzip(path, extract_to="./", pwd=""):
    try:
        with zipfile.ZipFile(path) as file:
            file.extractall(path=extract_to, pwd=bytes(pwd, "utf-8"))
            zipfile.ZipFile.close(file)
            colors.print_success("[+] FILES EXTRACTED:")
            return True
    except Exception as err:
        raise err



def start_brute(path, extract_to):
    for password in password_checker.passwords:
        try:
            colors.print_warning(f"[*] Attempting to extract with password: {password}")
            if(unzip(path, extract_to, password)):
                return
        except Exception as err:
            msg = str(err)
            if(msg.find("Bad password") == -1):
                print(msg)
                raise err

    colors.print_fail("[!] Unable to extract files, password not found")


def main():
    banners.zip_brute_banner()
    zipfile = input("Zip File: ")
    extract_here = input("Extract Here [Y]/n:").capitalize()
    extract_to = "./"
    if(not extract_here == "Y"):
        extract_to = input("Extract To: ")
    start_brute(zipfile, extract_to)


def signal_handler(signal, frame):
    exit(0)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    password_checker.load_passwords()
    main()
