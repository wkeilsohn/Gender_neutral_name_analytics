#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 07:45:39 2019

@author: William Keilsohn
"""

'''
What makes a name gender neutral?

Personally, I think a name is gender neutral if:
    1) The name is used/given by both boys and girls.
    2) Each gender makes up at least 20% of the people with the name for a given year.
    
Based on these standards the following code looks for gender neutral names and attempts to quantify their prevelance.
'''


# Import Packages:
import numpy as np
import pandas as pd


# Load in the data:
years = range(1880,2018) ### This is the script from the notes. 
pieces = []
columns = ['name','sex','births']
for year in years:
    path = '/home/william/Documents/Class_Scripts/baby_names/names/yob%d.txt' %year
    frame = pd.read_csv(path, names = columns)
    frame['year'] = year
    pieces.append(frame)
nameData = pd.concat(pieces, ignore_index = True) ### Don't fix what isn't broken, eh?

# Create an arrangment of columns:
## https://stackoverflow.com/questions/13148429/how-to-change-the-order-of-dataframe-columns
cols = ['year', 'name', 'births']

# Seperate out the two geneders:
boy_data = nameData[nameData.sex == "M"]
boys_data = boy_data[cols] #https://stackoverflow.com/questions/13148429/how-to-change-the-order-of-dataframe-columns
boys_data.columns = ['Year', 'Name', 'Male_Births']



girl_data = nameData[nameData.sex == "F"]
girls_data = girl_data[cols] #https://stackoverflow.com/questions/13148429/how-to-change-the-order-of-dataframe-columns
girls_data.columns = ['Year', 'Name', 'Female_Births']


# Create a summary data table:
# https://stackoverflow.com/questions/41815079/pandas-merge-join-two-data-frames-on-multiple-columns
total_data = pd.merge(boys_data, girls_data, how = 'left', left_on = ['Year', 'Name'], right_on = ['Year', 'Name']) 
total_data = total_data.fillna(0) # Textbook (Pg. 142-143)
total_data['Total_Births'] = total_data[['Male_Births', 'Female_Births']].sum(axis = 1) #https://stackoverflow.com/questions/25748683/pandas-sum-dataframe-rows-for-given-columns/25748826

# Make a copy for some additional calculations:
summed_data = total_data[:]

# Begin calculating frequencies:
## So there are two kinds of frequencies:
## Frequencies between genders, and/or frequency within the population.
   
# Create a frequency calcualtor:
def freqCalc(num1, num2):
    if num1 == 0 or num2 == 0:
        return 0
    elif num1 >= num2:
        return num2 / num1
    else:
        return num1 / num2
    
## Now we can determine the ratio between genders:
ratio_lst = []
for i in range(len(total_data)):
    ratio_lst.append(freqCalc(total_data['Male_Births'][i], total_data['Female_Births'][i]))
total_data['Ratio'] = ratio_lst


# Based on the criteria for a gender neutral name above:
total_data = total_data.query('Ratio>=0.2 & Ratio<=0.8') #http://jose-coto.com/query-method-pandas


# With this filtered dataframe it is possible to determine how names gender neutral names have changed over time:
year_data = total_data.groupby(['Year']).agg('count') # https://stackoverflow.com/questions/19384532/how-to-count-number-of-rows-per-group-and-other-statistics-in-pandas-group-by
year_data = year_data['Name']
year_data.columns = ['Number of Gender Neutral Names']


## Determine "Frequency" within the population as a whole:
summed_year_data = summed_data.pivot_table('Total_Births', index = 'Year', aggfunc = sum) # From Ppt
summed_year_vals = summed_year_data.sum(axis = 1) # http://blog.mathandpencil.com/column-and-row-sums

freq_lst = []
for i in range(len(total_data)):
    freq_lst.append(total_data['Total_Births'].iloc[i] / summed_year_vals.loc[total_data['Year'].iloc[i]])
total_data['Frequency'] = freq_lst


### Answer the Questions:
'''
Due to how much room the tables take up, and the graph needing to go at the end, I've written a sepearate file to handle user input.
Please run the script from that file. 
'''
 
# Question 1:
def nameTrender():
    names_change = False # Just create a dummy variable to use later.
    if year_data[2017] > year_data[1880]:
        names_change = True
        return names_change
    else:
        names_change = False
        return names_change
    
def slopeEvaluater(bol):
    if bol:
        print('Yes')
    else:
        print('No')
    print('\n')
        

# Question 2:
def trendTracker(bol):
    print('\n')
    if bol:
        print('There are ', year_data[2017] - year_data[1880], ' more gender nuetral names now than in 1880.')
    else:
        print('There are ', year_data[1880] - year_data[2017], ' less gender nuetral names now than in 1880.')
    print('\n')


# Question 3~ish:
# Create Plot(s):
def graphPrinter():
    print('\n')
    print('Here is a graphical representation of the useage of gender nuetral names over time: ')
    print('\n')
    year_data.plot(title = 'Total Gender-Neutral Names per Year') # From ppt.