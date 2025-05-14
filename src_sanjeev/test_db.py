
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

engine = create_engine('sqlite:///../output/sanjeev_data.db')

# Pull data from the database and execute a SELECT query
with engine.connect() as connection:
    result = connection.execute(sqlalchemy.text("SELECT * FROM train"))  # Replace 'your_table_name' with your actual table name
    res = result.fetchall()

# Convert the result to a pandas DataFrame for easier manipulation
df = pd.DataFrame(res, columns=result.keys())

print(df)