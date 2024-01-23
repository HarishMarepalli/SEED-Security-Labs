#!/usr/bin/python3
from scapy.all import *
print("CMPE209-Assignment1-016707314-Task1.2A-Spoofing packets from existing IPs");
print ("Sending Spoofed ICMP Packet...")
IP = IP()
IP.src="10.9.0.1"	#Attacker's IP Address
IP.dst="10.9.0.5"	#Host A's IP Address
ICMP = ICMP()
pkt = IP/ICMP		#Create a packet
pkt. show ()
send(pkt,verbose=0)	#Send the packet
