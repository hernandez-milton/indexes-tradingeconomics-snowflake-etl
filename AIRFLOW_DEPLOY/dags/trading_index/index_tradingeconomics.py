import os
import json
import time
import random
import logging
from datetime import datetime, timedelta
import pandas as pd
import airflow
from airflow import models
from airflow.models import DAG, Variable
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
import snowflake.connector as sf  # Conector nativo de Python
from airflow.providers.snowflake.hooks.snowflake import SnowflakeHook
from airflow.providers.snowflake.operators.snowflake import SQLExecuteQueryOperator
from utils_index import data_processing



default_arguments = {   'owner': 'mhernandez',
                        'email': 'mhernandez@gmail.com',
                        'retries':1 ,
                        'retry_delay':timedelta(minutes=2)}

with DAG('TRADING_ECONOMICS',
         default_args=default_arguments,
         description='Extracting Data Trading Economics' ,
         start_date = datetime(2025, 7, 29),
         schedule = None,
         tags=['index_tradingeconomics'],
         catchup=False) as dag :

        params_info = Variable.get("feature_info_trading", deserialize_json=True)
        df = pd.read_csv('/opt/airflow/local/trading/df_index.csv')

        def extract_info(df):
            url = df.loc[0, "url"]
            headers = json.loads(df.loc[0, "headers"])
            df_data = data_processing(url, headers)

            df_data.to_csv('/opt/airflow/local/trading/indexes_tradingeconomics.csv', index=False)   

        #tarea para extracion de datos
        extract_data = PythonOperator(
                                    task_id='EXTRACT_TRADING_ECONOMICS_DATA',
                                    python_callable=extract_info,
                                    op_kwargs={"df": df}
        )

        #tarea para carga de datos al stage
        upload_stage = SQLExecuteQueryOperator(
                task_id='UPLOAD_STAGE_TRADING_DATA',
                conn_id='connection_snowflake_trading', #conexión de Snowflake aquí
                sql='./queries/upload_stage_tradingeconomics.sql',
                hook_params={
                      "warehouse": params_info["DWH"],
                      "database": params_info["DB"],
                      "role": params_info["ROLE"],
                      "schema": params_info["SCHEMA"]
                },
                params=params_info
        )

        #tarea para carga de datos a la tabla
        ingest_data = SQLExecuteQueryOperator(
                task_id='INGEST_TABLE_TRADING_DATA',
                conn_id='connection_snowflake_trading',  #conexión de Snowflake aquí
                sql='./queries/ingest_table_tradingeconomics.sql',
                hook_params={
                      "warehouse": params_info["DWH"],
                      "database": params_info["DB"],
                      "role": params_info["ROLE"],
                      "schema": params_info["SCHEMA"]
                },
                params=params_info
        )

        extract_data >> upload_stage >> ingest_data

