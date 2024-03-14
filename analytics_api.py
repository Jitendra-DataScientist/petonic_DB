"""
    this script hosts data-api routes
    that are written using FASTAPI
"""
import os
import logging
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
# from db_main import DBMain
import pydantic_check
from gen_ai_analytics import gen_res_write, fetch_gen_usage


# Determine the directory for logs
log_directory = os.path.join(os.getcwd(), 'logs')

# Create the logs directory if it doesn't exist
if not os.path.exists(log_directory):
    os.mkdir(log_directory)

# Configure logging
# logging.basicConfig(
#     filename="logs.log"
#     level=logging.DEBUG,
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#     handlers=[logging.StreamHandler()],
# )

# Create a logger instance
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create a file handler for this script's log file
file_handler = logging.FileHandler(os.path.join(log_directory, "analytics_api.log"))
file_handler.setLevel(logging.DEBUG)  # Set the logging level for this handler

# Create a formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)


# db_main_inst = DBMain()


# Create a FastAPI instance
app = FastAPI()

# Allowing all origins for now
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/analytics/health")
async def health():
    """Route funtion to return health status of analytics-api"""

    return JSONResponse(content={"API_status": "healthy"}, status_code=200)


@app.post("/analytics/gen-ai-apis")
async def gen_log_write(payload: pydantic_check.GenAPIAnalytics):
    """Route function for user login action"""

    # req_body = await payload.json()
    response, status_code = gen_res_write(vars(payload))
    logger.info("Response: %s, Status Code: %s", response, status_code)
    return JSONResponse(content=response, status_code=status_code)


@app.post("/analytics/gen-ai-token-cost")
async def gen_usage_fetch(payload: pydantic_check.GenAITokenCost):
    """Route function for user login action"""

    # req_body = await payload.json()
    response, status_code = fetch_gen_usage(vars(payload))
    logger.info("Response: %s, Status Code: %s", response, status_code)
    return JSONResponse(content=response, status_code=status_code)
