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

# ignore collisions / duplicates
def get_random_numbers(num, minval, maxval):
    random.seed() # initialize with system time
    randnums = []
    for i in range(num):
        randnums.append(random.randint(minval, maxval))
    return randnums


"""
 1. count the number of records in the names table
 2. choose N (e.g. 25) random integers between 1 and Count
 3. select rows that have the right gender and type that are in the list of random numbers

 OK, this isn't working, and it's a bad idea anyway, even when I figure out the SQL issue. The
 results, when it returns anything, are like:
 DEBUG: names list is [(u'Paulita',), (u'Paulita',), (u'Paulita',), (u'Romaine',), (u'Romaine',), (u'Romaine',)]
"""
def method1(gender, nametype):
    name = None
    names = None
    rnametable = tables['rawnames']
    nametable = tables['names']
    nametypetable = tables['nametypes']
    count_em = select([func.count()]).select_from(nametable)
    rows = database['conn'].execute(count_em)
    value = rows.fetchone()[0]
    print('DEBUG: Number of rawnames is {}'.format(value))
    randids = get_random_numbers(25, 1, value)
    print('DEBUG: Random ID array is {}'.format(randids))
    idlist = str(randids).strip('[]')
    if gender is 'any':
        s = text( "select rawnames.name from names, namegenders, nametypes, rawnames where "
          "rawnames.id = names.rawnames_id "
          "and names.nametypes_id = nametypes.id "
          "and nametypes.type = :nt "
          "and rawnames.id in (" + idlist + ")")
        # I can't figure out how to use bindparams with the array of ints
        # which is why they're embedded in the string like this. I'm going to have
        # to redo this anyway, and rethink the schema. Databases aren't intended for
        # random selection this way.
        names = database['conn'].execute(s, nt=nametype).fetchall()
    # todo: need an else
    print('DEBUG: names list is {}'.format(names))
    if names is not None and len(names) > 0:
        name = names[0][0]
    return name
"""
 4. select all rows of the right gender and type into an array
 5. pick a random array element
"""
def method2(gender, nametype):
    return 'Bob'

def generate_name(gender, nametype):
    name = method1(gender, nametype)
    if name == None:
        name = method2(gender, nametype)
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

    name = generate_name(gender, 'first')
    print(name)

if __name__ == "__main__":
    main(sys.argv[1:])
