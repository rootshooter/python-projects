#!/usr/bin/python3

import socket
from termcolor import colored

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input("Please enter target IP address: ")

for port in range(1,65536):
	try:
		s.connect((host, port))
		s.close()
		print(colored("[+] Port %s is open!" % str(port), "green"))
	except:
		continue
