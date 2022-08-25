from infi.clickhouse_orm import (
  Model,
  Int8Field,
  Int16Field,
  Int64Field,
  Int256Field,
  StringField, 
  NullableField,
  DateTimeField,
  ReplacingMergeTree, 
  F,
)
from schemas.clickhouse.eth.__constant import PARTITION_STEP
from schemas.clickhouse.base import Base

# Schema of eth_data, remove text after review
# `transaction_hash` Nullable(String),
# `transaction_index` Nullable(Int64),
# `from_address` Nullable(String),
# `to_address` String,
# `value` Nullable(Int256) ,
# `input` Nullable(String),
# `output` Nullable(String),
# `trace_type` String,
# `call_type` Nullable(String),
# `reward_type` Nullable(String),
# `gas` Nullable(Int64),
# `gas_used` Nullable(Int64),
# `subtraces` Nullable(Int64),
# `trace_address` Nullable(String),
# `error` Nullable(String),
# `status` Int64,
# `block_timestamp` DateTime64(3, 'UTC'),
# `block_number` Int64,
# `block_hash` String,
# `trace_id` String"
class Traces(Base):

  transaction_hash = NullableField(StringField())
  transaction_index = NullableField(Int64Field())
  from_address = NullableField(StringField())
  to_address = NullableField(StringField())
  value = NullableField(Int64Field())
  input = NullableField(StringField())
  output = NullableField(StringField())
  # 我全部采用了Nullable，防止后期数据中出现null
  trace_type = NullableField(StringField())
  call_type = NullableField(StringField())
  reward_type = NullableField(StringField())
  gas = NullableField(Int64Field())
  gas_used = NullableField(Int64Field())
  subtraces = NullableField(Int64Field())
  trace_address = NullableField(StringField())
  error = NullableField(StringField())
  status = Int64Field()
  # 不确定能否传入这个参数
  block_timestamp = DateTimeField(3, 'UTC')
  block_number = Int64Field()
  block_hash = StringField()
  trace_id = StringField()

  engine = ReplacingMergeTree(
    primary_key=('address',),
    order_by=('address', 'block_number'), 
    ver_col='version',
    partition_key=(
      F.intDiv(block_number, PARTITION_STEP), 
      F.intDiv(block_number + PARTITION_STEP, PARTITION_STEP)
    ),
  )
