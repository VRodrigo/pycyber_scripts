#!/usr/bin/env python
# _*_ coding: utf-8

import socket
import argparse


def main():
    parse = argparse.ArgumentParser(description="Grab target's headers")
    parse.add_argument('-t', '--target', help="Define the target", dest="target", required=True)
    parse.add_argument('-p', '--port', help="Define the port's target", dest="port", required=True)
    args = parse.parse_args()

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((args.target, int(args.port)))
            banner = s.recv(1024)
            print(banner.decode('utf-8'))
    except:
        print('error en la conexion')


if __name__ == '__main__':
    try:

        main()
    except KeyboardInterrupt:
        exit()