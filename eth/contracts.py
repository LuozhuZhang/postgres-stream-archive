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

# TODO: Discuss using name Contract or Contracts
# using Contracts as name, same as ETL output files

# Schema of eth_data, remove text after review
# `address` String,
# `bytecode` String,
# `function_sighashes` String,
# `is_erc20` String,
# `is_erc721` String,
# `block_number` Int64"
class Contracts(Base):

  address = StringField() # string
  bytecode = StringField()
  function_sighashes = StringField()
  is_erc20 = StringField()
  is_erc721 = StringField()
  block_number = Int64Field() # Int64

  engine = ReplacingMergeTree(
    primary_key=('address',),
    order_by=('address', 'block_number'), 
    ver_col='version',
    partition_key=(
      F.intDiv(block_number, PARTITION_STEP), 
      F.intDiv(block_number + PARTITION_STEP, PARTITION_STEP)
    ),
  )
