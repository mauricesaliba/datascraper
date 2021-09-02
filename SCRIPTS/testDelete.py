import csv
import argparse
import os
from itertools import count

def remap(fieldnames):
    price_count = count(1)
    return ['price{}'.format(next(price_count)) if f.startswith('price') else f
            for f in fieldnames]


def suffixDuplicateStrings(liststrings):
    dicts = {}
    for i in range(len(liststrings)):
      if liststrings[i] in dicts:
        dicts[liststrings[i]] += 1
        liststrings[i] =  liststrings[i] + "_" + str(dicts[liststrings[i]])
      else:       
        dicts[liststrings[i]] = 0
    print(dicts)
    print(liststrings)
    

        
    
values = ["A", "B", "C", "D", "A"]    
print(suffixDuplicateStrings(values))