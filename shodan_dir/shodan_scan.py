#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from shodan import Shodan

KEY = 'AUGo52J5sKJsdQ2MIUl6IirIaSjUxm8Z'


def main():
    s_engine = Shodan(KEY)
    try:
        res = s_engine.search("struts")
        print("Total: {}".format(res['total']))
        for match in res['matches']:
            print("IP: {}".format(match['ip']))
            print("Port: {}".format(match['port']))
            print("ORG: {}".format(match['org']))
            print("TAGS: {}".format(match['tags']))
            try:
                print("ASN: {}".format(match['asn']))
            finally:
                print("No ASN")
            for loc in match['location']:
                print("{}: {}".format(loc, match['location'][loc]))
            print("---------------------------------------------")
    except ConnectionError:
        print('Something went wrong')


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting the program")
        exit()
    except ConnectionError:
        print('Something went wrong')
