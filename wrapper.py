#!/usr/bin/python 

import os
import sys
import time

def main():

    print "Scanning Options"
    print " 1. Fast Scan - Top 100 Ports"
    print " 2. Intense Scan + UDP"
    print " 3. Intense Scan - all TCP ports"
    print " 4. Normal Scan"
    print " 5. Custom"
    print " 6. ABORT ABORT ABORT"

    option = raw_input("Scanning Option : ")


    if option == '1':
        ip = raw_input("IP Address or Range : ")
        os.system("nmap -F "+ip)
        print "Scan Complete"
        main()

    elif option == '2':
        ip = raw_input("IP Address or Range : ")
        os.system("nmap -sS -sU -T4 -A -v "+ip)
        print "Scan Complete"
        main()

    elif option == '3':
        ip = raw_input("IP Address or Range : ")
        os.system("nmap -p 1-65535 -T4 -A -v "+ip)
        print "Scan Complete"
        main()

    elif option == '4':
        ip = raw_input("IP Address or Range : ")
        os.system("nmap "+ip)
        print "Scan Complete"
        main()

    elif option == '5':
        print "This custom option allows you to add all native nmap functionality, just add options/scripts and target IPs"
        ip = raw_input(" Options/script + Target IP  ")
        os.system("nmap "+ip)
        print "Scan Complete"
        main()

    elif option == '6':
        print "THROW EVERYTHING IN THE MICROWAVE AND LETS GET THE HELL OUT OF HERE!"
        time.sleep(5)
        sys.exit()

    else:
        main()

if __name__ == "__main__":
    try:
        main()
        
    except KeyboardInterrupt: 
        print "You know, you could have just aborted.. why have functionality if not to use it? Now you wait."
        time.sleep(30)
        pass


        
