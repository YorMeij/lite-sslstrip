"""
Initiates the Lite-SSLstrip tool, sets up the enviroment by enabeling ip_forwarding, checks wehter we are root and
sets up the IPtables to do the routing.
"""

import os
import sys

def init():
    print ""
    print ""
    print " __          __                                            __              __                __           "
    print "/  |        /  |                                          /  |            /  |              /  |          "
    print "$$ |       _$$ |_     ______            _______   _______ $$ |  _______  _$$ |_     ______  $$/   ______  "
    print "$$ |      / $$   |   /      \  ______  /       | /       |$$ | /       |/ $$   |   /      \ /  | /      \ "
    print "$$ |      $$$$$$/   /$$$$$$  |/      |/$$$$$$$/ /$$$$$$$/ $$ |/$$$$$$$/ $$$$$$/   /$$$$$$  |$$ |/$$$$$$  |"
    print "$$ |        $$ | __ $$    $$ |$$$$$$/ $$      \ $$      \ $$ |$$      \   $$ | __ $$ |  $$/ $$ |$$ |  $$ |"
    print "$$ |_____   $$ |/  |$$$$$$$$/          $$$$$$  | $$$$$$  |$$ | $$$$$$  |  $$ |/  |$$ |      $$ |$$ |__$$ |"
    print "$$       |  $$  $$/ $$       |        /     $$/ /     $$/ $$ |/     $$/   $$  $$/ $$ |      $$ |$$    $$/ "
    print "$$$$$$$$/    $$$$/   $$$$$$$/         $$$$$$$/  $$$$$$$/  $$/ $$$$$$$/     $$$$/  $$/       $$/ $$$$$$$/  "
    print "                                                                                                $$ |      "
    print "                                                                                                $$ |      "
    print "                                                                                                $$/   "
    print ""
    print ""

    print "Welcome to lite-sslstrip"

    # Check for root privilages
    if(os.geteuid() != 0):
        print "No root privileges, exiting"
        sys.exit()

    print "Enabeling ip_forwarding"
    f = open("/proc/sys/net/ipv4/ip_forward", "w")
    f.write("1")
    f.close()

    print "Reidirecting iptables"
    # Reroutes incoming trafic on port 80 (http) to port 8080 (lite-ssl)
    os.system("iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8080")