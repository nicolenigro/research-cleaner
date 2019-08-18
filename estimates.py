"""
Author: Nicole Nigro
Date: 8/1/19

Summary: This program identifies and pulls words/chars/ints from the email
bodies stored in the csv file that is read in, then stores them in a new
dataframe, which is ultimately saved as a csv file.

How to use: Have this python file saved to a folder. In that folder, save the
file that you want to scrape. Change the string for file_name to that file.
"""

import pandas as pd
import re

file_name = 'cleanedResearchMGMT.csv' #whatever file you wanna read in
df = pd.read_csv(file_name)

email_body = df.Body #storing the Body column as a variable

new_df = pd.DataFrame() #data frame where the values found in this program will be stored

#Organization Name
name_results = [] #empty list to add the org names to
for cell in email_body: #iterate over each row in the Body column
    match = re.search(r'From: (\S+)', cell) #regex for word after "From:"
    if match:
        organization_name = match.group(1) #storing the string following "From:"
        organization_name = "".join(c for c in organization_name if c not in ('"', ',')) #strip the punctuation
        if organization_name != "Mack": #filter for "Mack" because that can't be one of the org's names
            name_results.append(organization_name) #add string to org name list 
        else:
            name_results.append("")
    else:
        name_results.append("") #add blanks to org name list where it didn't find a name
new_df['Organization Name'] = pd.Series(name_results) #create column and populate it with list of organization names

"""These next few chunks of code basically follow the same logic for each of 
the terms you're looking for within the bodies of the emails, and pulls in 
similar logic from the chunk of code above."""

#Revenue
revenue_numbers = []
for cell in email_body:
    match = cell[cell.find('revenue'):cell.find('revenue')+100] #finds the word "revenue" and the 100 chars that follow and stores that string as a variable 
    rev_list = list(re.findall(r'\$?\+?\-?\d+(?:[-.,]\d+)?%?\D?', match))
    revenue_numbers.append(rev_list)
new_df['Revenue List'] = pd.Series(revenue_numbers)

#Gross Profit
gross_profit_numbers = []
for cell in email_body:
    match = cell[cell.find('gross profit'):cell.find('gross profit')+100]
    gp_list = list(re.findall(r'\$?\+?\-?\d+(?:[-.,]\d+)?%?\D?', match))
    gross_profit_numbers.append(gp_list)    
new_df['Gross Profit List'] = pd.Series(gross_profit_numbers)

#EBITDA
ebitda_numbers = []
for cell in email_body:
    match = cell[cell.find('ebitda'):cell.find('ebitda')+100]
    print(match)
    ebitda_list = list(re.findall(r'\$?\+?\-?\d+(?:[-.,]\d+)?%?\D?', match))
    print(ebitda_list)
    ebitda_numbers.append(ebitda_list)        
new_df['EBITDA List'] = pd.Series(ebitda_numbers)

#Net Income
net_income_numbers = []
for cell in email_body:
    match = cell[cell.find('net income'):cell.find('net income')+100]
    net_list = list(re.findall(r'\$?\+?\-?\d+(?:[-.,]\d+)?%?\D?', match))
    net_income_numbers.append(net_list)         
new_df['Net Income List'] = pd.Series(net_income_numbers)

#Free Cash Flow
free_cash_flow_numbers = []
for cell in email_body:
    match = cell[cell.find('free cash flow'):cell.find('free cash flow')+100]
    fcf_list = list(re.findall(r'\$?\+?\-?\d+(?:[-.,]\d+)?%?\D?', match))
    free_cash_flow_numbers.append(fcf_list)
new_df['Free Cash Flow List'] = pd.Series(free_cash_flow_numbers) 

#Debt
debt_numbers = []
for cell in email_body:
    match = cell[cell.find('debt'):cell.find('debt')+100]
    debt_list = list(re.findall(r'\$?\+?\-?\d+(?:[-.,]\d+)?%?\D?', match))
    debt_numbers.append(debt_list)    
new_df['Debt List'] = pd.Series(debt_numbers)

#Cash
cash_numbers = []
for cell in email_body:
    match = cell[cell.find('cash'):cell.find('cash')+100]
    cash_list = list(re.findall(r'\$?\+?\-?\d+(?:[-.,]\d+)?%?\D?', match))
    cash_numbers.append(cash_list)
new_df['Cash List'] = pd.Series(cash_numbers)

#Cash Equivalent
cash_equivalent_numbers = []
for cell in email_body:
    match = cell[cell.find('cash equivalent'):cell.find('cash equivalent')+100]
    cash_equiv_list = list(re.findall(r'\$?\+?\-?\d+(?:[-.,]\d+)?%?\D?', match))
    cash_equivalent_numbers.append(cash_equiv_list)
new_df['Cash Equivalent List'] = pd.Series(cash_equivalent_numbers)

#Price Target
price_target_numbers = []
for cell in email_body:
    match = cell[cell.find('price target'):cell.find('price target')+100]
    price_targ_list = list(re.findall(r'\$?\+?\-?\d+(?:[-.,]\d+)?%?\D?', match))
    price_target_numbers.append(price_targ_list)
new_df['Price Target List'] = pd.Series(price_target_numbers)

#save new data frame to a csv file
new_df.to_csv('estimateData.csv') 


"""
#list of all numbers found in each email body
numbers_found = []
for cell in email_body:
    match = re.findall(r'[+-]?\d+', cell)
    numbers_found.append(match)
    print(match)
new_df['Numbers found in email bodies'] = pd.Series(numbers_found)
"""

"""
#general formatting to match any 100 chars following
gross_profit_numbers = []
for cell in email_body:
    match = cell[cell.find('gross profit'):cell.find('gross profit')+100]
    gp_list = list(re.findall(r'\$?\+?\-?\d+(?:[-.,]\d+)?%?\D?', match))
    gross_profit_numbers.append(gp_list)    
new_df['Gross Profit List'] = pd.Series(gross_profit_numbers)
"""