from sqlalchemy import create_engine, Column, MetaData, literal

from clickhouse_sqlalchemy import Table, make_session, types, engines

uri = 'clickhouse://default:@localhost/test'

engine = create_engine(uri)
metadata = MetaData(bind=engine)

Blocks = Table('blocks', metadata,
    Column('number', types.Int64, primary_key=True),
    Column('parent_hash', types.String),
    Column('nonce', types.String),
    Column('sha3_uncles', types.String),
    Column('logs_bloom', types.String),
    Column('transactions_root', types.String),
    Column('state_root', types.String),
    Column('receipts_root', types.String),
    Column('miner', types.String),
    Column('difficulty', types.Float64),
    Column('total_difficulty', types.Float64),
    Column('size', types.Int64),
    Column('extra_data', types.String),
    Column('gas_limit', types.Int64),
    Column('gas_used', types.Int64),
    Column('timestamp', types.DateTime),
    Column('transaction_count', types.Int64),
    Column('base_fee_per_gas', types.Int64),
    engines.SummingMergeTree(primary_key='number',order_by='number')
)


