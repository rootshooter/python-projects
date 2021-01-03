This is a collection of projects I developed using Python/Python3. I am not an expert, so please ignore the ugly code.


getting_started.py is a tool that I created to automate some of the redundant tasks that come along with working through machines on TryHackMe and HackTheBox.
This scripts makes a directory, makes a nmap dirctory within that directory, and then runs a nmap scan with the flags -T3 -Pn -sC -sV -p- -oN set. It outputs the results from the scan to whatever_dir/nmap in the .nmap format. 

Usage: ./getting_started.py -n hackpark -t 10.10.10.1

port_scan_simple.py is a simple port scanner that accepts an IP address and a port as arguments. It will check to see whether the port is open or not and report it's status.

Usage: ./port_scan_simple.py

port_scan.py is a more advanced port scanner that accepts an IP address as an argument. It will scan ports 1-65535 and report open ports.

Usage: ./port_scan.py

