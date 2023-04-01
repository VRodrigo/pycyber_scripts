#!/usr/bin/env python
#_*_ conding: utf-8

import dns.resolver as dresolver
import argparse
from os import path

def dnsResolver(args, subdlist):
    found_sub = []
    for sub in subdlist:
        try:
            res = dresolver.resolve("{}.{}".format(sub, args.domain), "A")
            found_sub.append("{}.{}".format(sub, args.domain))
        except:
            pass
    return found_sub


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--domain',help="Domain option", dest='domain',required=True)
    parser.add_argument('-l', '--list',help="Domain option", dest='list',required=True)
    args = parser.parse_args()

    if path.exists(args.list):
        subdlist = open(args.list).read().split("\n")
        for name in dnsResolver(args, subdlist):
            print(name)
    else:
        print("Subdomain list dosen't exist")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()