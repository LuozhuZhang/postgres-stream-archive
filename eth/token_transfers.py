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
# `token_address` String,
# `from_address` String,
# `to_address` String,
# `value` Int64,
# `transaction_hash` String,
# `log_index` Int8,
# `block_number` Int64"
class TokenTransfers(Base):

  token_address = StringField()
  from_address = StringField()
  to_address = StringField()
  value = Int64Field()
  transaction_hash = StringField()
  log_index = Int8Field()
  block_number = Int64Field()

  engine = ReplacingMergeTree(
    primary_key=('token_address',),
    order_by=('token_address', 'block_number'), 
    ver_col='version',
    partition_key=(
      F.intDiv(block_number, PARTITION_STEP), 
      F.intDiv(block_number + PARTITION_STEP, PARTITION_STEP)
    ),
  )
