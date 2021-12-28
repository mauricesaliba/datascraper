import subprocess
import shlex
import getpass
import mergeFiles
import unpivotSprints

password = getpass.getpass("Input Jira password:")
workingDirectory = input("Input working directory:")
issuesFilePath = workingDirectory + "/ISSUES"
epicsFilePath = workingDirectory + "/EPICS"

## 01. GET ISSUES
processArgs01 = shlex.split(
    "python jql_to_csv.py -u maurice.saliba -p " + password + " -P \"" + issuesFilePath +
    "\" -U 'http://jira.go.com.mt' --jql 'filter = DIGITAL-MAURICE-UPDATED-2019-01' -n 5000")
p = subprocess.run(processArgs01)

## 02. GET EPICS
processArgs02 = shlex.split(
    "python jql_to_csv.py -u maurice.saliba -p " + password + " -P \"" + epicsFilePath +
    "\" -U 'http://jira.go.com.mt' --jql 'type = Epic and created >= startOfYear(-3) ORDER BY created' -n 5000")
p = subprocess.run(processArgs02)

## 03. MERGE ISSUES FILES RETRIEVED IN STEP ## 01 INTO ONE FILE
mergeFiles.merge(issuesFilePath, issuesFilePath + "/output.csv")



## 04. UNPIVOT SPRINTS
##unpivotSprints.unpivot() ---->>> decided to skip this since we want only work completed and not carried over to next sprints. If needed unpivot in memory. No need to persist.









