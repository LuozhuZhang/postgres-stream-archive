import sqlUtils
import os

location = os.getcwd()
path = location + '/output'
table_read = os.listdir(path)
database = "test_eth_sum"

print(table_read)

for table in table_read:
    sqlUtils.optimize(database,table)