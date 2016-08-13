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
from pprint import pprint
# for debugging, try
# pprint(someVar)
database = {}


# create the nametype if it doesn't exist, and return the ID
# this will only be called a handful of times, so it doesn't need to be
# very efficient
def getNameType(nametype):
    conn = database['conn']
    m = database['metadata']
    engine = database['engine']
    nameTypesTable = Table('nametypes', m, autoload=True, autoload_with=engine)
    s = select([nameTypesTable.c.id]).where(nameTypesTable.c.type == nametype)
    rows = conn.execute(s)
    id = None
    if rows.rowcount == 0:
        ins = nameTypesTable.insert()
        rows = conn.execute(ins, type=nametype)
        id = rows.inserted_primary_key[0]
    else:
        row = rows.fetchone()
        id = row['id']
    return id

# create the namegender if it doesn't exist, and return the ID
# this will only be called a handful of times, so it doesn't need to be
# very efficient


def getNameGender(namegender):
    conn = database['conn']
    m = database['metadata']
    engine = database['engine']
    nameGendersTable = Table(
        'namegenders', m, autoload=True, autoload_with=engine)
    s = select([nameGendersTable.c.id]).where(
        nameGendersTable.c.type == namegender)
    rows = conn.execute(s)
    id = None
    if rows.rowcount == 0:
        ins = nameGendersTable.insert()
        rows = conn.execute(ins, type=namegender)
        id = rows.inserted_primary_key[0]
    else:
        row = rows.fetchone()
        id = row['id']
    return id

# create the nameorigin if it doesn't exist, and return the ID
# this will only be called a handful of times, so it doesn't need to be
# very efficient


def getNameOrigin(nameorigin):
    conn = database['conn']
    m = database['metadata']
    engine = database['engine']
    nameOriginsTable = Table(
        'nameorigins', m, autoload=True, autoload_with=engine)
    s = select([nameOriginsTable.c.id]).where(
        nameOriginsTable.c.name == nameorigin)
    rows = conn.execute(s)
    id = None
    if rows.rowcount == 0:
        ins = nameOriginsTable.insert()
        rows = conn.execute(ins, name=nameorigin)
        id = rows.inserted_primary_key[0]
    else:
        row = rows.fetchone()
        id = row['id']
    return id


def getRawNameId(rawname):
    conn = database['conn']
    m = database['metadata']
    engine = database['engine']
    rawNamesTable = Table('rawnames', m, autoload=True, autoload_with=engine)
    s = select([rawNamesTable.c.id]).where(rawNamesTable.c.name == rawname)
    rows = conn.execute(s)
    id = None
    if rows.rowcount == 0:
        ins = rawNamesTable.insert()
        rows = conn.execute(ins, name=rawname)
        id = rows.inserted_primary_key[0]
    else:
        row = rows.fetchone()
        id = row['id']
    return id

# this is not very efficient, since we should do an insert if not exists in SQLAlchemy/Postgres,
# rather than look for it here, and insert if not found. Still, we'll do it this way, since
# this is a one-time load rather than an API handler.


def loadlist(filename, namegender, nametype):
    conn = database['conn']
    m = database['metadata']
    engine = database['engine']
    nameTypesId = getNameType(nametype)
    nameGendersId = getNameGender(namegender)
    nameOriginsId = getNameOrigin('any')

    # import pdb; pdb.set_trace()
    namesTable = Table('names', m, autoload=True, autoload_with=engine)
    # note: the name data has already been extracted into just a list; it's
    # not a csv
    with open(filename, 'rb') as listfile:
        for rawname in listfile:
            rawname = rawname.strip()
            rawNameId = getRawNameId(rawname)
            s = select([namesTable.c.rawnames_id]).where(and_(
                "namesTable.c.rawnames_id" == rawNameId,
                "namesTable.c.nametypes_id" == nameTypesId,
                "namesTable.c.namegenders_id" == nameGendersId,
                "namesTable.c.nameorigins_id" == nameOriginsId
            )
            )
            rows = conn.execute(s)
            id = None
            if rows.rowcount == 0:
                ins = namesTable.insert()
                rows = conn.execute(ins, rawnames_id=rawNameId,
                                    nametypes_id=nameTypesId,
                                    namegenders_id=nameGendersId,
                                    nameorigins_id=nameOriginsId)
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
