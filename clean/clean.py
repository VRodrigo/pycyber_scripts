#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import csv

write_csv=[]

with open('policy_rules.csv', 'r') as fd:
    lines = csv.DictReader(fd, delimiter=';')

    for line in lines:
        if line["Type"].lower() != 'section':
            if 'Disabled' not in line["Type"]:
                Hits = ''
                if line["Hits"].lower() == 'zero':
                    Hits = '0'
                else:
                    Hits = ((str(line["Hits"]).split('=')[1]).split(')')[0]).strip()
                dict_csv = {
                    "No.": line["No."],
                    "Name": line["Name"],
                    "Hits": Hits,
                    "Source": line["Source"],
                    "Destination": line["Destination"],
                    "Services": line["Services & Applications"],
                    "Action": line["Action"]
                }
                write_csv.append(dict_csv)

#print(write_csv)

with open('policy_rules_clean.csv', mode='w') as csv_file:
    fieldnames = ["No.", "Name", "Hits", "Source", "Destination", "Services", "Action"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for line in write_csv:
        writer.writerow(line)
