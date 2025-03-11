# Use a base image with Python
FROM python:3.8

# Set the working directory
WORKDIR /app

# Copy application files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir flask psycopg2 redis

# Expose port 5000
EXPOSE 5000

# Run the Flask application
CMD ["python", "flask_app.py"]
