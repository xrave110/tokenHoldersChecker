# Token Holders Checker

Steps to run:
1. Install necessary librares using **pip3 install -r requirements.txt**
2. Add environment variable representing your infura ID (must have account in **infura.io**) export INFURA_ID={your id}
3. Download csv files (with holders adresses) from **etherscan.io**
4. Put all csv files into the folder **etherscanExports**
5. Run **tokenHoldersChecker.py**
   - number of holders can be manipulated by parameters FIRST_HOLDER and LAST_HOLDER in configPkg.py
7. Outputs will be in folder **tokeData**
