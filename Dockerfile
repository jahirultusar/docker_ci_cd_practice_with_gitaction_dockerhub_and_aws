# Base image
FROM python:3.11-alpine

# Directory setup
WORKDIR /app

# copy install dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# copy files
COPY . .

# Run the app
CMD ["python", "app.py"]