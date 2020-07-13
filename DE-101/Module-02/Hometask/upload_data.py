import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path


DATAFILE = (
    Path(__file__).parent.parent.parent
    / 'Module-01'
    / 'Lab'
    / 'Sample - Superstore.xls'
)
DATABASECONN = (
    Path(__file__).parent.parent.parent.parent.parent
    / 'database.txt'
)


def upload_tables():
    with DATABASECONN.open() as database_conn:
        engine = create_engine(database_conn.read())

    orders = pd.read_excel(DATAFILE, 'Orders')
    orders = (
        orders
        .rename(
            columns=lambda x:
            x.lower()
            .replace(' ', '_')
            .replace('-', '_')
        )
        .set_index('row_id')
    )
    orders.to_sql(
        'orders',
        con=engine,
        schema='stg',
        if_exists='append',
    )


if __name__ == '__main__':
    upload_tables()
