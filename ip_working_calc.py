#!/usr/bin/env python3

# Script to give IPv4 addresses based on user input.
# Outputs to include:
# 1) First, last, network, broadcast addresses
# 2) Number of usable addresses/networks based on CIDR input
# 3) Supernetting of multiple network ranges
# 4) GUI display of application

#print('{0} and {1}'.format('Geeks', 'Portal'))

# Notes

import ipaddress
import sys


#net4 = ipaddress.ip_network('192.168.0.0/24')

#print('\nThe network address is: {0}\nThe first available address is: {1}\nThe last available address is: {2}\nThe broadcast address is: {3}'.format(net4[0], net4[1], net4[-2], net4[-1]))

#print(net4.num_addresses)

#ipaddress.ip_network = input('Enter an IP Address: ')
#print(ipaddress.hosts())

# This code works and prints the first, last, network id, broadcast, and number of assignable addresses. Line 28 takes user input and assigns it to the "ip_interface" global variable. Line 27 indicates "strict=False"
# in case the user does not specify the correct subnet format. 

if len(sys.argv) != 2:
    print("\nUsage: ./ip_calc.py IP Address with CIDR\n\
        E.G. -> ./ip_calc.py 192.168.0.1/24\n")
else:
    print(len(sys.argv))
    user_int = sys.argv[1]
    #user_int = ipaddress.ip_interface(input('Enter an IP Address (192.168.0.0/24): '))
    user_addr = ipaddress.ip_network(user_int, strict=False)
    addr_netmask = user_addr.netmask
    if str(user_addr.netmask) == '255.255.255.255':
        print('\nThe only available IP Address is: {}'.format(user_addr[0]))
    else:
        #print('\nThe network address is: {:14}\n\
        #The first available address is: {}\n\
        #The last assignable address is: {}\n\
        #The broadcast address is: {}'.format(str(user_addr[0]), str(user_addr[1]), str(user_addr[-2]), str(user_addr[-1])))
        #assign_addresses = user_addr.num_addresses - 2
        #print(num_addresses)
        #print('The number of assignable addresses is: {}\n'.format(assign_addresses))
        net_addr = str(user_addr[0])
        first_addr = str(user_addr[1])
        last_addr = str(user_addr[-2])
        bcast_addr = str(user_addr[-1])
        assignable_address = user_addr.num_addresses - 2
        print('Network address is: {:>18}'.format(net_addr))
        print('First address is: {:>20}'.format(first_addr))
        print('Last address is: {:>23}'.format(last_addr))
        print('Broadcast address is: {:>18}'.format(bcast_addr))
        print('Number of assignable: {:>8} IP addresses'.format(assignable_address))


#ip1 = ipaddress.ip_network('192.168.0.0/24')
#print(ip1.netmask)

