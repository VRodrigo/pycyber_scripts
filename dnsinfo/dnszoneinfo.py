#!/usr/bin/env python
#_*_ conding: utf-8

import dns.resolver as dresolver
import argparse

def dns_reverse_resolve(args):
    try:
        res = dresolver.resolve_address(args.address)
        for adr in res:
            print("Domain: " + str(adr))

    except:
        print("Query couldn't get resolved")

def dns_resolver(args):
    try:
        res = dresolver.resolve(args.address, args.type)
        print("Query name: " + str(res.qname))
        for adr in res:
            print("Adrdess: " + str(adr))
        print("Canonical name: " + str(res.canonical_name))
    except:
        print("Query couldn't get resolved")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--address',help="Address option", dest='address',required=True)
    parser.add_argument('-t', '--type',help="Query type option", dest='type',default="a")
    parser.add_argument('-r',help="Rverse resolve", dest='reverse', action='store_true')
    args = parser.parse_args()

    if args.reverse:
        dns_reverse_resolve(args)
    else:
        dns_resolver(args)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()