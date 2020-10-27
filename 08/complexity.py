import re
import getpass
import unicodedata
import password_checker
from colors import colors


def check_password_complexity(password):
    print(colors.FAIL)
    if(len(password) < 6):
        print(f"{password} || Passwords short in length regardless of complexity are easily cracked choose better!")
        return

    complex, message = check_complexity_rules(password)
    if(complex == False):
        print(
            f"{password} || Your password is not complex enough! {message}")
        return

    is_known_password = password_checker.check_known_passwords(password)
    if(is_known_password):
        print(
            f"{password} || This is a terrible choice it is on the list of known passwords!")
        return

    print(colors.OKGREEN)
    print("SUCCESS THAT IS A GREAT PASSWORD")


def check_complexity_rules(password):
    specials = "%^&*{()}[]!@#<>-_=+,./?;'\"\\/~` "
    has_num_and_case = {'Ll', 'Lu', 'Nd'}.issubset(
        unicodedata.category(ch) for ch in password)
    if not has_num_and_case:
        return {False, "Missing Uppercase or Number"}
    for ch in password:
        if ch in specials:
            return {True, ""}
    return {False, "Missing special characters"}


def main():
    passsword = getpass.getpass('Password:')
    check_password_complexity(passsword)


def test():
    check_password_complexity("test")
    check_password_complexity("testing123")
    check_password_complexity("testing123!")
    check_password_complexity("Testing123!")


if __name__ == "__main__":
    test()
    main()
