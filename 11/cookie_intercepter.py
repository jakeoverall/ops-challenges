import requests
import colors

def get_cookies(url):
    session = requests.Session()
    session.get(url)
    colors.print_header(f"--- {url} ---")
    colors.print_success(f"  [~] COOKIES: {session.cookies}")



def main():
    url = input("Enter Url: ")
    get_cookies(url)