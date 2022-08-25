import sqlUtils
import os

location = os.getcwd()

def main():
    database = 'eth'
    sqlUtils.create_databse(database)
    sqlUtils.show_database()

    #bloks
    table = "blocks"
    keys = "`number` UInt64,`hash` String,`parent_hash` String,`nonce` String,`sha3_uncles` String,`logs_bloom` String,`transactions_root` String,`state_root` String,`receipts_root` String,`miner` String,`difficulty` Float64,`total_difficulty` Float64,`size` UInt64,`extra_data` String,`gas_limit` UInt64,`gas_used` UInt64,`timestamp` UInt64,`transaction_count` UInt64,`base_fee_per_gas` Nullable(UInt8)"
    # sqlUtils.create_table(database,table,keys,'timestamp')
    sqlUtils.create_table_summing_merge(database,table,keys,'number','number')
    # sqlUtils.insert(database,table,location+"/output/blocks/start_block=00000000/end_block=00299999/blocks_00000000_00299999.csv")
    # sqlUtils.insert(database,'blocks',location+"/output/blocks/start_block=00300000/end_block=00499999/blocks_00300000_00499999.csv")

    #transactions
    table = "transactions"
    keys = "`hash` String,`nonce` UInt8,`block_hash` String, `block_number` UInt64,`transaction_index` UInt8,`from_address` String,`to_address` String,`value` UInt256,`gas` UInt64,`gas_price` UInt64,`input` String, `block_timestamp` UInt64,`max_fee_per_gas` Nullable(UInt64),`max_priority_fee_per_gas` Nullable(UInt64),`transaction_type` Nullable(UInt64)"
    # sqlUtils.create_table(database,table,keys,'block_timestamp')
    sqlUtils.create_table_summing_merge(database,table,keys,'block_number','block_number,transaction_index')
    # sqlUtils.insert(database,table,location+"/output/transactions/start_block=00000000/end_block=00299999/transactions_00000000_00299999.csv")
    # sqlUtils.insert(database,table,location+"/output/transactions/start_block=00300000/end_block=00499999/transactions_00300000_00499999.csv")

    # token_transfers
    table = "token_transfers"
    keys = "`token_address` String,`from_address` String,`to_address` String,`value` Int64,`transaction_hash` String,`log_index` UInt64,`block_number` UInt64"
    # sqlUtils.create_table(database,table,keys,'block_number')
    sqlUtils.create_table_summing_merge(database,table,keys,'block_number','block_number,log_index')
    # sqlUtils.insert(database,table,location+"/output/token_transfers/start_block=00300000/end_block=00499999/token_transfers_00300000_00499999.csv")

    # # traces
    # table = "traces"
    # keys = "`transaction_hash` Nullable(String),`transaction_index` Nullable(Int64),`from_address` Nullable(String),`to_address` String,`value` Nullable(Int256) ,`input` Nullable(String),`output` Nullable(String),`trace_type` String,`call_type` Nullable(String),`reward_type` Nullable(String),`gas` Nullable(Int64),`gas_used` Nullable(Int64),`subtraces` Nullable(Int64),`trace_address` Nullable(String),`error` Nullable(String),`status` Int64,`block_timestamp` DateTime64(3, 'UTC'),`block_number` Int64,`block_hash` String,`trace_id` String"
    # # sqlUtils.create_table(database,table,keys,'block_timestamp')
    # sqlUtils.create_table_summing_merge(database,table,keys,'block_number','block_number,transaction_index')
    # # sqlUtils.insert(database,table,location+"/output/traces/traces1.csv")

    # tokens
    table = "tokens"
    keys = "`address` String,`symbol` String,`name` String, `decimals` UInt64,`total_supply` UInt64,`block_number` UInt64"
    # sqlUtils.create_table(database,table,keys,'block_number')
    sqlUtils.create_table_summing_merge(database,table,keys,'block_number','block_number,address')
    # sqlUtils.insert(database,table,location+"/output/tokens/start_block=00300000/end_block=00499999/tokens_00300000_00499999.csv")

    #receipts
    table = 'receipts'
    keys = "`transaction_hash` String,`transaction_index` Nullable(Int64),`block_hash` String,`block_number` UInt64,`cumulative_gas_used` UInt64,`gas_used` UInt64,`contract_address` Nullable(String),`root` Nullable(String),`status` UInt8,`effective_gas_price` Float64"
    # sqlUtils.create_table(database,table,keys,'block_number')
    sqlUtils.create_table_summing_merge(database,table,keys,'block_number','block_number,transaction_index')
    # sqlUtils.insert(database,table,location+"/output/receipts/start_block=00000000/end_block=00299999/receipts_00000000_00299999.csv")
    # sqlUtils.insert(database,table,location+"/output/receipts/start_block=00300000/end_block=00499999/receipts_00300000_00499999.csv")

    #contracts
    table = 'contracts'
    keys = "`address` String,`bytecode` String,`function_sighashes` String,`is_erc20` String,`is_erc721` String,`block_number` UInt64"
    # sqlUtils.create_table(database,table,keys,'block_number')
    sqlUtils.create_table_replacing_merge(database,table,keys,'block_number,address')
    # sqlUtils.create_table_summing_merge(database,table,keys,'block_number','')
    # sqlUtils.insert(database,table,location+"/output/contracts/start_block=00000000/end_block=00299999/contracts_00000000_00299999.csv")
    # sqlUtils.insert(database,table,location+"/output/contracts/start_block=00300000/end_block=00499999/contracts_00300000_00499999.csv")

    #log
    table = 'logs'
    keys = "`log_index` UInt64,`transaction_hash` String,`transaction_index` UInt64,`block_hash` String,`block_number` UInt64,`address` String, `data` String, `topics` String"
    # sqlUtils.create_table(database,table,keys,'block_number')
    sqlUtils.create_table_replacing_merge(database,table,keys,'block_number,log_index')
    

    

main()