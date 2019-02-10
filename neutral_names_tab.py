#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 15:49:14 2019

@author: william Keilsohn
"""

# Import packages
import pandas as pd
from tabulate import tabulate 

# Connect to other files:
'''
This was explained last semester in Dr. Cassel's class.
The central file has some citations that explain the process, but to be honest, at this point I'm just using my old work as reference.
'''
folder_path = '/home/william/Documents/Class_Scripts/'

exec(open(folder_path + 'neutral_names_func.py').read()) # Holds Dataframes

'''
So there is A LOT os data.
Like soooooooo much data.
Like so much data that when I tried to just make a table to display it all combined, there was no good way to visualize it.

Thus my solution and therefore the tabular display is a little unorthedox, but I hope you undestand.
'''

# Make a list of possible selections:
select_lst = [i + 1880  for i in range(len(year_data))]


# Create tabular format:
def tablePrinter(df, num):
    temp_frame = df[df.Year == num]
    print(tabulate(temp_frame, headers = 'keys', tablefmt = 'psql')) #http://qaru.site/questions/175957/pretty-printing-a-pandas-dataframe

# Parse out tables based on desired metric:
# https://stackoverflow.com/questions/13148429/how-to-change-the-order-of-dataframe-columns
freq_data = total_data[['Year', 'Name', 'Total_Births', 'Frequency']]
neutral_Data = total_data[['Year', 'Name', 'Male_Births', 'Female_Births', 'Total_Births', 'Ratio']]


# Deal with user options:
def pageCounter():
    print('There are ', str(len(select_lst)), 'years of the data to choose from.', end = '\n')
    numVal = int(input('Please enter a year you would like to view: '))
    return numVal

    
def tabChecker(string):
    year_val = pageCounter()
    if string in ['frequency', 'Frenquency', 'F', 'f', 'FREQUENCY']:
        tablePrinter(freq_data, year_val)
    else:
        tablePrinter(neutral_Data, year_val)
        