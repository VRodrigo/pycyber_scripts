#!/usr/bin/env python
#_*_ conding: utf-8

import requests
import json
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url',help="URL option", dest='url',required=True)
    args = parser.parse_args()
    if not args.url.endswith('/'):
        args.url = args.url + '/'

    try:
        res = requests.get(args.url + 'wp-json/wp/v2/users')
        user_lst = json.loads(res.text())
        print('Users found:')
        for user in user_lst:
            print(user["slug"])
    except:
        pass

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()