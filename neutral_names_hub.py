#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 10:06:44 2019

@author: william Keilsohn
"""

''''
This document deals with data displating.

Please run this file rather than the others individually.

### Note: This whole project is going to take about 1-1.5min to load.... sorry about that. 
'''


# Import additional files:
'''
## This was done in Dr. Cassel's  class last semester, but here is a citation that explains the setup:
### https://stackoverflow.com/questions/7974849/how-can-i-make-one-python-file-run-another
### https://www.programiz.com/python-programming/methods/built-in/exec
'''
folder_path = '/home/william/Documents/Class_Scripts/'

exec(open(folder_path + 'neutral_names_func.py').read()) # Holds functions
exec(open(folder_path + 'neutral_names_tab.py').read()) # Deals with tables

# Options for the user:
options = ['Evaluate Trend', 'Evaluate Numeric Change', 'Print Tabular Display', 'Display Graphs']

# Deal with run checking:
def runChecked(string):
    if string in ['y', 'Y', 'yes', 'YES', 'Yes']:
        return True
    else:
        return False

run_checker = True


# Create a welcome Message:
print('Hello, and welcome to Neutral Name Data Exploration!\nPlease Select an option to get started: ')



# Create User Interface:
while run_checker:
    print('\n')
    print(options, end = '\n')
    user_select = int(input('Please select the number which corosponds to your choice: '))
    trend = nameTrender()
    if user_select == 0:
        print('\n')
        print('Are there more gender-neutral names today than in 1880: ', end = '')
        slopeEvaluater(trend)
    elif user_select == 1:
        print('\n')
        trendTracker(trend)
    elif user_select == 2:
        print('\n')
        table_answer = input('Would you like a table of the total individuals, or a table of the frequencies? ')
        tabChecker(table_answer)
        print('\n')
    else:
        print('\n')
        graph_select = runChecked(input('Are you sure you want to see the graph? It will terminate the interface.: '))
        if graph_select:
            graphPrinter()
            break # Graph will not print while the loop is still going.
    run_checker = runChecked(input('Whould you like to select another option? (y/n): '))

