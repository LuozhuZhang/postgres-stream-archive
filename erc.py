import sqlUtils
import os

location = os.getcwd()

def main():
    database = "test_eth"
    keys = "`address` String"
    sqlUtils.create_table(database,'erc20',keys,'block_number')
    sqlUtils.create_table(database,'erc721',keys,'block_number')
    

main()