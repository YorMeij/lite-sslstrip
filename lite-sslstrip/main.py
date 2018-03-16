# TODO horrible intro ASCII art
import argparse

# Commandline arguments for ARP-spoofing
parser = argparse.ArgumentParser()
parser.add_argument('macA', help="MAC address of Alice")
parser.add_argument('ipA', help="IP address of Alice")
parser.add_argument('macB', help="MAC address of Bob")
parser.add_argument('ipB', help="IP address of Bob")

# IDEA get this from the machine itself
parser.add_argument('macM', help="MAC address of you (Mallory)")
parser.add_argument('ipM', help="IP address of you (Mallory)")

args = parser.parse_args()
print args.macA

# TODO Launch ARP attack


# TODO include parameters for SSL stripping