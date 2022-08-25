from clickhouse_driver import Client
import os

location = os.getcwd()

client = Client(host='localhost')

def run_cmd(cmd):
      return os.system(cmd)

def show_database():
    res = client.execute('SHOW DATABASES')
    print(res)

def create_databse(database):
    s = f"CREATE DATABASE IF NOT EXISTS {database}"
    res = client.execute(s)
    print(res)

def create_table(database,table,keys,orders):
    s = f"CREATE TABLE IF NOT EXISTS {database}.{table} ({keys}) ENGINE = MergeTree ORDER BY {orders}"
    res = client.execute(s)
    print(res)

def create_table_summing_merge(database,table,keys,primary_key,orders):
    s = f"CREATE TABLE IF NOT EXISTS {database}.{table} ({keys}) ENGINE = SummingMergeTree PRIMARY KEY {primary_key} ORDER BY ({orders})"
    res = client.execute(s)
    print(res)

def create_table_replacing_merge(database,table,keys,orders):
    s = f"CREATE TABLE IF NOT EXISTS {database}.{table} ({keys}) ENGINE = ReplacingMergeTree ORDER BY ({orders})"
    res = client.execute(s)
    print(res)

def insert(database,table,file):
    cmd = '''cd /;cd /Users/foooox/ClickHouse/build/programs/;./clickhouse-client -q "INSERT INTO {}.{} FROM INFILE '{}' FORMAT CSVWithNames;"'''.format(database,table,file)
    cmd = cmd.strip()
    # print(cmd)
    run_cmd(cmd)

def select(database,table,limit=10):
    s = f"SELECT * FROM {database}.{table} LIMIT {limit}"
    res = client.execute(s)
    print(res)

def optimize(database,table):
    s = f"OPTIMIZE TABLE {database}.{table} FINAL"
    res = client.execute(s)
    print(res)

