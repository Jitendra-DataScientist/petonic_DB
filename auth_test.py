"""authentication test script for FASTAPI routes"""
import os
import logging
from dotenv import load_dotenv
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import APIKeyHeader
from fastapi.responses import JSONResponse

dotenv_path = os.path.join(os.getcwd(), ".env")
load_dotenv(dotenv_path)


# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()],
)

# Create a logger instance
logger = logging.getLogger(__name__)

# API key header
api_key_header = APIKeyHeader(name="Authorization")

# Function to validate the API key
async def get_api_key(api_key: str = Depends(api_key_header)):
    """
    Validates the provided API key for authentication.

    Parameters:
    - api_key (str): The API key passed in the 'Authorization' header.

    Returns:
    - str: The validated API key if authentication is successful.

    Raises:
    - HTTPException: 401 Unauthorized if the API key is invalid or not provided.
    """
    expected_api_key = os.getenv("data_api_auth")
    if api_key == expected_api_key:    #pylint: disable=no-else-return
        return []
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key",
            headers={"WWW-Authenticate": "Bearer"},
        )

app = FastAPI()

# Secure the endpoints using the get_api_key dependency
@app.get("/test/health", dependencies=[Depends(get_api_key)])
async def health():
    """Route funtion to return health status of data-api"""
    return JSONResponse(content={"API_status": "healthy"}, status_code=200)
