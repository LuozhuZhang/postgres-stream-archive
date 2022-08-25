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
# `address` String,
# `symbol` String,
# `name` String, 
# `decimals` Int64,
# `total_supply` Int8,
class Tokens(Base):

  address = StringField()
  symbol = StringField()
  name = StringField()
  decimals = Int64Field()
  total_supply = Int8Field()

  engine = ReplacingMergeTree(
    primary_key=('address',),
    order_by=('address', 'name'), 
    ver_col='version',
    partition_key=(
      F.intDiv(Base.gmt_insert, 10000000),
    ),
  )
