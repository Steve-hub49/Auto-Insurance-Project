import pandas as pd
from sqlalchemy import create_engine

from config import USERNAME, PASSWORD, HOST, PORT, DB, TABLE_NAME


df = pd.read_csv('insurance_claims.csv')

# create an engine that can talk to the database
conn_str = f'postgres://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB}'
engine = create_engine(conn_str)
conn = engine.connect()

df.to_sql(TABLE_NAME, engine, if_exists='replace') 
# sqlalchemy will not detect table without PK. This seems to be the best solution (https://stackoverflow.com/q/50469391)
engine.execute(f'ALTER TABLE {TABLE_NAME} ADD PRIMARY KEY (policy_number);')