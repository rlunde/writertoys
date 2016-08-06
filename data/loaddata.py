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

def main(argv):
   global database
   database['engine'] = engine = create_engine('postgresql://localhost/writertoys')
   database['conn'] = conn = engine.connect()
   database['metadata'] = metadata = MetaData()
   # todo: call a function 3 times to load csv files

if __name__ == "__main__":
   main(sys.argv[1:])

