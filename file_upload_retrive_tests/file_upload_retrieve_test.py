from fastapi import FastAPI, File, UploadFile, HTTPException, Depends, Form
from fastapi.responses import StreamingResponse
import sys
import os
import logging
import psycopg2
from psycopg2 import Error
from psycopg2 import sql
from io import BytesIO
from dotenv import load_dotenv

app = FastAPI()

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()],
)

# Create a logger instance
logger = logging.getLogger(__name__)

dotenv_path = os.path.join(os.getcwd(), ".env")
# below dotenv_path for local test in Downloads folder
# dotenv_path = os.path.join(os.path.expanduser("~"), "Downloads", ".env")
load_dotenv(dotenv_path)

# Database connection parameters
try:
    db_params = {
        "host": os.getenv("host"),
        "database": os.getenv("database"),
        "user": os.getenv("user"),
        "password": os.getenv("password"),
    }
except Error as env_error:
    logger.critical("Failed to read DB params: %s", env_error)
    sys.exit()

# Database connection
conn = psycopg2.connect(**db_params)
cursor = conn.cursor()

# Create a table for storing file data
create_table_query = """
CREATE TABLE IF NOT EXISTS files (
    id SERIAL PRIMARY KEY,
    filename VARCHAR(255),
    file_data BYTEA
);
"""
cursor.execute(create_table_query)
conn.commit()

# Function to save file to PostgreSQL
def save_file_to_db(filename, file_data):
    insert_query = sql.SQL("INSERT INTO files (filename, file_data) VALUES ({}, {})").format(
        sql.Literal(filename),
        sql.Literal(file_data),
    )
    cursor.execute(insert_query)
    conn.commit()

# Function to retrieve file from PostgreSQL
def get_file_from_db(filename):
    select_query = sql.SQL("SELECT file_data FROM files WHERE filename = {}").format(
        sql.Literal(filename),
    )
    cursor.execute(select_query)
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return None

# FastAPI endpoint for file upload
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    try:
        # Read file content
        file_content = await file.read()
        
        # Save file to PostgreSQL
        save_file_to_db(file.filename, file_content)

        return {"filename": file.filename, "file_size": len(file_content)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# FastAPI endpoint for file retrieval using payload
@app.post("/getfile/")
async def read_file(filename: str = Form(...)):
    file_content = get_file_from_db(filename)
    if file_content is not None:
        return StreamingResponse(BytesIO(file_content), media_type="application/octet-stream", headers={"Content-Disposition": f"inline; filename={filename}"})
    else:
        raise HTTPException(status_code=404, detail="File not found")
