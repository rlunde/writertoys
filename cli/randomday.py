#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 pick a random day from the past year
"""

import random
import datetime
"""
1) get a random number of days from 1-364
2) subtract from today
3) print result
"""
def pickday():
    days_before = random.randint(1, 364)
    today = datetime.date.today()
    then = today - datetime.timedelta(days=days_before)
    return then.isoformat()

print(pickday())

