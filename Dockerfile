# Base image
FROM python:3.11-alpine

# Install curl so the HEALTHCHECK can work
RUN apk add --no-cache curl

# Directory setup
WORKDIR /app

# copy install dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# copy files
COPY . .

# This will ping the container every 30 sec to check health
HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost:5001/health || exit 1

# Arguments passed during build 
ARG GIT_HASH
ARG BUILD_TIME

# Convert them to Environment Variables
ENV GIT_HASH=$GIT_HASH
ENV BUILD_TIME=$BUILD_TIME

# Run the app
CMD ["python", "app.py"]