#!/usr/bin/python3
from scapy.all import *
print("CMPE209-Assignment1-016707314-Task1.1B-Filtering the TCP packets with some src IP and destination port 23");
print("Sniffing Packets...");
def print_pkt(pkt):
    pkt.show()
pkt = sniff (iface = "br-62f4ebf4c30a",filter='tcp and src host 10.9.0.5 and dst port 23', prn=print_pkt)

