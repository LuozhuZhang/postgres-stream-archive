from sqlalchemy import create_engine, Column, MetaData

from clickhouse_sqlalchemy import make_session, types, engines

import logging

uri = 'clickhouse://default:@localhost/test'

engine = create_engine(uri)
session = make_session(engine)
metadata = MetaData(bind=engine)

from schema.blocks import Blocks

try:
    Blocks.drop()
except Exception:
    pass
Blocks.create()




