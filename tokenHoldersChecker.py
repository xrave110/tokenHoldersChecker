#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 22:07:25 2021

@author: anything
"""
import os
import json
from web3 import Web3
from contractDataApi import createDataForContract
from configPkg import ethscan_exports_path, infura_url

web3_provider = Web3(Web3.HTTPProvider(infura_url))

with open ('//home//anything//Workspace_py//EthDev_py//web3_training//erc20_abi.json') as f:
    abi = json.load(f)

print(os.listdir(ethscan_exports_path))
for csv_name in os.listdir(ethscan_exports_path):
    createDataForContract(csv_name, web3_provider, abi)


    
    