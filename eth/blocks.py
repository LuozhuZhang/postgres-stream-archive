# using INT, same as ETL Schema

# Review Attention
# 1. 把UInt换成了Int，参考ETL Schema: https://ethereum-etl.readthedocs.io/en/latest/schema/
# 2. token transfer和transaction的value换成了Int256，防止之后数据量太大溢出
# 3. traces采用了大量 Nullable、另外 DateTimeField(3, 'UTC') 需要确定是否可用
import sys
sys.path.append('../../../../')

from infi.clickhouse_orm import (
  Model,
  Int8Field,      # Int8
  Int16Field,
  Int64Field,     # Int64
  StringField,    # String
  Float64Field,   # Float64
  NullableField,  #  Nullable(xxx)
  ReplacingMergeTree, 
  F,
  DateTimeField
)
from schemas.clickhouse.eth.__constant import PARTITION_STEP
from schemas.clickhouse.base import Base

# ETL Schema: https://ethereum-etl.readthedocs.io/en/latest/schema/
# ORM Schema: https://github.com/Infinidat/infi.clickhouse_orm/blob/develop/docs/field_types.md#field-types

# Schema of eth_data, remove text after review
# `number` Int64,
# `hash` String,
# `parent_hash` String,
# `nonce` String,
# `sha3_uncles` String,
# `logs_bloom` String,
# `transactions_root` String,
# `state_root` String,
# `receipts_root` String,
# `miner` String,
# `difficulty` Float64,
# `total_difficulty` Float64,
# `size` Int64,
# `extra_data` String,
# `gas_limit` Int64,
# `gas_used` Int64,
# `timestamp` Int64,
# `transaction_count` Int64,
# `base_fee_per_gas` Nullable(Int8)"
class Blocks(Base):

  number = Int64Field()
  hash = StringField()
  parent_hash = StringField()
  nonce = StringField()
  sha3_uncles = StringField()
  logs_bloom = StringField()
  transactions_root = StringField()
  state_root = StringField()
  receipts_root = StringField()
  miner = StringField()
  difficulty = Float64Field()
  total_difficulty = Float64Field()
  size = Int64Field()
  extra_data = StringField()
  gas_limit = Int64Field()
  gas_used = Int64Field()
  timestamp = DateTimeField()
  transaction_count = Int64Field()
  base_fee_per_gas = NullableField(Int8Field())
    
  engine = ReplacingMergeTree(
    primary_key=('hash',),
    order_by=('hash', 'number'), 
    ver_col='version',
    partition_key=(
      F.intDiv(number, PARTITION_STEP), 
      F.intDiv(number + PARTITION_STEP, PARTITION_STEP)
    ),
  )

from infi.clickhouse_orm import models, fields, engines
from infi.clickhouse_orm.database import Database


class Person(models.Model):
    
    first_name = fields.StringField()
    last_name = fields.StringField()
    birthday = fields.DateField()
    height = fields.Float32Field()

    engine = engines.MergeTree('birthday', ('first_name', 'last_name', 'birthday'))