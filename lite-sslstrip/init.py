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

    ## Helper block, to remind the user of actions that need performing
    print "Welcome to lite-sslstrip"

    if(os.geteuid() != 0):
        print "No root privileges, exiting"
        sys.exit()

    print "Enabeling ip_forwarding"
    f = open("/proc/sys/net/ipv4/ip_forward", "w")
    f.write("1")
    f.close()

    print "Reidirecting iptables"
    # reroutes incoming trafic on port 80 (http) to port 8080 (lite-ssl)
    os.system("iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8080")