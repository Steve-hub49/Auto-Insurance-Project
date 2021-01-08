import pandas as pd
from sqlalchemy import create_engine

from config import USERNAME, PASSWORD, HOST, PORT, DB 


TABLE_NAME = 'insurance_claims'
df = pd.read_csv('insurance_claims.csv')

# create an engine that can talk to the database
conn_str = f'postgres://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB}'
engine = create_engine(conn_str)
conn = engine.connect()

df.to_sql(TABLE_NAME, engine, if_exists='replace') 
engine.execute(f'ALTER TABLE {TABLE_NAME} ADD PRIMARY KEY (policy_number);')