#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 1) load and cache a database of names (see schema.ddl)
 2) retrieve a random name from the cache by type (first, last) and gender (male, female, any)

 At first I made a normalized database to store the name data, but I realized that it's actually
 very inefficient to get random values from a database, and there really isn't that much data,
 even with all the most popular first and last names from the US Census data. So I'm switching
 over to using a single names table.
"""

import random
import configparser
from sqlalchemy import *
from sqlalchemy.sql import text

"""
Make sure the names have been loaded and cached, then pick
one at random of the right gender and type.
"""
def generate_name(gender, nametype):
    name = None
    if not initialized is True:
        load_names()
    found = False
    if nametype == 'first':
        if gender == 'female':
            name = random.choice(ffnames)
        elif gender == 'male':
            name = random.choice(mfnames)
        else:
            name = random.choice(fnames)
    else:
        name = random.choice(lnames)
    return name

'''
We could load the names into the different lists with separate
database queries, but I think it's faster to get them all and
split them up here.
'''
def load_names():
    global names
    global ffnames # female first names
    global mfnames # male first names
    global fnames # first names (either gender)
    global lnames # last names
    names = None
    ffnames = []
    mfnames = []
    fnames = []
    lnames = []
    global initialized
    initialized = False
    random.seed() # initialize random number generator (used by generate_name_) with system time
    Config = configparser.ConfigParser()
    Config.read("writertoys.cfg")
    host = Config.get("Database", "host")
    dbtype = Config.get("Database", "dbtype")
    dbname = Config.get("Database", "database")
    connectstr = dbtype + "://@" + host + "/" + dbname
    # todo: handle any database errors
    engine = create_engine(connectstr)
    conn = engine.connect()
    metadata = MetaData()
    nametable = Table('names', metadata, autoload=True, autoload_with=engine)
    s = select([nametable])
    rows = conn.execute(s)
    names = rows.fetchall()
    for name in names:
        (nameid, rawname, ntype, ngender, origin) = name
        if ntype == u'first':
            if ngender == u'female':
                ffnames.append(str(rawname))
            elif ngender == u'male':
                mfnames.append(str(rawname))
            fnames.append(str(rawname)) # either/any
        else:
            lnames.append(str(rawname))
    initialized = True
