from fastapi import FastAPI
import cx_Oracle
from config import config

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/execute_query")
async def execute_query(sql: str):
    # Update the connection details according to your Oracle database configuration
    connection = cx_Oracle.connect(
        user= config.oracle_username,
        password= config.oracle_password,
        dsn= config.oracle_dsn
    )

    try:
        cursor = connection.cursor()

        # Execute the SQL query
        cursor.execute(sql)

        # Fetch the result
        result = cursor.fetchall()

        return {"result": result}

    finally:
        # Close the cursor and the database connection
        cursor.close()
        connection.close()
