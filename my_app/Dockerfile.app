# Use a slim version of Python to reduce image size
FROM python:3.11-slim-bullseye

# App version
LABEL version="2.3.2"

# Set environment variables for Hugging Face model
ENV HF_MODEL_NAME=distilbert-base-uncased-finetuned-sst-2-english \
    MODEL_CACHE=/model_cache \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=/app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Create a non-root user and group
RUN groupadd -g 1000 appgroup && \
    useradd -u 1000 -g appgroup -m appuser

# Copy requirements.txt from root
COPY requirements.txt ./

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy preload script & preload the model
COPY my_app/preload_model.py /tmp/preload_model.py
RUN python /tmp/preload_model.py

# Copy app source code
COPY my_app/ ./my_app/
ENV PYTHONPATH=/app

# Change ownership of the /app directory to the non-root user
RUN chown -R appuser:appgroup /app

# Use non-root user
USER appuser

# Expose Flask and Prometheus ports
EXPOSE 5000
EXPOSE 8000

# Run the application
CMD ["python", "my_app/start_app.py"]
