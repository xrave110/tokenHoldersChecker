#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 18:29:47 2021

@author: anything
"""

import pandas as pd
import matplotlib.pyplot as plt
import os
import json

from configPkg import token_data_path

def takeData(csv_name):
    pass

# Make the graphs a bit prettier, and bigger
plt.style.use('ggplot')

# This is necessary to show lots of columns in pandas 0.12. 
# Not necessary in pandas 0.13.
pd.set_option('display.width', 5000) 
pd.set_option('display.max_columns', 60)

plt.rcParams['figure.figsize'] = (15, 5)

total_df = pd.DataFrame()
dict_of_data = {}

for json_name in os.listdir(token_data_path):
    if '.json' in json_name:
        json_path = token_data_path + json_name;
        data1 = {'Total Balance': {}}
        with open(json_path, 'r') as json_file:
            data = json.load(json_file)
        for key in data['Total Balance'].keys():
            length_start = len(key.split('_')[0]) + 1 # +1 is to remove underscore
            length_end = len(key.split('_')[-1]) + 1
            data1['Total Balance'][key[length_start:-length_end]] = data['Total Balance'][key]
        dict_of_data[json_name.split("_")[1]] = data1['Total Balance']
#print(dict_of_data)
total_df = pd.DataFrame(dict_of_data)
total_df.sort_index(inplace=True)
total_df.to_csv("Token_Total_Balances.csv")
#total_df.plot()
            
