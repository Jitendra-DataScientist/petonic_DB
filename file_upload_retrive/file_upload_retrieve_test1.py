from fastapi import (
    FastAPI, File, UploadFile, HTTPException, Depends, Form, Body
)
from fastapi.responses import JSONResponse, StreamingResponse
from fastapi.encoders import jsonable_encoder
from fastapi.openapi.utils import get_openapi
from pydantic import BaseModel, ValidationError, AnyHttpUrl
import psycopg2
from psycopg2 import sql, Error
from io import BytesIO
import sys
import os
import logging
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


# Pydantic model for the file upload payload
class FilePayload(BaseModel):
    id: int
    filename: str
    file_data: bytes

# Pydantic model for payload validation
class FileRequest(BaseModel):
    id: int
    filename: str


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
def save_file_to_db(id, filename, file_data):
    insert_query = sql.SQL("INSERT INTO files (id, filename, file_data) VALUES ({}, {}, {})").format(
        sql.Literal(id),
        sql.Literal(filename),
        sql.Literal(file_data),
    )
    cursor.execute(insert_query)
    conn.commit()

# Function to retrieve file from PostgreSQL
def get_file_from_db(id):
    select_query = sql.SQL("SELECT filename, file_data FROM files WHERE id = {}").format(
        sql.Literal(id),
    )
    cursor.execute(select_query)
    result = cursor.fetchone()
    if result:
        filename, file_data = result
        return FilePayload(id=id, filename=filename, file_data=file_data)
    else:
        return None

# FastAPI endpoint for file upload
@app.post("/uploadfile")
async def create_upload_file(id: int = Form(...), file: UploadFile = File(...)):
    try:
        # Read file content
        file_content = await file.read()
        
        # Save file to PostgreSQL
        save_file_to_db(id, file.filename, file_content)

        return {"id": id, "filename": file.filename, "file_size": len(file_content)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# FastAPI endpoint for file retrieval using payload
@app.post("/getfile")
async def read_file(request: FileRequest):
    file_content = get_file_from_db(request.id)
    if file_content is not None:
        return StreamingResponse(BytesIO(file_content.file_data), media_type="application/octet-stream", headers={"Content-Disposition": f"inline; filename={file_content.filename}"})
    else:
        raise HTTPException(status_code=404, detail="File not found")

# Custom endpoint to get OpenAPI schema with examples for Pydantic models
@app.get("/openapi.json")
async def get_open_api_endpoint():
    return JSONResponse(content=jsonable_encoder(get_openapi(title="FastAPI", version="1.0.0", routes=app.routes)), media_type="application/json")
