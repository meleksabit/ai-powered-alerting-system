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
- **torch**: The PyTorch library is used to run the Hugging Face BERT model. It provides an efficient and flexible way to run the model and classify log events.
- **flask**: The Flask web framework is used to expose a simple web API for the AI-powered alerting system. The API allows you to send log messages to be classified and trigger alerts if needed.
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
│   ├── Dockerfile.app
│   ├── requirements.txt
│   └── static
│       └── favicon.ico
├── prometheus-grafana
│   ├── alert_rules.yml
│   ├── data
│   ├── Dockerfile.grafana
│   └── prometheus.yml
└── README.md

5 directories, 10 files
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
* **Python app** (exposing metrics) on **`http://localhost:5000/metrics`**

#### Option 2: Manual Installation
You can also manually install Prometheus and Grafana on your local machine. Follow the links below for instructions:
* [Install Prometheus](https://prometheus.io/docs/introduction/first_steps/)
* [Install Grafana](https://grafana.com/grafana/download)

## Docker-Related Files
### Dockerfile for the Python App
```dockerfile
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
```

### Dockerfile for Grafana
```dockerfile
# Use Chainguard's secure Grafana image
FROM cgr.dev/chainguard/grafana:latest

# Set environment variables if needed
ENV GF_SECURITY_ADMIN_PASSWORD=admin

# Expose Grafana port
EXPOSE 3000

# Set the default command
CMD ["grafana-server", "--homepath=/usr/share/grafana", "--config=/etc/grafana/grafana.ini"]
```

### Docker Compose File
Here’s the **`docker-compose.yml`** that sets up both **Prometheus**, **Grafana**, and the **Python app**:

```yaml
services:
  # Prometheus
  prometheus:
    image: cgr.dev/chainguard/prometheus:latest
    volumes:
      - ./prometheus-grafana/prometheus.yml:/etc/prometheus/prometheus.yml  # Mount the config file
      - ./prometheus-grafana/alert_rules.yml:/etc/prometheus/alert_rules.yml  # Mount the rule file
      - /home/angel3/data/:/etc/prometheus/data  # Use a Docker volume for data storage
    user: "65534"  # Set Prometheus to run as nobody
    ports:
      - "9090:9090"  # Expose port 9090 on the host to port 9090 in the container
    entrypoint:
      - /usr/bin/prometheus
      - --config.file=/etc/prometheus/prometheus.yml
      - --storage.tsdb.path=/etc/prometheus/data
    restart: unless-stopped

  # Grafana
  grafana:
    build:
      context: ./prometheus-grafana
      dockerfile: Dockerfile.grafana
    ports:
      - "3000:3000"  # Expose port 3000 for Grafana
    restart: unless-stopped

  # Python app
  python-app:
    build:
      context: ./my-app
      dockerfile: Dockerfile.app
    ports:
      - "5000:5000"  # Expose port 5000 for the Python app
    restart: unless-stopped
    depends_on:
      - prometheus
      - grafana

volumes:
  prometheus_data:  # Define the volume for Prometheus data storage
```

## Configuration
### Step 4: Prometheus Configuration
Edit the **`prometheus-grafana/prometheus.yml`** file to add a scrape config for your Python app that exposes metrics on **`localhost:5000`**:

```yaml
# Global settings
global:
  scrape_interval: 15s  # Scrape every 15 seconds
  evaluation_interval: 15s  # Evaluate rules every 15 seconds

# Alertmanager configuration (if using Alertmanager)
alerting:
  alertmanagers:
    - static_configs:
        - targets: ['alertmanager:9093']  # Define Alertmanager target

# Reference to rule files
rule_files:
  - "/etc/prometheus/alert_rules.yml"  # Points to your alert rules file

# Scrape configurations
scrape_configs:
  # Scrape Prometheus itself
  - job_name: "prometheus"
    static_configs:
      - targets: ["localhost:9090"]

  # Scrape metrics from the Python AI-powered alerting app
  - job_name: "ai-powered-alerting-app"
    static_configs:
      - targets: ["python-app:5000"]  # Your Python app exposing metrics on port 5000

```

* Scrapes metrics from your Python app (**`ai-powered-alerting-app`**) at **`python-app:5000`**.
* Includes the **`alert_rules.yml`** file for **Prometheus** to evaluate alert rules.

### Step 5: Alert Rules Configuration
Create the **`alert_rules.yml`** file in your Prometheus configuration directory (**`/etc/prometheus/`**).

alert_rules.yml:
```yml
groups:
  - name: critical_alert_rules
    rules:
      - alert: CriticalLogAlert
        expr: log_severity{level="critical"} > 0  # Alert when critical logs are detected
        for: 1m
        labels:
          severity: "critical"
        annotations:
          summary: "Critical log detected"
          description: "A critical log event was detected in the AI-powered alerting system."
```

#### How This Works:
* **`prometheus.yml`**: This file tells Prometheus to scrape metrics from both Prometheus itself and the AI-powered alerting app (your Python app).
* **`alert_rules.yml`**: This file defines alerting rules that notify you when a critical log event is detected (based on the **`log_severity`** metric exposed by the Python app).

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
The Python app will expose Prometheus metrics at **`http://localhost:5000/metrics`**. Prometheus will scrape these metrics to monitor the log severity levels (e.g., **`critical`**, **`not_critical`**).

* Metrics URL: **`http://localhost:5000/metrics`**

Prometheus will automatically scrape this endpoint based on the scrape configuration.

### Step 8: Test Log Classification
You can test the log classification functionality by generating various log messages through the app's HTTP API.

* Use the **`/log/<message>`** endpoint to send log messages to be classified by the Hugging Face BERT model.
* The model will classify each log as either critical or not critical, based on the message's sentiment (this uses a sentiment analysis model as a placeholder).

Example log classifications:

1. **Test Log 1**: Classifying a user log-in message as ***"not critical"***:
```bash
curl http://localhost:5000/log/User%20logged%20in%20successfully
```
2. **Test Log 2**: Classifying an SQL injection attempt as ***"not critical"***:
```bash
curl http://localhost:5000/log/SQL%20injection%20attempt%20detected%20in%20API
```
3. **Test Log 3**: Classifying a critical vulnerability detection as ***"critical"***:
```bash
curl http://localhost:5000/log/Critical%20vulnerability%20found%20in%20package%20xyz
```

Each of these log messages will be classified by the AI-powered system, and the classification will be reflected in the Prometheus metrics.

The Python app automatically updates the Prometheus metric log_severity with the corresponding severity label (critical or not_critical), which Prometheus will scrape.

### Step 9: Set Up Grafana for Alerts
You can now set up Grafana to visualize and alert based on the **`log_severity`** metrics.

1. **Open Grafana**: Access Grafana by navigating to **`http://localhost:3000`** in your browser.
2. **Add Data Source**: Add Prometheus as the data source in Grafana:

* Name: Prometheus
* Type: Prometheus
* URL: **`http://prometheus:9090`** (Use the container name if Grafana and Prometheus are running in Docker, i.e., **`http://prometheus:9090`**)

3. **Create a Dashboard**:

* Build a dashboard in Grafana to visualize the log severity metrics being scraped from Prometheus.
* For example, create a time series graph to display the metric **`log_severity`** with labels for **`critical`** and **`not_critical`** logs.

4. **Set Up Alerts**:
* Create an alert rule in Grafana to send notifications when the **`log_severity`** metric for **`critical`** logs exceeds 0.

Example Grafana alert rule:

```yaml
# Condition: Trigger an alert if any critical logs are detected
expr: log_severity{severity="critical"} > 0
for: 1m
labels:
  severity: "critical"
annotations:
  summary: "Critical log detected"
  description: "A critical log was detected in the application"
```

### Demo
After setting up Prometheus and Grafana with the Python AI-powered alerting system, you’ll be able to:

1. **Monitor Logs**:

* View the log severity metrics in Grafana to monitor the number of critical and non-critical logs processed by the system.

2. **Trigger Alerts**:

* Grafana will trigger alerts based on the **`log_severity`** metric.

* Only logs classified as **`critical`** by the ***BERT*** model will trigger alerts, reducing noise and focusing on important events.
