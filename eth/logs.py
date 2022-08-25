from infi.clickhouse_orm import (
  Model,
  Int16Field,
  Int64Field,
  StringField, 
  ReplacingMergeTree, 
  F,
)
from schemas.clickhouse.eth.__constant import PARTITION_STEP
from schemas.clickhouse.base import Base

# Schema of eth_data, remove text after review
# `log_index` Int64,
# `transaction_hash` String,
# `transaction_index` Int64,
# `block_hash` String,
# `block_number` Int64,
# `address` String, 
# `data` String, 
# `topics` String"
class Logs(Base):

  log_index = Int64Field()
  transaction_hash = StringField()
  transaction_index = Int64Field()
  block_hash = StringField()
  block_number = Int64Field()
  address = StringField()
  data = StringField()
  topics = StringField()

  engine = ReplacingMergeTree(
    primary_key=('transaction_hash',),
    order_by=('transaction_hash', 'block_number'), 
    ver_col='version',
    partition_key=(
      F.intDiv(block_number, PARTITION_STEP), 
      F.intDiv(block_number + PARTITION_STEP, PARTITION_STEP)
    ),
  )
