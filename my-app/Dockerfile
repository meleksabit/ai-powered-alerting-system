# Use a lighter Python image for better performance
FROM python:3.9-slim-buster

# Set the working directory
WORKDIR /my-app

# Copy the requirements file first to leverage Docker's layer caching
COPY requirements.txt /my-app/requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Now copy the application code
COPY app.py /my-app/app.py

# Expose the port for Prometheus metrics
EXPOSE 8000

# Run the Python app
CMD ["python", "app.py"]
