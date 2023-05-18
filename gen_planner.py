#!/usr/bin/env python3

from datetime import date, timedelta
from sys import argv

# $ ./gen_planner.py START_YYYY-MM-DD END_YYYY-MM-DD
# $ ./gen_planner.py 2023-05-18 2023-06-11

s = date(*[int(x) for x in argv[1].split("-")])
e = date(*[int(x) for x in argv[2].split("-")])

for n in range((e-s).days+1):
  d = s + timedelta(n)
  print(f'----------------  #{n:02} : {d.strftime("%a %b %d")}  ----------------\n\n')
