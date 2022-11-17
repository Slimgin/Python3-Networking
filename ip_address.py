#! /usr/bin/env python3

# The original intent was to have this code always running, in a separate iTerm2 window with other information displayed. I am still working on that aspect and will post updated
# working code, at some point. That is the reason for the while loop - sleep command. If I connected to a different network or VPN, I wanted the code to update the new IP addresses.
# This can certainly be turned off without any loss of functionality. If you have any comments, like my code is garbage, feel free to hit me up on GitHub (https://github.com/Slimgin)
# or on Reddit (https://www.reddit.com/user/GilNims). 

from requests import get
import time

# ip_address function prints your machine's IPv4 and IPv6 address, provided they are unique. Since some ISP's have not started providing customer's with IPv6 addresses
# this script checks to see if the two addresses are the same.
def ip_address(addy1, addy2):
    if addy1 == addy2:
        print(' Your IPv4 public address is: ' + addy1, flush=True, end='\n')
    else:
        print(' Your IPv4 public address is: ' + addy1 + ' and your IPv6 public address is: ' + addy2, flush=True, end='\n')
    return

def main():
    address1 = get('https://api.ipify.org').text
    address2 = get('https://api64.ipify.org').text
    ip_address( address1, address2 )


if __name__ == "__main__":
    main()