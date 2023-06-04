#!/usr/bin/python3

import csv
import io
import requests
import pprint


def processRepeaterList(url="https://utahvhfs.org/rptrraw.txt"):
    r = requests.get(url)
    buff = io.StringIO(r.text)
    dr = csv.DictReader(buff)
    for row in dr:
        processRepeater(row)


def processRepeater(repeaterRow=None):
    if repeaterRow==None:
        raise ValueError("No repeater definition found")
    
    pprint.pprint(repeaterRow)

if __name__=="__main__":
    processRepeaterList()
