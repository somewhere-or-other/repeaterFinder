#!/usr/bin/python3

import csv
import io
import requests
import pyproj

import pprint


geodesic = pyproj.Geod(ellps='WGS84')

def processRepeaterList(url="https://utahvhfs.org/rptrraw.txt"):
    r = requests.get(url)
    buff = io.StringIO(r.text)
    dr = csv.DictReader(buff)
    for row in dr:
        processRepeater(row)


def processRepeater(repeaterRow=None):
    if repeaterRow==None:
        raise ValueError("No repeater definition found")
    
    #pprint.pprint(repeaterRow)

def getBearing(lat1, long1, elev1, lat2, long2, elev2):
    #TODO: figure out how to us pyproj to convert using epsg 4979 (3d), and NOT EPSG 4236 (2d); see https://gis.stackexchange.com/a/385738

if __name__=="__main__":
    processRepeaterList()
