import sqlalchemy as db
import pandas as pd
from config import DATABASE_URI

def connect(data):
    engine = db.create_engine(DATABASE_URI)
    data.to_sql('arXivPapers', con=engine, if_exists='replace', index=False)

def fetch_all_papers(engine):
    with engine.connect() as connection:
        query_result = connection.execute(
            db.text("SELECT title FROM arXivPapers;")).fetchall()
        if query_result:
            return pd.DataFrame(query_result, columns=query_result[0].keys())
        else:
            return pd.DataFrame()
