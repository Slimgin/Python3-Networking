#!/usr/bin/env python3

import ipaddress

# This code works and prints the first, last, network id, broadcast, and number of assignable addresses. Line 7 takes user input and assigns it to the "ip_interface" global variable. Line 27 indicates "strict=False"
# in case the user does not specify the correct subnet format. 
user_int = ipaddress.ip_interface(input('Enter an IP Address (192.168.0.0/24): '))
user_addr = ipaddress.ip_network(user_int, strict=False)
print('\nThe network address is: {}\nThe first available address is: {}\nThe last assignable address is: {}\nThe broadcast address is: {}'.format(user_addr[0], user_addr[1], user_addr[-2], user_addr[-1]))
assign_addresses = user_addr.num_addresses - 2
#print(num_addresses)
print('The number of assignable addresses is: {}\n'.format(assign_addresses))