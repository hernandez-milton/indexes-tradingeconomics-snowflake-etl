#librerias
import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO

def data_processing(url, headers):
    """Extraer datos de tradingeconomics y procesarlos."""
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    tables = soup.find_all('table')

    dfs = []
    for i, table in enumerate(tables):
        table_io = StringIO(str(table))
        df = pd.read_html(table_io)[0]
        df = df.dropna(axis=1, how="all")
        region = df.columns[0]
        df['region'] = region
        df['CREATED_AT'] = pd.to_datetime('today').strftime('%Y-%m-%d')
        df = df.rename(columns={df.columns[0]: 'INDEXES', 
                                df.columns[3]: 'PERCENT'})
        dfs.append(df)
        
    return pd.concat(dfs, ignore_index=True)

