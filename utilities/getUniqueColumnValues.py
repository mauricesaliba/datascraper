import configparser
import logging as log
import numpy as np
import pandas as pd

config = configparser.RawConfigParser()
config.read('config.properties')


def getUniqueColumnValues(dfjiraissues, columnsearchfilter):


  dataheader = dfjiraissues.columns.tolist()
  sprintcolumns = list(filter(lambda k: columnsearchfilter in k, dataheader))
  uniquesprints = pd.unique(dfjiraissues[sprintcolumns].astype(str).values.ravel('K'))
  sorteduniquesprints = np.sort(uniquesprints)
  return sorteduniquesprints








