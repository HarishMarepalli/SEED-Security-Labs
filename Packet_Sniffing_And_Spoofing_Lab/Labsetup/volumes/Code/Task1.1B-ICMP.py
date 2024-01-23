#! / usr/bin/python3
from scapy.all import *
print("CMPE209-Assignment1-016707314-Task1.1B-Filtering the ICMP packets");
print("Sniffing Packets...");
def print_pkt(pkt):
    pkt.show()
pkt = sniff (iface = "br-62f4ebf4c30a",filter='icmp', prn=print_pkt)
