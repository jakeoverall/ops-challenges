from scapy.all import ICMP, IP, sr1, TCP

# Define target host and TCP port to scan
host = "scanme.nmap.org"
port_range = 22
src_port = 22
dst_port = 22

response = sr1(IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=1,verbose=0)

print(response)