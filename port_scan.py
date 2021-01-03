#!/usr/bin/python3

import socket, sys
from termcolor import colored

host = input("Please enter target IP address: ")

try:
	for port in range(1,65536):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		r = s.connect_ex((host, port))
		if r == 0:
			print(colored("[+] Port %s is open!" % str(port), "green"))
		s.close()
	else:
	    	print(colored("[*] Scan complete!", "green"))
except socket.error:
	print(colored("[-] Could not connect to the server!", "red"))
	sys.exit(0)
except KeyboardInterrupt:
	print(colored("[-] Scanning cancelled!", "red"))
	sys.exit(0)
