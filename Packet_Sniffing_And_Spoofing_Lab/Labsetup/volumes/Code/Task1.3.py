#!/usr/bin/python3
from scapy.all import *
'''Usage:  ./traceroute.py " hostname or ip address"'''
host=sys.argv[1]
print("CMPE209-Assignment1-016707314-Task1.3-Tracing the route");
print ("Traceroute for "+ host)
ttl=1
while 1:
    IPObj=IP ()
    IPObj.dst=host
    IPObj.ttl=ttl
    ICMPobj=ICMP()
    pkt=IPObj/ICMPobj
    reply = sr1(pkt,verbose=0)
    if reply is None:
        break
    elif reply [ICMP].type==0:
        print(f"{ttl} hop(s) away: ", reply [IP].src)
        print( "Done...Packet reached destination", reply [IP].src)
        break
    else:
        print (f"{ttl} hop(s) away: ", reply [IP].src)
        ttl+=1
