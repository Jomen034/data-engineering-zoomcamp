#!/usr/bin/env python
# coding: utf-8

import os
import argparse
from time import time
import pandas as pd
from sqlalchemy import create_engine

def main(params):
    user = params.user
    password = params.password
    host = params.host 
    port = params.port 
    db = params.db
    table_name = params.table_name
    url = params.url
    
    if url.endswith('.csv.gz'):
        csv_name = 'output.csv.gz'
    else:
        csv_name = 'output.csv'

    print(f"Downloading file from {url}")
    os.system(f"wget {url} -O {csv_name}")
    
    if not os.path.exists(csv_name):
        print(f"Failed to download the file from {url}")
        return

    print(f"Connecting to database postgresql://{user}:*****@{host}:{port}/{db}")
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    try:
        df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000)
        df = next(df_iter)
        
        # Uncomment if dealing with date-time data
        # df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
        # df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)

        print(f"Creating table {table_name} if not exists")
        df.head(0).to_sql(name=table_name, con=engine, if_exists='replace')

        while True:
            try:
                t_start = time()
                df.to_sql(name=table_name, con=engine, if_exists='append')
                t_end = time()

                print(f"Inserted a chunk of data, took {t_end - t_start:.3f} seconds")
                df = next(df_iter)
            
            except StopIteration:
                print("Finished ingesting data into the PostgreSQL database")
                break

    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest CSV data to PostgreSQL')

    parser.add_argument('--user', required=True, help='User name for PostgreSQL')
    parser.add_argument('--password', required=True, help='Password for PostgreSQL')
    parser.add_argument('--host', required=True, help='Host for PostgreSQL')
    parser.add_argument('--port', required=True, help='Port for PostgreSQL')
    parser.add_argument('--db', required=True, help='Database name for PostgreSQL')
    parser.add_argument('--table_name', required=True, help='Name of the table where we will write the results to')
    parser.add_argument('--url', required=True, help='URL of the CSV file')

    args = parser.parse_args()

    main(args)