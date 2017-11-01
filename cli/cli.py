#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Shell wrapper around randnames.py
"""

import os
import sys
import getopt
import randnames

def main(argv):

    # parse arguments
    gender = 'any'
    numberOfNames = 1
    global debug
    debug = False
    try:
        opts, args = getopt.getopt(argv, "hxg:n:", ["gender=", "number="])
    except getopt.GetoptError:
        print('generate-name.py [-x] -g <gender> -n <number>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('generate-name.py [-x] -g <gender> -n <number>')
            sys.exit()
        elif opt == '-x':
            debug = True
        elif opt in ("-g", "--gender"):
            gender = arg
        elif opt in ("-n", "--number"):
            numberOfNames = arg
    if debug is True:
        print('DEBUG: Gender is {}'.format(gender))
        print('DEBUG: Number of names to generate is {}'.format(numberOfNames))

    if debug:
        import pdb; pdb.set_trace()

    randnames.load_names()
    for n in range(0,int(numberOfNames)):
        first_name = randnames.generate_name(gender, 'first')
        last_name = randnames.generate_name(gender, 'last')
        print('{} {}'.format(first_name, last_name))

if __name__ == "__main__":
    main(sys.argv[1:])
