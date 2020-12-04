#!/usr/bin/python3

import nmap

scanner = nmap.PortScanner()

print("Nmap Automation Tool")
print("--------------------")

ip_addr = input("IP address to scan: ")
print("The IP you entered is: ", ip_addr)
resp = input("""\nSelect scan to execute:
                1) SYN ACK Scan
                2) UDP Scan
                3) Ping Scan\n""")
print("You have selected option: ", resp)

range = input('Please select your port range (start-end)')

if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, range, '-v -sS')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp == '2':
    scanner.scan(hosts=ip_addr+'/24', arguments=f'-n -sP -p {range}')
elif resp == '3':
    scanner.scan(hosts=ip_addr+'/24', arguments=f'-oX -p {range} -sV')
elif resp >= '4':
    print("Please enter a valid option")
``
