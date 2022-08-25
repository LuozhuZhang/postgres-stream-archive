from infi.clickhouse_orm import (
  Model,
  Int8Field,
  # Int256Field,
  Int64Field,
  StringField, 
  NullableField,
  DateTimeField,
  DecimalField,
  ReplacingMergeTree, 
  F,
)
from schemas.clickhouse.eth.__constant import PARTITION_STEP
from schemas.clickhouse.base import Base

# Schema of eth_data, remove text after review
# `hash` String,
# `nonce` Int8,
# `block_hash` String,
# `block_number` Int64,
# `transaction_index` Int8,
# `from_address` String,
# `to_address` String,
# `value` Int64,
# `gas` Int64,
# `gas_price` Int64,
# `input` String, 
# `block_timestamp` Int64,
# `max_fee_per_gas` Nullable(Int64),
# `max_priority_fee_per_gas` Nullable(Int64),
# `transaction_type` Nullable(Int64)"
class Transactions(Base):

  hash = StringField()
  nonce = Int8Field()
  block_hash = StringField()
  block_number = Int64Field()
  transaction_index = Int8Field()
  from_address = StringField()
  to_address = StringField()
  # 防止未来出现溢出，设置个较大值
  # value = Int256Field()
  value = DecimalField(38,4)
  gas = Int64Field()
  gas_price = Int64Field()
  input = StringField()
  block_timestamp = Int64Field()
  max_fee_per_gas = NullableField(Int64Field())
  max_priority_fee_per_gas = NullableField(Int64Field())
  transaction_type = NullableField(Int64Field())

  engine = ReplacingMergeTree(
    primary_key=('hash',),
    order_by=('hash', 'block_number'), 
    ver_col='version',
    partition_key=(
      F.intDiv(block_number, PARTITION_STEP), 
      F.intDiv(block_number + PARTITION_STEP, PARTITION_STEP)
    ),
  )
