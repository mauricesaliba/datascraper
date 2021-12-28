import configparser
import pandas as pd


def unpivot():
    config = configparser.RawConfigParser()
    config.read('../config.properties')
    mergedfilesout = config.get('DataFiles', 'files.jira.issues.filename.merged')
    unpivotedSprintsFilename = config.get('DataFiles', 'files.jira.issues.sprints.unpivoted')
    dfjiraissues = pd.read_csv(mergedfilesout)
    dfjiraissuesunpivoted = dfjiraissues.melt(id_vars='Issue key',
                                              value_vars=['Sprint', 'Sprint_1', 'Sprint_2', 'Sprint_3', 'Sprint_4',
                                                          'Sprint_5',
                                                          'Sprint_6', 'Sprint_7', 'Sprint_8', 'Sprint_9', 'Sprint_10',
                                                          'Sprint_11',
                                                          'Sprint_12', 'Sprint_13', 'Sprint_14', 'Sprint_15'],
                                              var_name='Sprint',
                                              value_name='SprintValue')
    # remove sprint columns from origin jira issues dataset
    print(dfjiraissues.columns)
    cols = [c for c in dfjiraissues.columns if c.lower()[:6] != 'sprint']
    print(cols)
    dfjiraissues = dfjiraissues[cols]
    dfjiraissuesunpivoted = dfjiraissuesunpivoted[
        (dfjiraissuesunpivoted.Sprint == 'Sprint') | (dfjiraissuesunpivoted.SprintValue.notnull())]
    mergeddataframes = pd.merge(left=dfjiraissuesunpivoted, right=dfjiraissues, left_on='Issue key',
                                right_on='Issue key')
    # What's the size of the output data?
    print(mergeddataframes.shape)
    print(mergeddataframes.columns)
    mergeddataframes.to_csv(unpivotedSprintsFilename)



