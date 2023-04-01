#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from shodan import Shodan

KEY = 'AUGo52J5sKJsdQ2MIUl6IirIaSjUxm8Z'


def main():
    s_engine = Shodan(KEY)
    try:
        res = s_engine.host("72.167.226.7")
        print("IP: {}".format(res['ip']))
        print("Ports: {}".format(res['ports']))
        print("ORG: {}".format(res['org']))
        print("TAGS: {}".format(res['tags']))
        try:
            print("ASN: {}".format(res['asn']))
        except AttributeError:
            print("No ASN")
        for elem in res['data']:
            elem_list = elem.keys()
            for el in elem_list:
                print(str(elem[el]))
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
