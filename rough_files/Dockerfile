FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

# Install system-level dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    apt-utils \
    tzdata \
    uvicorn \
    python3-pip \
    nano && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Reset the environment variable
ENV DEBIAN_FRONTEND=dialog

# Create a non-root user
RUN useradd -m myuser
USER myuser

# Set the working directory inside the container
WORKDIR /app

# Copy the FastAPI application code into the container
COPY ./ /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Upgrade pip and suppress warning about script location
RUN pip install --upgrade pip --no-warn-script-location

# Command to run the application
CMD ["uvicorn", "index:app", "--host", "0.0.0.0", "--port", "8000"]
