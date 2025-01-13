# Use a slim version of Python to reduce image size
FROM python:3.11-slim-buster

# App version
LABEL version="1.0.0"

# Install necessary system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Create a non-root user and group
RUN groupadd -g 1000 appgroup && \
    useradd -u 1000 -g appgroup -m appuser

# Copy requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt --upgrade pip

# Preload Hugging Face models to avoid downloading on startup
RUN python -c "from transformers import AutoModelForSequenceClassification, AutoTokenizer; \
    AutoModelForSequenceClassification.from_pretrained('distilbert-base-uncased-finetuned-sst-2-english'); \
    AutoTokenizer.from_pretrained('distilbert-base-uncased-finetuned-sst-2-english')"

# Copy only the application code explicitly
COPY my_app/ ./my_app/

# Change ownership of the /app directory to the non-root user
RUN chown -R appuser:appgroup /app

# Switch to the non-root user
USER appuser

# Expose necessary ports for Flask (5000) and Prometheus metrics (8000)
EXPOSE 5000
EXPOSE 8000

# Run the application (starting both Prometheus and Gunicorn from Python)
CMD ["python", "my_app/start_app.py"]
