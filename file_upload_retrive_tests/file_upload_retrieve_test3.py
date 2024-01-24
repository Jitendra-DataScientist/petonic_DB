from fastapi import FastAPI, File, UploadFile, HTTPException, Depends, Form
from fastapi.responses import StreamingResponse, JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.openapi.models import HTTPBase
from fastapi.openapi.utils import get_openapi
from pydantic import BaseModel, ValidationError, AnyHttpUrl
import psycopg2
from psycopg2 import sql, Error, Binary
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
class FileRequest(BaseModel):
    pk: str  # Primary key provided in the payload
    filename: str

# Pydantic model for the file retrieval payload
class FilePayload(BaseModel):
    pk: str  # Primary key provided in the payload
    filename: str
    file_data: bytes  # Add this line to include the file_data attribute


# Create a table for storing file data
create_table_query = """
CREATE TABLE IF NOT EXISTS files (
    pk VARCHAR PRIMARY KEY,
    filename VARCHAR(255),
    file_data BYTEA
);
"""
cursor.execute(create_table_query)
conn.commit()

# Function to save file to PostgreSQL
def save_file_to_db(pk, filename, file_data):
    insert_query = sql.SQL("INSERT INTO files (pk, filename, file_data) VALUES (%s, %s, %s)")
    cursor.execute(insert_query, (pk, filename, Binary(file_data)))
    conn.commit()

# Function to retrieve file from PostgreSQL
def get_file_from_db(pk):
    select_query = sql.SQL("SELECT filename, file_data FROM files WHERE pk = %s")
    cursor.execute(select_query, (pk,))
    result = cursor.fetchone()
    if result:
        filename, file_data = result
        return FilePayload(pk=pk, filename=filename, file_data=bytes(file_data))
    else:
        return None

# FastAPI endpoint for file upload
@app.post("/uploadfile")
async def create_upload_file(pk: str = Form(...), file: UploadFile = File(...)):
    try:
        # Read file content
        file_content = await file.read()
        
        # Save file to PostgreSQL
        save_file_to_db(pk, file.filename, file_content)

        return {"pk": pk, "filename": file.filename, "file_size": len(file_content)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# FastAPI endpoint for file retrieval using payload
@app.post("/getfile")
async def read_file(request: FilePayload):
    file_content = get_file_from_db(request.pk)
    if file_content is not None:
        return StreamingResponse(BytesIO(file_content.file_data), media_type="application/octet-stream", headers={"Content-Disposition": f"inline; filename={file_content.filename}"})
    else:
        raise HTTPException(status_code=404, detail="File not found")


# Custom endpoint to get OpenAPI schema with examples for Pydantic models
@app.get("/openapi.json")
async def get_open_api_endpoint():
    return JSONResponse(content=jsonable_encoder(get_openapi(title="FastAPI", version="1.0.0", routes=app.routes)), media_type="application/json")
