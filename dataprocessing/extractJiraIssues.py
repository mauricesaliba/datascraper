import subprocess
import shlex


processArgs = shlex.split(
    "python jql_to_csv.py -u maurice.saliba -U 'http://jira.go.com.mt' --jql 'team in (1, 2, 3, 4, 5, 6, 7, DE) AND status CHANGED to (Fixed, Closed) AFTER startOfYear() AND status IN (Fixed, Closed) AND resolution IN (Fixed,Done,Unresolved) ORDER BY key ASC' -n 5000")
print(processArgs)
p = subprocess.run(processArgs)
