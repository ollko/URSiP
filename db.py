import os
from typing import Tuple, 
from pathlib import Path
import sqlite3


conn = sqlite3.connect(os.path.join("db", "ursip.db"))
cursor = conn.cursor()


def insert(table: str, column_values: List[Dict]):
    columns = ', '.join( column_values.keys() )
    values = [tuple(column_values.values())]
    placeholders = ", ".join( "?" * len(column_values.keys()) )
    cursor.executemany(
        f"INSERT INTO {table} "
        f"({columns}) "
        f"VALUES ({placeholders})",
        values)
    conn.commit()
