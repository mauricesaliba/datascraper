import configparser
import logging as log
import numpy as np
import pandas as pd
from utilities.getUniqueColumnValues import getUniqueColumnValues

config = configparser.RawConfigParser()
config.read('config.properties')

logsfile = config.get('Logs', 'files.log.filename')
log.basicConfig(filename=logsfile, encoding='utf-8', level=log.DEBUG)

mergedfilesout = config.get('DataFiles', 'files.jira.issues.filename.merged')
sprintsfile = config.get('DataFiles', 'files.jira.issues.sprints')
assigneesfile = config.get('DataFiles', 'files.jira.issues.assignees')
statusesfile = config.get('DataFiles', 'files.jira.issues.statuses')
typesfile = config.get('DataFiles', 'files.jira.issues.types')
reportersfile = config.get('DataFiles', 'files.jira.issues.reporters')
systemsfile = config.get('DataFiles', 'files.jira.issues.systems')

dfjiraissues = pd.read_csv(mergedfilesout)

def getuniquesprints():
    sorteduniquesprints = getUniqueColumnValues(dfjiraissues, 'Sprint')
    pd.DataFrame(sorteduniquesprints).to_csv(sprintsfile)

def getuniqueassignees():
    sorteduniqueassignees = getUniqueColumnValues(dfjiraissues, 'Assignee')
    pd.DataFrame(sorteduniqueassignees).to_csv(assigneesfile)

def getuniquestatuses():
    sorteduniquestatuses = getUniqueColumnValues(dfjiraissues, 'Status')
    pd.DataFrame(sorteduniquestatuses).to_csv(statusesfile)

def getuniquereporters():
    sorteduniquereporters = getUniqueColumnValues(dfjiraissues, 'Reporter')
    pd.DataFrame(sorteduniquereporters).to_csv(reportersfile)

def getuniquetypes():
    sorteduniquetypes = getUniqueColumnValues(dfjiraissues, 'Issue Type')
    pd.DataFrame(sorteduniquetypes).to_csv(typesfile)

def getuniquesystems():
    sorteduniquesystems = getUniqueColumnValues(dfjiraissues, 'System/Area)')
    pd.DataFrame(sorteduniquesystems).to_csv(systemsfile)

getuniquesprints()
getuniqueassignees()
getuniquestatuses()
getuniquereporters()
getuniquetypes()
getuniquesystems()





