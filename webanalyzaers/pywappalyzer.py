#!/usr/bin/env python
#_*_ conding: utf-8

import argparse
from Wappalyzer import WebPage, Wappalyzer
import warnings

def analyzer(url):
    wap = Wappalyzer.latest()
    try:
        web = WebPage.new_from_url(url)
        techs = wap.analyze(web)
        print("Web page technologies: ")
        for tech in techs:
            print(" - " + tech)
    except:
        print("Can't connect to the target")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url',help="URL option", dest='url',required=True)
    args = parser.parse_args()

    analyzer(args.url)

if __name__ == "__main__":
    warnings.filterwarnings(action='ignore')
    main()