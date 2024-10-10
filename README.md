# $\color{SeaGreen}{AI-Powered\ Alerting\ System:}$ $\color{OrangeRed}{Critical\ Alerts\ Only}$

This repository implements an AI-powered alerting system that uses a **Hugging Face BERT model** to classify and prioritize log alerts based on severity, specifically notifying only for **critical alerts**. The system integrates with **Prometheus** for metrics collection and **Grafana** for visualization and alerting, and is built with **Python** for log processing.

## Table of Contents
- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Docker-Related Files](#docker-related-files)
- [Configuration](#configuration)
- [Usage](#usage)
- [Testing and Alerts](#testing-and-alerts)
- [Prometheus and Grafana Setup](#prometheus-and-grafana-setup)
- [Demo](#demo)

## Introduction

This project demonstrates how to classify log events using **Hugging Face's BERT model** to filter critical log messages and trigger alerts only when critical issues arise. **Prometheus** is used to scrape the log metrics, and **Grafana** is used for visualization and alert notifications. This approach reduces noise by ensuring that only critical logs are flagged and alerted.

### Core Components:
- **Hugging Face BERT Model**: Classifies logs based on severity.
- **Python Logging**: For generating log events.
- **Prometheus**: Collects log metrics for monitoring.
- **Grafana**: Visualizes log metrics and triggers alerts for critical events.

## Prerequisites

Before starting, make sure you have the following tools installed:

- **Python 3.8+**: The application is built using Python.
- **Prometheus**: For metrics collection.
- **Grafana**: For data visualization and alerting.
- **Docker** (Optional but recommended): To run Prometheus and Grafana easily.
- **Pip**: For managing Python packages.

### Python Dependencies

You'll also need to install the following Python libraries:

- **transformers**: For Hugging Face BERT model.
- **prometheus-client**: For exposing log metrics to Prometheus.
- **requests**: For sending Slack notifications (optional).
- **smtplib**: For sending email notifications (optional).

## Project Structure

Here’s the structure of the project:

```bash
.
├── docker-compose.yml
├── LICENSE
├── my-app
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── prometheus-grafana
│   ├── Dockerfile
│   └── prometheus.yml
└── README.md
```	

## Installation

### Step 1: Clone the repository
```bash
git clone https://github.com/meleksabit/ai-powered-alerting-system.git
cd ai-powered-alerting-system
```

### Step 2: Install Python dependencies(if you choose **Manual Installation**, without using **Docker** or **Docker Compose**)
Install the required Python libraries using pip:

```bash
pip install -r my-app/requirements.txt
```

### Step 3: Install and set up Prometheus and Grafana
You can run the application using Docker or Docker Compose.

#### Option 1: Using Docker Compose (Recommended)
This will set up both the Python app, Prometheus, and Grafana services in containers.

Run the following command to start the services:

```bash
docker-compose up --build
```
* **`docker-compose up`**: Starts the services based on the **`docker-compose.yml`** file.
* **`--build`**: Forces **Docker** to rebuild the images even if nothing has changed. You can skip  **`--build`** for subsequent runs if no changes are made to the Dockerfiles or dependencies.

The services will be available at:

**Prometheus** on **`http://localhost:9090`**
**Grafana** on **`http://localhost:3000`**
* **Python app** (exposing metrics) on **`http://localhost:8000/metrics`**

#### Option 2: Manual Installation
You can also manually install Prometheus and Grafana on your local machine. Follow the links below for instructions:
* [Install Prometheus](https://prometheus.io/docs/introduction/first_steps/)
* [Install Grafana](https://grafana.com/grafana/download)

## Docker-Related Files
### Dockerfile for the Python App
```dockerfile
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
```

### Dockerfile for Prometheus & Grafana
```dockerfile
# Use Chainguard's secure Prometheus image
FROM cgr.dev/chainguard/prometheus:latest as prometheus

# Use Chainguard's secure Grafana image
FROM cgr.dev/chainguard/grafana:latest as grafana

# Create necessary directories for Prometheus and Grafana
RUN mkdir -p /etc/prometheus/data /etc/prometheus/conf

# Copy Prometheus configuration
COPY prometheus.yml /etc/prometheus/prometheus.yml

# Expose Prometheus and Grafana ports
EXPOSE 9090 3000

# Create a script to run both services
RUN echo "#!/bin/bash\n\
    prometheus --config.file=/etc/prometheus/prometheus.yml --storage.tsdb.path=/etc/prometheus/data &\n\
    grafana-server --homepath /usr/share/grafana --config /etc/grafana/grafana.ini\n" > /run_services.sh \
    && chmod +x /run_services.sh

# Set entrypoint to run Prometheus and Grafana
ENTRYPOINT ["/bin/bash", "/run_services.sh"]
```

### Docker Compose File
Here’s the **`docker-compose.yml`** that sets up both **Prometheus**, **Grafana**, and the **Python app**:

```yaml
version: '3.8'
services:
  prometheus-grafana:
    build:
      context: ./prometheus-grafana
      dockerfile: Dockerfile
    ports:
      - "9090:9090"   # Prometheus
      - "3000:3000"   # Grafana
    volumes:
      - ./prometheus-grafana/prometheus.yml:/etc/prometheus/prometheus.yml

  python-app:
    build:
      context: ./my-app
      dockerfile: Dockerfile
    ports:
      - "8000:8000"   # Python app (Prometheus metrics)
    depends_on:
      - prometheus-grafana
```

## Configuration
### Step 4: Prometheus Configuration
Edit the **`prometheus-grafana/prometheus.yml`** file to add a scrape config for your Python app that exposes metrics on **`localhost:8000`**:

```yaml
# prometheus.yml
scrape_configs:
  - job_name: 'python_logging'
    static_configs:
      - targets: ['localhost:8000']
```
Prometheus will scrape metrics from **`localhost:8000`**, where your Python app exposes log severity metrics.

### Step 5: Hugging Face BERT Model Setup
In the **`my-app/app.py file`**, we’ll load the **BERT** model from **Hugging Face** and classify log messages.

```python
from transformers import pipeline

# Load Hugging Face's BERT model (sentiment analysis as a placeholder)
classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

def classify_log_event(log_message):
    """
    Use the Hugging Face transformer model to classify log messages.
    In this example, we use a sentiment analysis model to classify
    logs as either critical or non-critical based on the 'positive' label.
    """
    result = classifier(log_message)
    if result[0]['label'] == 'POSITIVE':
        return 'critical'
    else:
        return 'not critical'
```

## Usage
### Step 6: Run the Python Application
Now you can run the **AI-powered alerting system**:

```bash
docker-compose up --build
```

## Testing and Alerts
### Step 7: Expose Metrics to Prometheus
The Python app will expose metrics at **`localhost:8000/metrics`**, which Prometheus will scrape.

### Step 8: Test Log Classification
You can test the log classification by generating various log messages in **`my-app/app.py`**:

```python
log_event('INFO', 'User logged in successfully.')
log_event('ERROR', 'SQL injection attempt detected in API.')
log_event('CRITICAL', 'Critical vulnerability found in package xyz.')
```

Prometheus will scrape the log severity metrics, and Grafana can be configured to trigger alerts for critical logs.

## Prometheus and Grafana Setup
### Step 9: Set Up Grafana for Alerts
1. **Open Grafana**: Access Grafana at **`http://localhost:3000`**.
2. **Add Data Source**: Add **Prometheus** as the data source, pointing to **`http://localhost:9090`**.
3. **Create a Dashboard**: Build a dashboard to visualize the log severity metrics from **Prometheus**.
4. **Set Up Alerts**: Create an alert rule in **Grafana** to send notifications (Slack, email, etc.) when the **`log_severity`** for **`CRITICAL`** exceeds 0.
Example Grafana Alert Rule:
```yaml
# Condition: Trigger an alert if the CRITICAL logs are detected
expr: log_severity{level="CRITICAL"} > 0
for: 1m
labels:
  severity: "critical"
annotations:
  summary: "Critical log detected"
  description: "Critical log detected in the application"
```

## Demo
After setting up the system, you’ll be able to:

1. **Monitor logs**: View all logs in Grafana.
2. **Trigger Alerts**: Only logs classified as "Critical" by the BERT model will trigger alerts, reducing noise.
