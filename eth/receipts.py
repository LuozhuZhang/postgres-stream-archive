from infi.clickhouse_orm import (
  Model,
  Int8Field,
  Int16Field,
  Int64Field,
  StringField, 
  NullableField,
  ReplacingMergeTree, 
  F,
)
from schemas.clickhouse.eth.__constant import PARTITION_STEP
from schemas.clickhouse.base import Base

# Schema of eth_data, remove text after review
# `transaction_hash` String,
# `transaction_index` String,
# `block_hash` String,
# `block_number` Int64,
# `cumulative_gas_used` Int64,
# `gas_used` Int64,
# `contract_address` Nullable(String),
# `root` Nullable(String),
# `status` Int8,
# `effective_gas_price` Int64"
class Receipts(Base):

  transaction_hash = StringField()
  transaction_index = StringField()
  block_hash = StringField()
  block_number = Int64Field()
  cumulative_gas_used = Int64Field()
  gas_used = Int64Field()
  contract_address = NullableField(StringField())
  root = NullableField(StringField())
  status = NullableField(Int8Field())
  effective_gas_price = Int64Field()

  engine = ReplacingMergeTree(
    primary_key=('transaction_hash',),
    order_by=('transaction_hash', 'block_number'), 
    ver_col='version',
    partition_key=(
      F.intDiv(block_number, PARTITION_STEP), 
      F.intDiv(block_number + PARTITION_STEP, PARTITION_STEP)
    ),
  )
