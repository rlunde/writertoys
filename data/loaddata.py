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

'''
Load a file of the specified gender (female,male,any) and type (first,last).
Hardcode the origin to 'any' for now.
'''
def loadlist(filename, namegender, nametype):
    conn = database['conn']
    m = database['metadata']
    engine = database['engine']

    #import pdb; pdb.set_trace()
    namesTable = Table('names', m, autoload=True, autoload_with=engine)
    # note: the name data has already been extracted into just a list; it's
    # not a csv
    with open(filename, 'rb') as listfile:
        for rawname in listfile:
            rawname = rawname.strip()
            # the first time this is run, there should be no collisions, so
            # it might be more efficient to just try to insert it and catch errors
            s = select([namesTable]).where(and_(
                (namesTable.c.name == rawname),
                (namesTable.c.type == nametype),
                (namesTable.c.gender == namegender),
                (namesTable.c.origin == 'any')
                )
            )
            #print s
            rows = conn.execute(s)
            id = None
            if rows.rowcount == 0:
                ins = namesTable.insert()
                rows = conn.execute(ins, name=rawname,
                                    type=nametype,
                                    gender=namegender,
                                    origin='any')
                id = rows.inserted_primary_key[0]
    return 0


def main(argv):
    global database
    database['engine'] = engine = create_engine(
        'postgresql://localhost/writertoys')
    database['conn'] = conn = engine.connect()
    database['metadata'] = m = MetaData()
    loadlist('female_first_names.txt', 'female', 'first')
    loadlist('male_first_names.txt', 'male', 'first')
    loadlist('surnames.txt', 'either', 'last')

if __name__ == "__main__":
    main(sys.argv[1:])
