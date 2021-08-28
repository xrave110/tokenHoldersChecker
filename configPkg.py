#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 15:59:49 2021

@author: anything
"""
import os

# Params
first_holder = 50
default_last_holder = 3050
percentage_to_consider = 15
from dotenv import load_dotenv

# Constants
load_dotenv()
node_provider = os.getenv("INFURA_ID")
infura_url = 'https://mainnet.infura.io/v3/' + node_provider
ethscan_exports_path = os.getcwd()+'/etherscanExports/'
token_data_path = os.getcwd()+'/tokenData/'
dict_of_conv = {
    '1': 'wei',
    '1000': 'kwei',
    '1000000': 'mwei' ,
    '1000000000': 'gwei',
    '1000000000000': 'micro' ,
    '1000000000000000': 'milliether' ,
    '1000000000000000000': 'ether' ,
    '1000000000000000000000': 'kether',
    '1000000000000000000000000': 'mether' ,
    '1000000000000000000000000000': 'gether' ,
    '1000000000000000000000000000000': 'tether' 
    }