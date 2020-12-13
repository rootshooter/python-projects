#!/usr/bin/python3
import os, sys, optparse
from time import sleep

parser = optparse.OptionParser('Example: python getting_started.py -n <directory name> -t <target address>')
parser.add_option('-n', dest='dir_name', type='string', help='Enter directory name')
parser.add_option('-t', dest='target', type='string', help='Enter target address')
(options, args) = parser.parse_args()
dir_name = options.dir_name
target = options.target


if (dir_name == None) | (target == None):
	print(parser.usage)
	exit(0)




try:
    os.system('mkdir '+dir_name)
    os.system('mkdir '+dir_name+'/nmap')
    print('\n[+] Running Nmap scan now')
    print('[**] This could take a while')
    os.system('nmap -T3 -Pn -sC -sV -p- -oN '+dir_name+'/nmap/'+dir_name+'.nmap' + ' ' +target +'>/dev/null')
    print('[+] Check for results under '+dir_name+'/nmap \n')

except:
	print('[-] Error! Something went wrong')
