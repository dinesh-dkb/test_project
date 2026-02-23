# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements (if you have one)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY vehicle_telematics.py .

# Default command
CMD ["python", "vehicle_telematics.py"]