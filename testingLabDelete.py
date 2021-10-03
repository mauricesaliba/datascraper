import argparse
import os
from itertools import count

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


joe = 'Col1', 'Col2'
print(type(joe))