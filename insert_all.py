import sqlUtils
import os

location = os.getcwd()
path = location + '/output'
table_read = os.listdir(path)
database = "test_eth_sum"

# for table in table_read:
#     sql_file = f"{location}/{table}.sql"
#     cmd = f"cd /;cd /Users/foooox/ClickHouse/build/programs/;./clickhouse-client --multiquery <  {sql_file}"
#     print(cmd)
#     cmd = cmd.strip()
#     # print(cmd)
#     sqlUtils.run_cmd(cmd)

for table in table_read:
    txt_file = f"{location}/{table}.txt"
    print(txt_file)
    f = open(txt_file)               # 返回一个文件对象 
    line = f.readline()               # 调用文件的 readline()方法 
    while line: 
        # print(line)              # 后面跟 ',' 将忽略换行符 
        print(line, end = '')
        cmd = '''cd /;cd /Users/foooox/ClickHouse/build/programs/;./clickhouse-client -q "{}"'''.format(line)
        cmd = cmd.strip()
        # print(cmd)
        sqlUtils.run_cmd(cmd)
        line = f.readline()

    f.close()