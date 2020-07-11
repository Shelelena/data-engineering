import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path


FILE = (
    Path(__file__).parent.parent.parent
    / 'Module-01'
    / 'Lab'
    / 'Sample - Superstore.xls'
)
DATABASE = 'postgresql://dummy:dummy@localhost:5432/dummy'


def upload_tables():
    engine = create_engine(DATABASE)

    orders = pd.read_excel(FILE, 'Orders')
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
        engine,
        if_exists='append',
    )


if __name__ == '__main__':
    upload_tables()
