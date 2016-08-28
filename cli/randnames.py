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
    while not found:
        name = random.choice(names)
        (nameid, rawname, ntype, ngender, origin) = name
        # Wow, this is *really* inefficient, since there are a LOT more last names than first names
        # Need to change this to load first and last names into different arrays (and gendered names?)
        if str(ntype) != nametype:
            continue
        if str(ngender) != 'either' and gender != 'any' and str(ngender) != gender:
            continue
        found = True
    return str(rawname)

def load_names():
    global names
    names = None
    global initialized
    initialized = False
    random.seed() # initialize random number generator (used by generate_name_) with system time
    dbname = 'writertoys'
    # todo: allow non-local database
    # todo: handle any database errors
    engine = create_engine('postgresql://@localhost/' + dbname)
    conn = engine.connect()
    metadata = MetaData()
    nametable = Table('names', metadata, autoload=True, autoload_with=engine)
    s = select([nametable])
    rows = conn.execute(s)
    names = rows.fetchall()
    initialized = True
