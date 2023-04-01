#!/usr/bin/env python
#_*_ conding: utf-8

import requests
import argparse
from os import path

URL = "<Write a URL>"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file',help="Select the file that will be upload", required=True)
    args = parser.parse_args()

    if path.exists(args.file):
        fd = open(args.file,"rb")
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'}
        post_pet = requests.post(url=URL, files={'file': fd}, headers=headers)
        if args.file in post_pet.text:
            print("File seccessfully uploaded")
        else:
            print("Can't upload the file")
    else:
        print("no exixte el archivo")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting the program")
        exit()
