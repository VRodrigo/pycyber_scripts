#!/usr/bin/env python
#_*_ conding: utf-8

import requests
import argparse
import json

def geolocator(args):
    res = requests.get("https://ipinfo.io/{}/json".format(args.address))
    ip_info = json.loads(res.text)
    for key, value in ip_info.items():
        print("{}: {}".format(key, value))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--address',help="IP address option", dest='address',required=True)
    args = parser.parse_args()

    geolocator(args)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()