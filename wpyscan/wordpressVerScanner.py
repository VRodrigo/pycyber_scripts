#!/usr/bin/env python
#_*_ conding: utf-8

import requests
from bs4 import BeautifulSoup
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url',help="URL option", dest='url',required=True)
    args = parser.parse_args()

    try:
        req_headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'}
        res = requests.get(url=args.url, headers=req_headers)

        web_html = BeautifulSoup(res.text, 'html5lib')
        for meta in web_html.find_all('meta'):
            if meta.get('name') == 'generator':
                print(meta.get('content'))
    except:
        "Can't connect to the url"

if __name__ == '__main__':
    main()