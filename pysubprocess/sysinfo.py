#!/usr/bin/env python
#* conding: utf-8

import subprocess as sbp

comout = sbp.check_output("systeminfo", stderr=sbp.STDOUT)

with open("../info.txt", "w+") as fd:
    fd.write(comout.decode('utf-8'))
