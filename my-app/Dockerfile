# Use Python base image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the Python app
COPY app.py /my-app/app.py

# Install required Python libraries
COPY requirements.txt /my-app/requirements.txt
RUN pip install -r requirements.txt

# Expose the port for Prometheus metrics (if necessary)
EXPOSE 8000

# Run the Python app
CMD ["python", "app.py"]
