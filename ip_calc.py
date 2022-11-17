#!/usr/bin/env python3

import ipaddress
import sys

if len(sys.argv) != 2:
    print("\nUsage: ./ip_calc.py IP Address with CIDR\n\
        E.G. -> ./ip_calc.py 192.168.0.1/24\n")
else:
    user_int = sys.argv[1]
    user_addr = ipaddress.ip_network(user_int, strict=False)
    addr_netmask = user_addr.netmask
    if str(user_addr.netmask) == '255.255.255.255':
        print('\nThe only available IP Address is: {}'.format(user_addr[0]))
    else:
        net_addr = str(user_addr[0])
        first_addr = str(user_addr[1])
        last_addr = str(user_addr[-2])
        bcast_addr = str(user_addr[-1])
        assignable_address = user_addr.num_addresses - 2
        print('\nNetwork address is: {:>18}'.format(net_addr))
        print('First address is: {:>20}'.format(first_addr))
        print('Last address is: {:>23}'.format(last_addr))
        print('Broadcast address is: {:>18}'.format(bcast_addr))
        print('Number of assignable: {:>8} IP addresses'.format(assignable_address))