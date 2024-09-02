from fastapi import FastAPI, HTTPException
from app.logger.logger import get_logger
import cx_Oracle
from app.config import config
from pydantic import BaseModel

app = FastAPI()
logger = get_logger(__name__)

# Root endpoint
@app.get("/")
def read_root():
    logger.info("Root endpoint was accessed")
    return {"Hello": "World"}

# Model for handling Oracle SQL queries
class Oracle_IO_Model(BaseModel):
    sql: str

@app.post("/oracle_query/")
async def oracle_query(data_model: Oracle_IO_Model):
    # Update the connection details according to your Oracle database configuration
    new_dsn = cx_Oracle.makedsn(config.oracle_hostname, config.oracle_port, service_name=config.oracle_service_name)
    
    # Establish a connection to the Oracle database
    try:
        connection = cx_Oracle.connect(user=config.oracle_username, password=config.oracle_password, dsn=new_dsn)
        cursor = connection.cursor()
        cursor.execute(data_model.sql)
        result = cursor.fetchall()
    except Exception as e:
        # Log the exception and return an error response
        logger.error(f"An exception occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        # Ensure that the cursor and connection are closed
        if cursor:
            cursor.close()
        if connection:
            connection.close()

    return result

if __name__ == '__main__':
    logger.info('Starting APP')
