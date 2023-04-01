#!/usr/bin/env python
#_*_ conding: utf-8

import requests
import argparse

def cloudflare_detect(url):
    word = "cloudflare"
    verify = False
    try:
        res = requests.get(url=url)
        headers = dict(res.headers)
        for h in headers:
            if word in headers[h].lower():
                verify = True
                break
        if verify:
            print('Cloudflare present')
        else:
            print('Cloudflare not present')
    except:
        print("Can't connect to target")


def main():
    parse = argparse.ArgumentParser(description="Grab target's headers")
    parse.add_argument('-u','--url',help="Define the url's target",dest="url", required=True)
    args = parse.parse_args()

    cloudflare_detect(args.url)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()