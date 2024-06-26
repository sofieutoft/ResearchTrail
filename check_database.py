import sqlalchemy as db
import pandas as pd
from config import DATABASE_URI

# Connect to the database
engine = db.create_engine(DATABASE_URI)

# Function to fetch and print table contents
def check_table(engine):
    with engine.connect() as connection:
        # Execute a query to fetch all data from the table
        query_result = connection.execute(db.text("SELECT * FROM arXivPapers;"))
        rows = query_result.fetchall()
        if rows:
            columns = query_result.keys()
            df = pd.DataFrame(rows, columns=columns)
            print("Table Contents:")
            print(df)
            print("\nColumn Names and Data Types:")
            print(df.dtypes)
        else:
            print("The table arXivPapers is empty.")

# Run the function
check_table(engine)