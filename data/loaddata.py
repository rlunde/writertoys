#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
(1) open and read hard-coded files for male, female first names
(2) open and read hard-coded files for surnames
(3) insert the data into a postgres database named writertoys
"""

import os
import sys
import getopt
from sqlalchemy import *
database = {}


# create the nametype if it doesn't exist, and return the ID
def getNameType(nametype):
    conn = database['conn']
    m = database['metadata']
    nameTypesTable = Table('NameTypes', metadata, autoload=True, autoload_with=engine)
    # TODO: finish this

# create the namegender if it doesn't exist, and return the ID
def getNameGender(namegender):
    conn = database['conn']
    m = database['metadata']
    nameGendersTable = Table('NameGenders', metadata, autoload=True, autoload_with=engine)
    # TODO: finish this

# create the nameorigin if it doesn't exist, and return the ID
def getNameOrigin(nameorigin):
    conn = database['conn']
    m = database['metadata']
    nameOriginsTable = Table('NameOrigins', metadata, autoload=True, autoload_with=engine)
    # TODO: finish this


def loadlist(filename, namegender, nametype):
    conn = database['conn']
    m = database['metadata']
    nameTypesId = getNameType(nametype)
    nameGendersId = getNameGender(namegender)
    nameOriginsId = getNameOrigin('any')

    rawNamesTable = Table('RawNames', metadata, autoload=True, autoload_with=engine)
    namesTable = Table('Names', metadata, autoload=True, autoload_with=engine)
    # note: the name data has already been extracted into just a list; it's not a csv
    with open(filename, 'rb') as listfile:
        for name in listfile:
            # TODO: finish this

def main(argv):
   global database
   database['engine'] = engine = create_engine('postgresql://localhost/writertoys')
   database['conn'] = conn = engine.connect()
   database['metadata'] = metadata = MetaData()
   loadlist('female_first_names.txt', 'female', 'first')
   loadlist('male_first_names.txt', 'male', 'first')
   loadlist('surnames.txt', 'either', 'last')

if __name__ == "__main__":
   main(sys.argv[1:])

