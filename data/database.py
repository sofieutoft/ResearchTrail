import sqlalchemy as db
import pandas as pd
from config import DATABASE_URI

def connect(data):
    engine = db.create_engine(DATABASE_URI)
    data.to_sql('arXivPapers', con=engine, if_exists='replace', index=False)

def fetch_all_papers(engine):
    with engine.connect() as connection:
        query_result = connection.execute(db.text("SELECT * FROM arXivPapers;"))
        rows = query_result.fetchall()
        if rows:
            columns = query_result.keys()
            return pd.DataFrame(rows, columns=columns)
        else:
            return pd.DataFrame()