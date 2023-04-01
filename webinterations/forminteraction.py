#!/usr/bin/env python
#_*_ conding: utf-8

from http.client import ImproperConnectionState
import mechanize
import argparse
from bs4 import BeautifulSoup

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--browse',help="Browse option", dest='browse',required=True)
    args = parser.parse_args()

    brow = mechanize.Browser()
    brow.set_handle_equiv(False)
    brow.set_handle_robots(False)
    brow.addheaders = [('User-Agent', 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0')]
    brow.open('https://www.google.com/')

    forms = brow.select_form(nr=0)
    brow['q'] = args.browse
    brow.submit()
    res = BeautifulSoup(brow.response().read(), 'html5lib')
    for link in res.find_all('a'):
        if link.get('href') is not None and 'http' in link.get('href'):
            try:
                print(link.get('href').split('q=')[1])
            except IndexError:
                print(link.get('href'))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting the program")
        exit()