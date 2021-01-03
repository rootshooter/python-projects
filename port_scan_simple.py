#!/usr/bin/python3

import socket
from termcolor import colored

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input("Please enter an IP address: ")
port = int(input("Please enter a port: "))

try:
	s.connect((host, port))
	s.close()
	print(colored("[+] Port %s is open!" % str(port), "green"))
except:
	print(colored("[-] Port %s is closed!" % str(port), "red"))
