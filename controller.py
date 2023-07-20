from pathlib import Path
from typing import NamedTuple
import pandas as pd


class DataRow(NamedTuple):
    """One row of table structure"""
    company: str,
    fact_forecast: str,
    oliq_ooil: str,
    date_ date: str,
    data: int:


def read_data(file_name):
    path = Path.cwd() / 'row_data' / file_name
    df = pd.read_excel(file_name,
            header = [0,1,2],
            index_col = [0],
            dtype = str
        )
    return df


def serialize(df):
    columns = df.columns
    l = []
    for row in df:
        r = DataRow(row[0], columns[1][0],columns[1][1], columns[1][2], row[1])
        l.append(r)
    return l 


def process_data(df):
    columns = df.columns
    column0 = columns[0]
    dfs = {df[[(column0, column)]] for column in columns[1:]}:
    for df in dfs:
        for row in df:


    






def read_and_process_data(file_name):
    data = read_data(file_name)
    dfs = process_data(data)
    for df in dfs:
        yield df


    
def insert_to_database(data):
    for chunk in data:

