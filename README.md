# datascraper
to scrape data from any source endpopint


TODO:

3. Get unique project codes - has to be done from epics datasource
4. Get Epics from Jira
5. Filter out columns that are not needed from merging process output csv
6. Create Calendar dimension
7. Create one main file to orchestrate all ETL
8. To implement incremental updates to Power BI tables.
9. To create visualizations.


## RUN jql_to_csv.py - extract any jira issues by any JQL search

**to get issues use jql:** 'team in( 1 , 2, 3, 4, 5, 6) AND updatedDate >= "2019/01/01" AND updatedDate <= "2021/12/31" ORDER BY key'
**to get epics use jql:** 'type = Epic  and created >= "2019/01/01" ORDER BY created'


https://confluence.atlassian.com/jirakb/exporting-jira-s-issues-using-csv-in-batches-1071829731.html

python jql_to_csv.py -u maurice.saliba -U "http://jira.go.com.mt" --jql 'team in( 1 , 2, 3, 4, 5, 6) AND updatedDate >= "2019/01/01" AND updatedDate <= "2021/12/31" ORDER BY key' -n 5000

## RUN MergFiles.py - merges multiple jira issues CSV files into one.

python mergeFiles.py --ifp 'C:\Users\maurice.saliba\OneDrive - GO PLC\MANAGEMENT\JIRA\datascraper\INPUT FILES\' --ofp 'C:\Users\maurice.saliba\OneDrive - GO PLC\MANAGEMENT\JIRA\datascraper\OUTPUT FILES'

## RUN unpivotSprints.py - removes multiple sprint columns and repeats rows per sprint value. creates a sprint issue man-to-many intermediate table. No arguments needed to run file

python unpivotSprints.py

## RUN getUniqueJiraCategories.py - creates all the necessary dimension tables (seperate CSV files) for Jiras. Example: types, status, assignee.

## Get projects file from Confluence

## Load data in Power BI 


