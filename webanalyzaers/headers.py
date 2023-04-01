#!/usr/bin/env python
#_*_ conding: utf-8

import requests
import argparse

def main():
    parse = argparse.ArgumentParser(description="Grab target's headers")
    parse.add_argument('-t','--target',help="Define the url's target", required=True)
    args = parse.parse_args()

    try:
        res = requests.get(url=args.target)
        headers = dict(res.headers)
        for key,value in headers.items():
            print(key + " : " + value)
    except:
        print("Can't connect to target")

if __name__ == "__main__":
    main()