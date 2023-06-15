import logging
from fastapi import FastAPI
import cx_Oracle
from app.config import config
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Get the root logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Create a file handler and set its level to DEBUG
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.DEBUG)

# Create a stream handler and set its level to DEBUG
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)

# Create a formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

# Add the handlers to the root logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)


@app.get("/")
def read_root():
    # Log a debug message
    logger.info("Root endpoint was accessed")

    return {"Hello": "World"}


class Item(BaseModel):
    sql: str


@app.post("/execute_query/")
async def execute_query(item: Item):
    """
    Executes the given SQL query and returns the results.

    Args:
        item: The Item object containing the SQL query.

    Returns:
        The results of the SQL query.
    """

    # Update the connection details according to your Oracle database configuration
    dsn = cx_Oracle.makedsn("localhost", 1521, sid="FREE")
    connection = cx_Oracle.connect(
        user=config.oracle_username,
        password=config.oracle_password,
        dsn=config.oracle_dsn,
    )

    try:
        cursor = connection.cursor()

        # Execute the SQL query
        cursor.execute(item.sql)

        # Fetch the result
        result = cursor.fetchall()

        # Close the cursor and the database connection
        cursor.close()
        connection.close()

        # Return the results
        return result

    except Exception as e:
        # Log the exception
        logger.error(f"An exception occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

