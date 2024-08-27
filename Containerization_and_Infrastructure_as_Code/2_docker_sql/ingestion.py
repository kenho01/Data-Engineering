import pandas as pd
from sqlalchemy import create_engine
import argparse
import os

def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    database = params.db
    table_name = params.table_name
    url= params.url
    parquet_file = 'output.parquet'

    os.system(f"wget {url} -O {parquet_file}")

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')
    df = pd.read_parquet(parquet_file)
    engine.connect
    df.to_sql(name=table_name, con=engine, if_exists='append')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingesting parquet file to Postgres DB...')

    # Parameters required: 
    # User, Password, Host, Port, Database name, Table name, parquet file
    parser.add_argument('--user',help='Username for postgres database')
    parser.add_argument('--password',help='Password for postgres database')
    parser.add_argument('--host',help='Hostname of postgres database')
    parser.add_argument('--port',help='Port for postgres database')
    parser.add_argument('--db',help='Database name for postgres')
    parser.add_argument('--table_name',help='Name of table to write to on postgres database')
    parser.add_argument('--url',help='Url of the csv file')

    args = parser.parse_args()
    main(args)

