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
"""
def generate_name(gender, nametype):
    name = None
    return name

def load_names(database)
    dbname = 'writertoys'
    gender = 'any'
    # todo: allow non-local database
    # todo: handle any database errors
    engine = create_engine('postgresql://@localhost/' + database)
    conn = engine.connect()
    metadata = MetaData()
    nametable = Table('names', metadata, autoload=True, autoload_with=engine)
