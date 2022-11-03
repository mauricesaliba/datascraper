import pandas as pd

issuesfilepath = "C:/Users/maurice.saliba/OneDrive - GO PLC/MANAGEMENT/JIRA/Workspace/RUNS/2022-03-15/ISSUES/output - Copy.csv"
dfissues = pd.read_csv(issuesfilepath,encoding='latin-1')



print(dfissues.shape[0])

regex = "^[a-zA-Z]+-[0-9]+$"
dfissues_filtered = dfissues[dfissues['Issue key'].str.match(regex,na=False)]

print(dfissues_filtered.shape[0])

bool_series = pd.notnull(dfissues['Issue key'])
dfissues_filtered = dfissues_filtered[bool_series]

dfissues_filtered.to_csv("C:/Users/maurice.saliba/OneDrive - GO PLC/MANAGEMENT/JIRA/Workspace/RUNS/2022-03-15/ISSUES/filtered1.csv")

