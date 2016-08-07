#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
(1) open and read hard-coded csv files for male, female first names
(2) open and read hard-coded csv files for surnames
(3) insert the data into a postgres database named writertoys
"""

import os
import sys
import getopt
from sqlalchemy import *
import csv
database = {}


def loadcsv(filename, namegender, nametype):
    conn = database['conn']
   # todo: see if all the csv files have the same structure?
   # todo: finish this
    with open(filename, 'rb') as csvfile:
        namereader = csv.reader(csvfile, delimiter=',')
        for row in namereader:
             print ', '.join(row)

def main(argv):
   global database
   database['engine'] = engine = create_engine('postgresql://localhost/writertoys')
   database['conn'] = conn = engine.connect()
   database['metadata'] = metadata = MetaData()
   loadcsv('female_first_names.csv', 'female', 'first')
   loadcsv('male_first_names.csv', 'male', 'first')
   loadcsv('surnames.csv', 'either', 'last')

if __name__ == "__main__":
   main(sys.argv[1:])

