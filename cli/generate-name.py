#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""

import os
import sys
import getopt
from sqlalchemy import *

tables = {}
database = {}


def generate_name(gender):
    return "Bob"


def main(argv):

    # parse arguments
    dbname = 'writertoys'
    gender = 'any'
    global debug
    debug = False
    try:
        opts, args = getopt.getopt(argv, "hxg:d:", ["gender=", "dbname="])
    except getopt.GetoptError:
        print 'generate-name.py [-x] -g <gender> -d <dbname>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'generate-name.py [-x] -g <gender> -d <dbname>'
            sys.exit()
        elif opt == '-x':
            debug = True
        elif opt in ("-g", "--gender"):
            gender = arg
        elif opt in ("-d", "--dbname"):
            dbname = arg
    if debug:
        print('DEBUG: Gender is {}'.format(gender))
        print('DEBUG: Name database is {}'.format(dbname))

    # open the database
    global database
    # todo: allow non-local database
    # todo: handle any database errors
    database['engine'] = engine = create_engine(
        'postgresql://@localhost/' + dbname)
    database['conn'] = conn = engine.connect()
    database['metadata'] = metadata = MetaData()
    """
    Load the table definitions from the database using reflection
    """
    global tables
    tables['rawnames'] = Table(
        'rawnames', metadata, autoload=True, autoload_with=engine)
    tables['nametypes'] = Table(
        'nametypes', metadata, autoload=True, autoload_with=engine)
    tables['namegenders'] = Table(
        'namegenders', metadata, autoload=True, autoload_with=engine)
    tables['nameorigins'] = Table(
        'nameorigins', metadata, autoload=True, autoload_with=engine)
    tables['names'] = Table(
        'names', metadata, autoload=True, autoload_with=engine)
    if debug:
        import pdb; pdb.set_trace()

    name = generate_name(gender)
    print(name)

if __name__ == "__main__":
    main(sys.argv[1:])
