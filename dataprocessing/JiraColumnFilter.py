import csv

import pandas as pd


def remove_non_ascii(s):
    return "".join(c for c in s if ord(c)<128)


issues_filepath = "C:/Users/maurice.saliba/OneDrive - GO PLC/MANAGEMENT/JIRA/Workspace/RUNS/2022-03-15/ISSUES/"
issues_filename_input = "filtered1.csv";
issues_filename_output = "filtered2.csv";


dfjiras = pd.read_csv(issues_filepath + issues_filename_input, encoding='latin-1')

dfjiras_filtered = dfjiras.filter(["Summary",	"Issue key",	"Issue id",	"Issue Type",	"Status",	"Project key",	"Priority",	"Resolution",	"Assignee",	"Reporter",	"Creator",	"Created",	"Updated",	"Resolved",	"Fix Version/s",	"Component/s",	"Due Date",	"Labels",	"Description",	"Outward issue link (Depends)",	"Outward issue link (Relates)",	"Custom field (Corporate Project Code)",	"Custom field (Epic Link)",	"Custom field (Epic Name)",	"Sprint",	"Sprint_1",	"Sprint_2",	"Sprint_3",	"Sprint_4",	"Sprint_5",	"Sprint_6",	"Sprint_7",	"Sprint_8",	"Sprint_9",	"Custom field (Story Points)",	"Custom field (System/Area)",	"Custom field (Team)"])





dfjiras_filtered['Description'] = dfjiras_filtered['Description'].str.slice(0,1000)




dfjiras_filtered.to_csv(issues_filepath + issues_filename_output, index=False)
print(dfjiras_filtered.head())