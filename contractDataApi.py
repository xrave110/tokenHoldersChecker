#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 19:09:18 2021

@author: anything
"""

import os
import pandas as pd
from web3 import Web3
from datetime import datetime

from configPkg import dict_of_conv, ethscan_exports_path, token_data_path
from configPkg import FIRST_HOLDER, LAST_HOLDER


def filterDataByHolder(csv_name, outputs, current_balance_str):
    contract_holders = pd.read_csv(ethscan_exports_path + csv_name)
    contract_holders.drop('PendingBalanceUpdate', axis=1, inplace=True)
    contract_holders.sort_values("Balance", ascending=False, inplace=True)
    contract_holders_head = contract_holders[FIRST_HOLDER:LAST_HOLDER]
    contract_holders_head.set_index("HolderAddress", inplace=True)
    contract_holders_head.rename(columns={"Balance": current_balance_str}, inplace=True)
    new_row_sum = pd.Series(data={current_balance_str: contract_holders_head[current_balance_str].sum()}, name='Total Balance')
    contract_holders_head = contract_holders_head.append(new_row_sum)
    contract_holders_head.to_csv(outputs['csv'])
    contract_holders_head.to_json(outputs['json'], orient='index', indent=4)
    
def fecthDatabyHolder(outputs, current_balance_str, contract, web3_provider):
    csv_contract_holders = {}
    csv_contract_holders[current_balance_str] = []
    safe_address = ''
    decimals = contract.functions.decimals().call()
    contract_holders_head = pd.read_csv(outputs['csv'])
    for i,holder in enumerate(contract_holders_head['HolderAddress']):
        if 'Total Balance' in holder:
            break
        safe_address = Web3.toChecksumAddress(holder)
        balance = contract.functions.balanceOf(Web3.toChecksumAddress(safe_address)).call()
        csv_contract_holders[current_balance_str].append(float(web3_provider.fromWei(balance, dict_of_conv['1{}'.format('0'*decimals)])))
        '''print("Holder {} has {} of {}".format(holder,
                                              web3_provider.fromWei(csv_contract_holders['Balance'],
                                                           dict_of_conv['1{}'.format('0'*decimals)]),
                                              symbol))'''
    csv_contract_holders[current_balance_str].append(sum(csv_contract_holders[current_balance_str]))
    print(csv_contract_holders)
    contract_holders_head.set_index("HolderAddress", inplace=True)
    contract_holders_head[current_balance_str] = pd.DataFrame(csv_contract_holders,index=contract_holders_head.index)
    contract_holders_head.to_csv(outputs['csv'])
    contract_holders_head.to_json(outputs['json'], orient='index', indent=4)
    
def createDataForContract(csv_name, web3_provider, abi):
    # Datetime handling
    now = datetime.now()
    current_balance_str = "Balance_{}_{}-{}".format(str(now.date()),now.hour,now.minute)
    
    # Connect to contract
    contract_address = Web3.toChecksumAddress(csv_name.split('-')[-1][:-4]) 
    contract = web3_provider.eth.contract(address=contract_address, abi=abi)
    symbol = contract.functions.symbol().call()
    outputs = {'csv': token_data_path + "Top_{}_Holders.csv".format(symbol),
               'json': token_data_path + "Top_{}_Holders.json".format(symbol)}
    print("Contract address: {}".format(contract_address))
    print("Token: {}".format(contract.functions.name().call()))
    
    # Check if there is an output
    if (os.path.isfile(outputs['csv']) == False and 
       os.path.isfile(outputs['json']) == False):
        # First run
        filterDataByHolder(csv_name, outputs, current_balance_str)
    else:
        # Not first run - take data from blockchain
        fecthDatabyHolder(outputs, current_balance_str, contract, web3_provider)