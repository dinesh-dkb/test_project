# Dockerfile
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (if it's a web app)
EXPOSE 5000

# Command to run the app
CMD ["python", "test.py"]