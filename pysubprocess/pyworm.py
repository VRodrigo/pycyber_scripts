#!/usr/bin/env python
#_*_ conding: utf-8

import shutil
import argparse
from datetime import datetime
import time


def main():
    parse = argparse.ArgumentParser(description="WORM")
    parse.add_argument('-c', '--count', help="Number of duplicates", required=True)
    args = parse.parse_args()
    for n in range(0, int(args.count)):
        dtraw = datetime.now()
        dtform = dtraw.strftime("%Y%m%d%H%M%S")
        shutil.copy(parse.prog, parse.prog + dtform + ".py")
        time.sleep(1)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
