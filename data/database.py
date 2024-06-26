import sqlalchemy as db
import pandas as pd
from config import DATABASE_URI

def connect(data):
    df = pd.DataFrame(data)
    engine = db.create_engine(DATABASE_URI)
    df.to_sql('arXivPapers', con=engine, if_exists='replace', index=False)
    with engine.connect() as connection:
        query_result = connection.execute(db.text("SELECT title FROM arXivPapers;")).fetchall()
        print(pd.DataFrame(query_result))
