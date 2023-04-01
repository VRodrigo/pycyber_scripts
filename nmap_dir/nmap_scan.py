#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import nmap
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-h', '--host', help="Address option", dest='host', required=True)
    args = parser.parse_args()

    if args.host:
        nm = nmap.PortScanner()
        nm.scan(hosts=args.host, arguments="--top-ports 1000 -sV --version-intensity 3")
        print("CMD: {}".format(nm.command_line()))
        print("Protocols: {}".format(nm[args.host].all_protocols()))
        print("Host status: {}".format(nm[args.host].state()))
        for service in nm[args.host]['tcp'].keys():
            print(service)
            for data in nm[args.host]['tcp'][service]:
                print("{}: {}".format(data, nm[args.host]['tcp'][service][data]))
    else:
        print("Please input a host")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting the program")
        exit()
