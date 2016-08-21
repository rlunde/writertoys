#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 1. count the number of records in the names table
 2. choose N (e.g. 25) random integers between 1 and Count
 3. select rows that have the right gender and type that are in the list of random numbers
 4. if none, select all rows of the right gender and type into an array
 5. pick a random array element
"""

import os
import sys
import getopt
import random
from sqlalchemy import *
from sqlalchemy.sql import text

tables = {}
database = {}

"""
 1. select all rows of the right gender and type into an array
 2. pick a random array element

 Notes:
   a) this is SUPER expensive. For an API, we'll want to load the arrays in memory
      by name type and gender the first time they're used, and cache them
   b) last names don't have gender (I think?) so should refactor into get_first_name
      and get_last_name
"""
def generate_name(gender, nametype):
    name = None
    names = None
    random.seed() # initialize with system time
    if gender is 'any':
        s = text( "select rawnames.name from names, nametypes, rawnames where "
          "rawnames.id = names.rawnames_id "
          "and names.nametypes_id = nametypes.id "
          "and nametypes.type = :nt ")
        names = database['conn'].execute(s, nt=nametype).fetchall()
    else:
        s = text( "select rawnames.name from names, nametypes, namegenders, rawnames where "
          "rawnames.id = names.rawnames_id "
          "and names.nametypes_id = nametypes.id "
          "and nametypes.type = :nt "
          "and namegenders.type = :ng ")
        names = database['conn'].execute(s, nt=nametype, ng=gender).fetchall()
    if debug:
        print('DEBUG: names list is {}'.format(names))
    if names is not None and len(names) > 0:
        name = random.choice(names)[0]
    return name

def main(argv):

    # parse arguments
    dbname = 'writertoys'
    gender = 'any'
    global debug
    debug = False
    try:
        opts, args = getopt.getopt(argv, "hxg:d:", ["gender=", "dbname="])
    except getopt.GetoptError:
        print('generate-name.py [-x] -g <gender> -d <dbname>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('generate-name.py [-x] -g <gender> -d <dbname>')
            sys.exit()
        elif opt == '-x':
            debug = True
        elif opt in ("-g", "--gender"):
            gender = arg
        elif opt in ("-d", "--dbname"):
            dbname = arg
    if debug is True:
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

    first_name = generate_name(gender, 'first')
    last_name = generate_name(gender, 'last')
    print('{} {}'.format(first_name, last_name))

if __name__ == "__main__":
    main(sys.argv[1:])
