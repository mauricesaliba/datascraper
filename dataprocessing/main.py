import pandas as pd

issuesfilepath = "C:/Users/maurice.saliba/OneDrive - GO PLC/MANAGEMENT/JIRA/Workspace/RUNS/2022-11-03/ISSUES/output.csv"
outfilepath = "C:/Users/maurice.saliba/OneDrive - GO PLC/MANAGEMENT/JIRA/Workspace/RUNS/2022-11-03/ISSUES/storypoints.csv"
projectsfilepath = "C:/Users/maurice.saliba/OneDrive - GO PLC/MANAGEMENT/JIRA/Workspace/COMMON SLOW CHANGING/projects.csv"
epicsfilepath = "C:/Users/maurice.saliba/OneDrive - GO PLC/MANAGEMENT/JIRA/Workspace/RUNS/2022-11-03/EPICS/"


dfissues = pd.read_csv(issuesfilepath)
dfepics = pd.read_csv(epicsfilepath)
dfprojects = pd.read_csv(projectsfilepath)

#remove rows that do not have an 'issue id' and replace NaN with empty string.
dfissuesvalidated = dfissues[(dfissues['Issue id'] >= 99999) & (dfissues['Issue id'] <= 1000000)]
dfissuesvalidated['Custom field (Epic Link)'] = dfissuesvalidated['Custom field (Epic Link)'].fillna('')
dfissuesvalidated['Custom field (Epic Link)'] = dfissuesvalidated['Custom field (Epic Link)'].fillna('')

#df['date_col'] = pd.to_datetime(df['date_str'], utc=True)
#print(df.date_str.dtype)  # datetime64[ns, UTC]
dfissuesvalidated['Resolved'] = pd.to_datetime(dfissuesvalidated['Resolved'], format="%d/%b/%y %I:%M %p")
dfissuesvalidated['Updated'] = pd.to_datetime(dfissuesvalidated['Updated'], format="%d/%b/%y %I:%M %p")
dfissuesvalidated['Created'] = pd.to_datetime(dfissuesvalidated['Created'], format="%d/%b/%y %I:%M %p")

print("Resolved data type:  ",dfissuesvalidated['Resolved'])

print(dfissuesvalidated.shape)

statuses_done = ["Closed", "Done", "Fixed"]
dfissues_done = dfissuesvalidated[dfissuesvalidated['Status'].isin(statuses_done)]

#Update the COVI external dependencies documentation in confluence	COVI-709	819255		Task	Closed
#Replace bsi calls for  product links with data from basket.	COVI-708	819216		Task	On Hold

print(dfissues_done)

# Filter data between two dates
dfissues_done = dfissues_done.loc[(dfissues_done['Updated'] >= '2021-10-01')
                     & (dfissues_done['Updated'] <= '2021-11-30')]


# Filter data between two dates
dfissues_resolved = dfissuesvalidated.loc[(dfissuesvalidated['Resolved'] >= '2021-10-01')
                     & (dfissuesvalidated['Resolved'] <= '2021-11-30')]



dfissues_resolved_done = dfissues_resolved.append(dfissues_done,ignore_index = True)
dfissues_resolved_done = dfissues_resolved_done.drop_duplicates(subset=['Issue key'])





print(dfissues_resolved_done.shape)

#dfissuesvalidated = dfissuesvalidated.astype({"Custom field (Epic Link)": str})
#dfepics = dfepics.astype({"Issue key": str})

dfepicsreduced = dfepics[["Issue key","Custom field (Corporate Project Code)"]]

dfissueswithepics = pd.merge(dfissues_resolved_done, dfepicsreduced, how="left", left_on="Custom field (Epic Link)", right_on="Issue key",suffixes=('_x', '_y'))
dfissueswithepicsprojects = pd.merge(dfissueswithepics, dfprojects, how="left", left_on="Custom field (Corporate Project Code)_y", right_on="id",suffixes=('_x', '_y'))

grouped_multiple = dfissueswithepicsprojects.groupby(['Custom field (Corporate Project Code)_y','Project Name', 'Assignee']).agg({'Custom field (Story Points)': ['mean', 'sum']})
grouped_multiple.columns = ['sp_mean','sp_sum']
grouped_multiple = grouped_multiple.reset_index()

grouped_multiple.to_csv(outfilepath)


#print(dfcolumns[dfcolumns.str.contains('Points')])
#print(dfissuesvalidated['Custom field (Epic Link)'])
#print(dfepics['Issue key'])
#print(dfissuesvalidated[pd.isna(dfissuesvalidated['Custom field (Epic Link)'])])#print(dfepics[dfepics['Issue key'].map(type) != str])
#print(dfepics[["Issue key","Custom field (Corporate Project Code)"]])


