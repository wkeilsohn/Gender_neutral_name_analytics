#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 13:57:05 2019

@author: William Keilsohn
"""

# Import Packages:
import pandas as pd
from tabulate import tabulate

# Load in the baby_names data:
years = range(1990,2000) ## This is the script from the notes. 
pieces = [] ### Also, yes, I only picked the specific interval b/c why bother with the extra?
columns = ['name','sex','births']
for year in years:
    path = '/home/william/Documents/Class_Scripts/baby_names/names/yob%d.txt' %year
    frame = pd.read_csv(path, names = columns)
    frame['year'] = year
    pieces.append(frame)
nameData = pd.concat(pieces, ignore_index = True) ### Don't fix what isn't broken, eh?

# Sort out the boys and girls:
boys_data = nameData[nameData.sex == 'M']
girls_data = nameData[nameData.sex == 'F'] 

# Group by name and year:
## Technically in the ppt...
boys_data = boys_data.pivot_table('births', index = 'year', columns = 'name')
girls_data = girls_data.pivot_table('births', index = 'year', columns = 'name')


# Make a list of unique names by sex (and filter out the ones that are not unique):
## Technically in the ppt...
boys_names = set(boys_data.columns)
girls_names = set(girls_data.columns)

'''
# If you want names that are ONLY in ONE gender run these lines:
## These lines filter based on use in both genders and make lists: 
# Textbook (Pg. 417)
boys_lst = list(boys_names.difference(girls_names))
girls_lst = list(girls_names.difference(boys_names))
'''
# Else run these lines:
## These lines turn the sets (w/o duplicates) back into lists for later use:
boys_lst = list(boys_names)
girls_lst = list(girls_names)

boys_data = boys_data[boys_lst]
girls_data = girls_data[girls_lst]

### Output question answer:
print("\nNow printing the unique boys' names: \n")
print(boys_lst)
print("\nNow printing the unique girls' names: \n")
print(girls_lst)

#---------------------------------#
# Make future outputs look pretty:
def prettyPrinter(df):
    temp_df =  df.iloc[-7:, :6] #Just wanted to grab a small subset.
    print(tabulate(temp_df, headers = 'keys', tablefmt = 'psql')) 
    #http://qaru.site/questions/175957/pretty-printing-a-pandas-dataframe
#---------------------------------#

# Make a table showing the occurances of each name per year:
## Textbook (Pg.142)
boys_data = boys_data.fillna(0)
girls_data = girls_data.fillna(0)


### Output question answer:
print("\nPrinting boys' data: \n")
prettyPrinter(boys_data) # You can ofcourse just print the table if you want a larger display.
print('\n')
print("Printing girls' data: \n")
prettyPrinter(girls_data)

# Make the requested alterations to the tables:
def summaryStats(df):
    tmp_data = df.diff() # Don't want the average and/or the year(s) incluided in the calculations. 
    #https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.diff.html
    df.loc['Average'] = pd.Series(df[list(df.columns)].mean()) # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.mean.html
    df.loc['Year w/ Most Births'] = pd.Series(df[list(df.columns)].idxmax()) # Makes the assumption the year with the most people with a given name is the year it is most common.
    #https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.idxmax.html
    df.loc['Year w/ Greatest Change'] = pd.Series(tmp_data[list(tmp_data.columns)].idxmax())
    return df

boys_data = summaryStats(boys_data)
girls_data = summaryStats(girls_data)

### Output final results:
print("\nPrinting final boys' data: \n")
prettyPrinter(boys_data)
print("\nPrinting final girls' data: \n")
prettyPrinter(girls_data)

