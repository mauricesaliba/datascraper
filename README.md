# datascraper
to scrape data from any source endpopint


TODO:

1. Create one main file to orchestrate all ETL
2. To implement incremental updates to Power BI tables.



## 01 RUN jql_to_csv.py - extract jira issues and Epics

**to get issues use jql:** 'team in (1, 2, 3, 4, 5, 6, 7, DE) AND status CHANGED to (Fixed, Closed) AFTER startOfYear() AND status IN (Fixed, Closed) AND resolution IN (Fixed,Done,Unresolved) ORDER BY key ASC'
**to get epics use jql:** 'type = Epic and created >= startOfYear(-3) ORDER BY created'

python jql_to_csv.py -u maurice.saliba -U "http://jira.go.com.mt" --jql 'team in (1, 2, 3, 4, 5, 6, 7, DE) AND status CHANGED to (Fixed, Closed) AFTER startOfYear() AND status IN (Fixed, Closed) AND resolution IN (Fixed,Done,Unresolved) ORDER BY key ASC' -n 5000

python jql_to_csv.py -u maurice.saliba -U "http://jira.go.com.mt" --jql 'type = Epic and created >= startOfYear(-3) ORDER BY created' ORDER BY key ASC' -n 5000

https://confluence.atlassian.com/jirakb/exporting-jira-s-issues-using-csv-in-batches-1071829731.html

## 02 RUN MergFiles.py - merges multiple jira issues CSV files into one.

python mergeFiles.py --ifp 'C:\Users\maurice.saliba\OneDrive - GO PLC\MANAGEMENT\JIRA\datascraper\INPUT FILES\' --ofp 'C:\Users\maurice.saliba\OneDrive - GO PLC\MANAGEMENT\JIRA\datascraper\OUTPUT FILES'

## 03 RUN unpivotSprints.py - removes multiple sprint columns and repeats rows per sprint value. creates a sprint issue man-to-many intermediate table. No arguments needed to run file

python unpivotSprints.py

## 04 RUN getUniqueJiraCategories.py - creates all the necessary dimension tables (seperate CSV files) for Jiras. Example: types, status, assignee.

## 05 Get projects file from Confluence

## 06 Load data in Power BI 


