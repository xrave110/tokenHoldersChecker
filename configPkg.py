#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 15:59:49 2021

@author: anything
"""
import os

# Params
FIRST_HOLDER = 50
LAST_HOLDER = 60

# Constants
INFURA_ID = os.getenv('INFURA_ID')

infura_url = 'https://mainnet.infura.io/v3/' + INFURA_ID
ethscan_exports_path = os.getcwd()+'/etherscanExports/'
token_data_path = os.getcwd()+'/tokenData/'
dict_of_conv = {
    '1': 'wei',
    '1000': 'kwei' ,
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