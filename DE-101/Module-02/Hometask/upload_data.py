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

    for name in ('Orders', 'People', 'Returns'):
        df = pd.read_excel(FILE, name)
        df.to_sql(
            name.lower(),
            engine,
            if_exists='replace'
        )


if __name__ == '__main__':
    upload_tables()
