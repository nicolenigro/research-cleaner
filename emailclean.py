"""
Author: Nicole Nigro
Date: 8/12/19

This program cleans the exported email data and saves it to a new file that 
only has emails sent to Research or Research Team.
"""

import pandas as pd

file_name = 'ResearchMGMT1.csv' #the name of the file you're reading in
dataframe = pd.read_csv(file_name, encoding = "ISO-8859-1")

dataframe = dataframe[(dataframe.EmailTo == 'Research Team') | (dataframe.EmailTo == 'Research')]

dataframe.to_csv('CleanedResearchMGMT2.csv') #name of file you're saving cleaned data to