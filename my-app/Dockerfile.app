# Use a lighter Python image for better performance
FROM python:3.11-slim-buster

# Set the working directory
WORKDIR /my-app

# Copy the requirements file first to leverage Docker's layer caching
COPY requirements.txt /my-app/requirements.txt

# Install dependencies
# We use the `--no-cache-dir` flag to prevent pip from storing the package files in a cache directory,
# which can save disk space and reduce the size of the Docker image.
# The `-r` flag tells pip to read the list of dependencies from the `requirements.txt` file.
RUN pip install --no-cache-dir -r requirements.txt

# Now copy the application code
COPY app.py /my-app/app.py

# Expose the port for Prometheus metrics
EXPOSE 5000

# Run the Python app
CMD ["python", "app.py"]
