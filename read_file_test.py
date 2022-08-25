import os

location = os.getcwd()
path = location + '/output'
database = "test_eth_sum"

def check_if_dir(file_path):
    temp_list = os.listdir(file_path)    #put file name from file_path in temp_list
    for i in temp_list:
        if(i == ".DS_Store"):
            temp_list.remove(i)
        else:
            continue  #.DS_Store 是Mac下的特殊文件 用于存储目录的自定义属性（不可见）要删掉
    if os.path.isfile(file_path + '/' + temp_list[0]):    #此处直接判断list中第一项是不是文件
        for temp_list_each in temp_list:
            temp_path = file_path + '/' + temp_list_each
            if os.path.splitext(temp_path)[-1] == '.csv' and os.path.getsize(temp_path) > 0:
                path_read.append(temp_path)
            else:
                continue
    else:
        for temp_list_each in temp_list:
            check_if_dir(file_path + '/' + temp_list_each)    #loop traversal

table_read = os.listdir(path)

# for table in table_read:
#     path_read = []
#     path_each = path + "/" + table
#     check_if_dir(path_each)
#     # print(path_read)
#     file_name = table + ".txt"
#     with open(file_name,'w') as f:
#         for p in path_read:
#             sql_command = f"INSERT INTO {database}.{table} FROM INFILE '{p}' FORMAT CSVWithNames;\n"
#             # print(sql_command)
#             f.writelines(sql_command)

#     os.rename(f"{table}.txt",f"{table}.sql")

for table in table_read:
    path_read = []
    path_each = path + "/" + table
    check_if_dir(path_each)
    # print(path_read)
    file_name = table + ".txt"
    with open(file_name,'w') as f:
        for p in path_read:
            sql_command = f"INSERT INTO {database}.{table} FROM INFILE '{p}' FORMAT CSVWithNames;\n"
            # print(sql_command)
            f.writelines(sql_command)
    # os.rename(f"{table}.txt",f"{table}.sql")

