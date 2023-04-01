#!/usr/bin/env python
#_*_ conding: utf-8

import requests
from os import path
import argparse
from progress.bar import Bar

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url',help="URL option", dest='url',required=True)
    args = parser.parse_args()
    if not args.url.endswith('/'):
        args.url = args.url + '/'

    try:
        if path.exists("wp_plugins.txt"):
            fd = open("wp_plugins.txt", "r")
            plg_list = fd.read().split("\n")
            fnd_plg_list = []
            b = Bar("Wait...", max=len(plg_list))
            for plugin in plg_list:
                b.next()
                try:
                    res = requests.get(args.url + plugin)
                    if res.status_code == 200:
                        fnd_plg_list.append(plugin.split('/')[-2])
                except:
                    pass
            b.finish()
            print('Founded plugins:\n')
            for plugin in fnd_plg_list:
                print(plugin, end='\n')
        else:
            print("Couldn't find file wp_plugins.txt, that contain plugins' list")
    except:
        print('unknow error, ensure url is well written')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
