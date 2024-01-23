#!/usr/bin/python3
from scapy.all import *
print("CMPE209-Assignment1-016707314-Task1.2B-Spoofing packets from non-existing (random) IPs");
print ("Sending Spoofed ICMP Packet...")
IP = IP()
IP.src="10.9.0.18"
IP.dst="10.9.0.26"
ICMP = ICMP()
pkt = IP/ICMP
pkt. show()
send(pkt,verbose=0)

