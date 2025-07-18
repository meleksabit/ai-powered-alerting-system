<a name="top"></a>
# ![AI System](https://img.shields.io/badge/AI--Powered%20Alerting%20System-green?style=for-the-badge&labelColor=green&color=green&logo=openai&logoColor=white)![Critical Alerts](https://img.shields.io/badge/Critical%20Alerts%20Only-red?style=for-the-badge&logo=huggingface&logoColor=white)

<div align="center">
  <a href="https://sonarcloud.io/summary/new_code?id=meleksabit_ai-powered-alerting-system">
    <img src="https://sonarcloud.io/images/project_badges/sonarcloud-light.svg" alt="SonarQube Cloud">
    </a>
</div> 

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=meleksabit_ai-powered-alerting-system&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=meleksabit_ai-powered-alerting-system) [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=meleksabit_ai-powered-alerting-system&metric=coverage)](https://sonarcloud.io/summary/new_code?id=meleksabit_ai-powered-alerting-system) [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=meleksabit_ai-powered-alerting-system&metric=bugs)](https://sonarcloud.io/summary/new_code?id=meleksabit_ai-powered-alerting-system) [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=meleksabit_ai-powered-alerting-system&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=meleksabit_ai-powered-alerting-system) [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=meleksabit_ai-powered-alerting-system&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=meleksabit_ai-powered-alerting-system) [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=meleksabit_ai-powered-alerting-system&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=meleksabit_ai-powered-alerting-system) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=meleksabit_ai-powered-alerting-system&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=meleksabit_ai-powered-alerting-system) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=meleksabit_ai-powered-alerting-system&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=meleksabit_ai-powered-alerting-system) [![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=meleksabit_ai-powered-alerting-system&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=meleksabit_ai-powered-alerting-system) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=meleksabit_ai-powered-alerting-system&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=meleksabit_ai-powered-alerting-system) [![Lint](https://github.com/meleksabit/ai-powered-alerting-system/actions/workflows/super-linter.yml/badge.svg)](https://github.com/meleksabit/ai-powered-alerting-system/actions/workflows/super-linter.yml) [![Python CodeQL Analysis](https://github.com/meleksabit/ai-powered-alerting-system/actions/workflows/codeql-scan.yml/badge.svg)](https://github.com/meleksabit/ai-powered-alerting-system/actions/workflows/codeql-scan.yml) [![Docker Vulnerability Scan](https://github.com/meleksabit/ai-powered-alerting-system/actions/workflows/docker-trivy-scan.yml/badge.svg)](https://github.com/meleksabit/ai-powered-alerting-system/actions/workflows/docker-trivy-scan.yml) [![Kubernetes Security Scan for Misconfigurations](https://github.com/meleksabit/ai-powered-alerting-system/actions/workflows/kubescape-scan.yml/badge.svg)](https://github.com/meleksabit/ai-powered-alerting-system/actions/workflows/kubescape-scan.yml) [![Dependabot Updates](https://github.com/meleksabit/ai-powered-alerting-system/actions/workflows/dependabot/dependabot-updates/badge.svg)](https://github.com/meleksabit/ai-powered-alerting-system/actions/workflows/dependabot/dependabot-updates) [![License: MIT](https://img.shields.io/badge/License-MIT-orange.svg)](https://opensource.org/licenses/MIT) [![PR Title Check](https://github.com/meleksabit/ai-powered-alerting-system/actions/workflows/pr-title-linter.yml/badge.svg)](https://github.com/meleksabit/ai-powered-alerting-system/actions/workflows/pr-title-linter.yml) [![GitHub Release](https://img.shields.io/github/v/release/meleksabit/ai-powered-alerting-system)](https://github.com/meleksabit/ai-powered-alerting-system/releases)

![alt text](Prometheus_Grafana_Python_Hugging_Face.png)
![Demo](demo.gif)

### This repository implements an AI-powered alerting system that uses a **Hugging Face BERT model** to classify and prioritize log alerts based on severity, specifically notifying only for **critical alerts**. The system integrates with **Prometheus** for metrics collection and **Grafana** for visualization and alerting, and is built with **Python** for log processing.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Project Structure](#%EF%B8%8Fproject-structure)
- [Use a Custom Hugging Face Model](#-use-a-custom-hugging-face-model)
- [Installation](#installation)
- [Docker-Related Files](#docker-related-files)
- [Configuration](#%EF%B8%8Fconfiguration)
- [Usage](#usage)
- [Testing and Alerts](#testing-and-alerts)
- [Prometheus and Grafana Setup](#prometheus-and-grafana-setup)
- [Demo](#demo)
- [Additional Improvements](#additional-improvements)
  - [Kubernetes Deployment](#%EF%B8%8Fkubernetes-deployment)
- [Roadmap: Next Steps for Improvements](#-roadmap-next-steps-for-improvements)

## 📢Introduction

This project demonstrates how to classify log events using **Hugging Face's BERT model** to filter critical log messages and trigger alerts only when critical issues arise. **Prometheus** is used to scrape the log metrics, and **Grafana** is used for visualization and alert notifications. This approach reduces noise by ensuring that only critical logs are flagged and alerted.

## 🚀Features:
* **`AI-Based Log Classification`**: Uses machine learning to classify log messages based on severity.
* **`Critical Alerts`**: Alerts are triggered only for critical logs, reducing noise and improving response time.
* **`Prometheus & Grafana Integration`**: Real-time metrics collection and visualization.
* **`Production-Ready Deployment`**: Uses **Gunicorn** to run the Flask app in a production environment.
* **`Kubernetes Support`**: Kubernetes manifests for deploying the system in a scalable environment.
* **`Lazy Loading`**: The system optimizes resource usage with lazy loading of machine learning models.

## 📜Prerequisites

Before starting, make sure you have the following tools installed:

* **Python 3.8+**: The application is built using Python.
* **Prometheus**: For metrics collection. Prometheus will scrape metrics from the Python app.
* **Grafana**: For data visualization and alerting. Grafana is used to monitor log metrics from Prometheus.
* **Gunicorn**: For running the Python app in a production environment. It replaces the Flask development server.
* **Docker** (Optional but recommended): Simplifies the setup for Prometheus, Grafana, and the Python app, and is useful for running the services in containers.
* **Kubernetes** (Optional): If you plan to deploy the app in a Kubernetes cluster, ensure you have a working Kubernetes environment.
* **Pip**: For managing Python packages and installing dependencies.
* **Pipenv** (Optional): For virtual environment and dependency management, if you prefer using Pipenv over pip.

### 🐍Python Dependencies

You'll need to install the following Python libraries:

- **transformers**: For Hugging Face's BERT model, which is used to classify log events based on their content.
- **prometheus-client**: For exposing log metrics to Prometheus.
- **torch**: The PyTorch library is used to run the Hugging Face BERT model. It provides an efficient and flexible way to run and classify log events.
- **flask**: The Flask web framework is used to create a simple web API for the AI-powered alerting system. The API allows you to send log messages for classification and trigger alerts if needed.
- **gunicorn**: Gunicorn is a WSGI HTTP server for running Python web applications like Flask in a production environment. It allows handling multiple requests efficiently, providing better performance and scalability compared to Flask's built-in development server.
- **requests**: For sending Slack notifications (optional).
- **smtplib**: For sending email notifications (optional).

### 🦄Why Flask and Gunicorn?

- **Flask**: Flask is a lightweight web framework, perfect for building and exposing APIs, especially in a development or small-scale environment. It provides easy setup and flexibility for defining routes and handling requests.

- **Gunicorn**: Flask's built-in development server is not suitable for production, as it can only handle a single request at a time and is not designed for high-performance workloads. Gunicorn, a robust WSGI server, is typically used in production environments. It allows Flask to run as a more efficient, multi-threaded, and scalable web application, handling concurrent requests more effectively.

<table>
<tr>
<th>🗝️ <b>CONCLUSION</b></th>
</tr>
<tr>
<td width="33%"">
In short, <b><i>Flask</i></b> handles the logic of the web application, while <b><i>Gunicorn</i></b> ensures that the application can serve requests at scale in a production environment.
</td>
</tr>
</table>

## 🏗️Project Structure

Here’s the structure of the project:

```bash
.
├── docker-compose.yml
├── k8s
│   ├── grafana-configmap.yaml
│   ├── grafana-deployment.yaml
│   ├── grafana-pvc.yaml
│   ├── grafana-service.yaml
│   ├── prometheus-configmap.yaml
│   ├── prometheus-deployment.yaml
│   ├── prometheus-pvc.yaml
│   ├── prometheus-service.yaml
│   ├── python-app-deployment.yaml
│   └── python-app-service.yaml
├── LICENSE
├── my_app
│   ├── app.py
│   ├── Dockerfile.app
│   ├── __init__.py
│   ├── start_app.py
│   └── static
│       └── favicon.ico
├── prometheus-grafana
│   ├── alert_rules.yml
│   ├── Dockerfile.grafana
│   ├── Dockerfile.prometheus
│   ├── grafana.ini
│   └── prometheus.yml
├── Prometheus_Grafana_Python_Hugging_Face.png
├── README.md
├── requirements.txt
├── sonar-project.properties
└── tests
    ├── conftest.py
    ├── __init__.py
    ├── test_app.py
    ├── test_parametrized.py
    └── test_start_app.py

6 directories, 31 files
```	
#### - [![python-1.png](https://i.postimg.cc/KjRBHDzm/python-1.png)](https://postimg.cc/8fg7FWMY) **_Python_**: Core application code.
#### - [![icons8-docker-48.png](https://i.postimg.cc/13xwv6ZZ/icons8-docker-48.png)](https://postimg.cc/w7V1v1vW) **_Docker Compose_**: Multi-container setup in `docker-compose.yml`.
#### - [![kubernetes-256x249.png](https://i.postimg.cc/26j44DNb/kubernetes-256x249.png)](https://postimg.cc/Mc4MSgTq) **_Kubernetes_**: Deployment manifests in `k8s/`.
#### - [![Git-Hub-Actions.png](https://i.postimg.cc/BQP25pkg/Git-Hub-Actions.png)](https://postimg.cc/Vd1SmqYr) **_GitHub Actions_**: CI/CD workflows in `.github/workflows/`.

## <img height="32" width="32" src="https://cdn.simpleicons.org/huggingface" /> Use a Custom Hugging Face Model

### By default, the app uses the **`distilbert-base-uncased-finetuned-sst-2-english`**
### To change it, just set the **`HF_MODEL_NAME`** environment variable:
```bash
export HF_MODEL_NAME="your-model-name"
```

## 🧑‍🔧Installation

### Step 1: Clone the repository
```bash
git clone https://github.com/meleksabit/ai-powered-alerting-system.git
cd ai-powered-alerting-system
```

### Step 2: Install Python dependencies(if you choose **Manual Installation**, without using **Docker** or **Docker Compose**)
Install the required Python libraries using pip:

```bash
pip install -r requirements.txt
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

* **Prometheus**: Accessible at **`http://localhost:9090`**
* **Grafana**: Accessible at **`http://localhost:3000`**
* **Python app**:
  * **Flask app** running on **`http://localhost:5000`**
  * **Prometheus metrics** exposed at **`http://localhost:8000/metrics`**

#### Option 2: Manual Installation
You can also manually install Prometheus and Grafana on your local machine. Follow the links below for instructions:
* [Install Prometheus](https://prometheus.io/docs/introduction/first_steps/)
* [Install Grafana](https://grafana.com/grafana/download)

## 🐋Docker-Related Files
### Dockerfile for the Python App
```dockerfile
# Use a slim version of Python to reduce image size
FROM python:3.11-slim-buster

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

# Change ownership of the /app directory to the non-root user
RUN chown -R appuser:appgroup /app

# Use non-root user
USER appuser

# Expose Flask and Prometheus ports
EXPOSE 5000
EXPOSE 8000

# Run the application
CMD ["python", "my_app/start_app.py"]
```

### Dockerfile for Prometheus
```dockerfile
# Use the official Prometheus image as the base
FROM prom/prometheus:main

# Copy custom Prometheus configuration and alert rules into the container
COPY prometheus.yml /etc/prometheus/prometheus.yml
COPY alert_rules.yml /etc/prometheus/alert_rules.yml

# Expose Prometheus on the default port
EXPOSE 9090

# Command to run Prometheus
CMD ["--config.file=/etc/prometheus/prometheus.yml", "--storage.tsdb.path=/etc/prometheus/data"]
```

### Dockerfile for Grafana
```dockerfile
# Use the official Grafana image as a base
FROM grafana/grafana:main-ubuntu

# Copy only the Grafana configuration file
COPY ./grafana.ini /etc/grafana/grafana.ini

# Expose Grafana web port
EXPOSE 3000

# Use the default entry point for the Grafana image
CMD ["/run.sh"]
```

### Docker Compose File
Here’s the **`docker-compose.yml`** that sets up both **Prometheus**, **Grafana**, and the **Python app**:

```yaml
services:
  # Prometheus service
  prometheus:
    build:
      context: ./prometheus-grafana
      dockerfile: Dockerfile.prometheus
    image: ${DOCKER_USERNAME}/prometheus:${TAG}
    ports:
      - "9090:9090"
    user: "65534"
    restart: unless-stopped
    networks:
      - monitor-net

  # Grafana service
  grafana:
    build:
      context: ./prometheus-grafana
      dockerfile: Dockerfile.grafana
      args:
        TAG: ${TAG}
    image: ${DOCKER_USERNAME}/grafana:${TAG}
    ports:
      - "3000:3000"
    volumes:
      - ./prometheus-grafana/grafana.ini:/etc/grafana/grafana.ini
      - grafana_data:/var/lib/grafana
    environment:
      - GF_RENDERING_SERVER_URL=http://renderer:8081/render
      - GF_RENDERING_CALLBACK_URL=http://grafana:3000/
    restart: unless-stopped
    depends_on:
      - renderer
    networks:
      - monitor-net

  # Grafana Image Renderer service
  renderer:
    image: grafana/grafana-image-renderer:latest
    ports:
      - "8081:8081"
    restart: unless-stopped
    networks:
      - monitor-net

  # Python Flask app service
  python-app:
    environment:
      - PYTHONPATH=/app
    build:
      context: .
      dockerfile: ./my_app/Dockerfile.app
      args:
        TAG: ${TAG}
    image: ${DOCKER_USERNAME}/ai-powered-alerting-system:${TAG}
    ports:
      - "5000:5000"  # Expose Flask app on port 5000
      - "8000:8000"  # Expose Prometheus metrics on port 8000
    volumes:
      - ./my_app:/app/my_app  # Mount app source code
    restart: unless-stopped
    depends_on:
      - prometheus
      - grafana
    networks:
      - monitor-net

# Define a shared network
networks:
  monitor-net:
    driver: bridge

# Define a volume for Prometheus & Grafana data storage
volumes:
  prometheus_data:
  grafana_data:
```

## 🛠️Configuration
### 🔥Step 4: Prometheus Configuration
Edit the **`prometheus-grafana/prometheus.yml`** file to add a scrape config for your Python app that exposes metrics on **`localhost:8000`**:

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

  # Scrape metrics from the Python AI-powered alerting app (now on port 8000)
  - job_name: "ai-powered-alerting-app"
    static_configs:
      - targets: ["python-app:8000"]  # Python app exposing metrics on port 8000
```

* Scrapes metrics from your Python app (**`ai-powered-alerting-app`**) at **`localhost:8000`**.
* Includes the **`alert_rules.yml`** file for **Prometheus** to evaluate alert rules.

### 📛Step 5: Alert Rules Configuration
Create the **`alert_rules.yml`** file in your Prometheus configuration directory (**`/etc/prometheus/`**).

alert_rules.yml:
```yml
groups:
  - name: critical_alert_rules
    rules:
      - alert: CriticalLogAlert
        expr: log_severity{severity="critical"} > 0
        for: 1m
        labels:
          severity: "critical"
        annotations:
          summary: "Critical log detected"
          description: "A critical log event was detected in the AI-powered alerting system."
```

#### 🤷‍♂️❔How This Works:
* **`prometheus.yml`**: This file tells Prometheus to scrape metrics from both Prometheus itself and the AI-powered alerting app (your Python app).
* **`alert_rules.yml`**: This file defines alerting rules that notify you when a critical log event is detected (based on the **`log_severity`** metric exposed by the Python app).

### 🤗Step 6: Hugging Face BERT Model Setup
In the **`my_app/app.py file`**, we’ll load the **BERT** model from **Hugging Face** and classify log messages.

```python
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

def lazy_load_model():
    """Lazy load the model and tokenizer for text classification."""
    global model, tokenizer, classifier, app_ready
    if model is None or tokenizer is None or classifier is None:
        logging.info("Loading model and tokenizer lazily...")
        tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
        model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
        classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)
        logging.info("Model and tokenizer loaded.")
    app_ready = True

def classify_log_event(log_message):
    """Classify log messages using Hugging Face DistilBERT model."""
    lazy_load_model()  # Ensure the model and tokenizer are loaded
    result = classifier(log_message)  # Use the classifier pipeline

    # Determine severity based on sentiment analysis result
    severity = 'not_critical' if result[0]['label'] == 'POSITIVE' else 'critical'
    log_severity.labels(severity=severity).inc()  # Update Prometheus metric
    logging.info(f"Classified log '{log_message}' as {severity}")
    return severity
```

## ⚡Usage
### Step 7: Run the Python Application
Now you can run the **AI-powered alerting system**:

```bash
docker-compose up --build
```

## 📝Testing and Alerts
### 🔥Step 8: Expose Metrics to Prometheus
The Python app will expose Prometheus metrics at **`http://localhost:8000/metrics`**. Prometheus will scrape these metrics to monitor the log severity levels (e.g., **`critical`**, **`not_critical`**).

* Metrics URL: **`http://localhost:8000/metrics`**

Prometheus will automatically scrape this endpoint based on the scrape configuration.

### 🗂️Step 9: Test Log Classification
You can test the log classification functionality by generating various log messages through the app's HTTP API.

* Use the **`/log/<message>`** endpoint to send log messages to be classified by the Hugging Face BERT model.
* The model will classify each log as either critical or not critical, based on the message's sentiment (this uses a sentiment analysis model as a placeholder).

Example log classifications:

1. **Test Log 1**: Classifying a user log-in message as ***"not critical"***:
```bash
curl http://localhost:5000/log/User%20logged%20in%20successfully
```
2. **Test Log 2**: Classifying an SQL injection attempt as ***"critical"***:
```bash
curl http://localhost:5000/log/SQL%20injection%20attempt%20detected%20in%20API
```
3. **Test Log 3**: Classifying a critical vulnerability detection as ***"critical"***:
```bash
curl http://localhost:5000/log/Critical%20vulnerability%20found%20in%20package%20xyz
```

Each of these log messages will be classified by the AI-powered system, and the classification will be reflected in the Prometheus metrics.

The Python app automatically updates the Prometheus metric **`log_severity`** with the corresponding severity label (critical or not_critical), which Prometheus will scrape.

## 🔥🔅Prometheus and Grafana Setup
### Step 10: Set Up Grafana for Alerts
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
# Condition: Trigger an alert if any critical logs are detected
expr: log_severity{severity="critical"} > 0
for: 1m
labels:
  severity: "critical"
annotations:
  summary: "Critical log detected"
  description: "A critical log was detected in the application"
```

### 💡Demo
After setting up Prometheus and Grafana with the Python AI-powered alerting system, you’ll be able to:

1. **Monitor Logs**:

* View the log severity metrics in Grafana to monitor the number of critical and non-critical logs processed by the system.

2. **Trigger Alerts**:

* Grafana will trigger alerts based on the **`log_severity`** metric.

* Only logs classified as **`critical`** by the ***BERT*** model will trigger alerts, reducing noise and focusing on important events.

## ➕📶🔝🆙Additional Improvements:

### ☸️Kubernetes Deployment:
You can also deploy the system using **Kubernetes**. This section includes the Kubernetes manifests for deploying Prometheus, Grafana, and the Python app.

### Deployment Steps:

1. **Apply the Kubernetes manifests**:
  ```bash
  kubectl apply -f k8s/
  ```
2. **Scale the Python app**: If you want to scale the Python app deployment, run: 
  ```bash
kubectl scale deployment python-app --replicas=3
  ```

### Kubernetes Deployment Files
Below are the Kubernetes manifest files located in the `k8s/` directory:

### Deployment for Python App (python-app-deployment.yaml):
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: python-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: python-app
  template:
    metadata:
      labels:
        app: python-app
    spec:
      securityContext:
        runAsUser: 1000
        runAsGroup: 3000
        runAsNonRoot: true
        fsGroup: 2000
      containers:
        - name: python-app
          image: angel3/ai-powered-alerting-system:${IMAGE_TAG}
          resources:
            requests:
              cpu: "200m"
              memory: "256Mi"
            limits:
              cpu: "400m"
              memory: "512Mi"
          securityContext:
            readOnlyRootFilesystem: true
            allowPrivilegeEscalation: false
            capabilities:
              drop:
                - ALL
          env:
            - name: SENDER_EMAIL
              valueFrom:
                secretKeyRef:
                  name: email-secrets
                  key: sender-email
            - name: NOTIFICATION_RECEIVER
              valueFrom:
                secretKeyRef:
                  name: email-secrets
                  key: notification-receiver
            - name: SLACK_BOT_TOKEN
              valueFrom:
                secretKeyRef:
                  name: email-secrets
                  key: SLACK_BOT_TOKEN
            - name: SLACK_SIGNING_SECRET
              valueFrom:
                secretKeyRef:
                  name: email-secrets
                  key: SLACK_SIGNING_SECRET
          ports:
            - containerPort: 5000
          startupProbe:
            httpGet:
              path: /startup
              port: 5000
            initialDelaySeconds: 30
            periodSeconds: 10
            failureThreshold: 5
          readinessProbe:
            httpGet:
              path: /readiness
              port: 5000
            initialDelaySeconds: 10
            periodSeconds: 5
          livenessProbe:
            httpGet:
              path: /health
              port: 5000
            initialDelaySeconds: 10
            periodSeconds: 5
```

### Service for Python App (python-app-service.yaml):
```yaml
apiVersion: v1
kind: Service
metadata:
  name: python-app-service
spec:
  type: NodePort
  selector:
    app: python-app
  ports:
    - protocol: TCP
      port: 5000
      targetPort: 5000
```

### Deployment for Prometheus (prometheus-deployment.yaml):
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: prometheus
  labels:
    app: prometheus
spec:
  replicas: 1
  selector:
    matchLabels:
      app: prometheus
  template:
    metadata:
      labels:
        app: prometheus
    spec:
      securityContext:
        runAsUser: 1000
        runAsGroup: 3000
        runAsNonRoot: true
        fsGroup: 2000
      containers:
        - name: prometheus
          image: prom/prometheus:main  # Replaced `main` with a stable version
          args:
            - "--config.file=/etc/prometheus/prometheus.yml"
          ports:
            - containerPort: 9090
          resources:
            requests:
              cpu: "500m"
              memory: "512Mi"
            limits:
              cpu: "1"
              memory: "1Gi"
          securityContext:
            readOnlyRootFilesystem: true
            allowPrivilegeEscalation: false
            capabilities:
              drop:
                - ALL
          volumeMounts:
            - name: config-volume
              mountPath: /etc/prometheus/
      volumes:
        - name: config-volume
          configMap:
            name: prometheus-config
```

### Service for Prometheus (prometheus-service.yaml):
```yaml
apiVersion: v1
kind: Service
metadata:
  name: prometheus-service
spec:
  selector:
    app: prometheus
  ports:
    - protocol: TCP
      port: 9090
      targetPort: 9090
  type: NodePort
```
### ConfigMap for Prometheus (prometheus-configmap.yaml):
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: prometheus-config
  namespace: default
data:
  prometheus.yml: |
    # Global settings
    global:
      scrape_interval: 15s  # Scrape every 15 seconds
      evaluation_interval: 15s  # Evaluate rules every 15 seconds

    # Alertmanager configuration (if using Alertmanager)
    alerting:
      alertmanagers:
        - static_configs:
            - targets: ['alertmanager:9093']  # Define Alertmanager target if in use

    # Reference to rule files
    rule_files:
      - "/etc/prometheus/alert_rules.yml"  # Points to the alert rules file

    # Scrape configurations
    scrape_configs:
      # Scrape Prometheus itself
      - job_name: "prometheus"
        static_configs:
          - targets: ["localhost:9090"]

      # Scrape metrics from the Python AI-powered alerting app via localhost (requires port-forwarding)
      - job_name: "ai-powered-alerting-app"
        static_configs:
          - targets: ["localhost:8000"]  # Python app exposing metrics, accessible on localhost via port-forwarding
```
### Persistent Volume Claim for Prometheus (prometheus-pvc.yaml):
```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: prometheus-data
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi  # Adjust storage size as needed
```
### Deployment for Grafana (grafana-deployment.yaml):
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: grafana
  labels:
    app: grafana
spec:
  replicas: 1
  selector:
    matchLabels:
      app: grafana
  template:
    metadata:
      labels:
        app: grafana
    spec:
      securityContext:
        runAsUser: 1000
        runAsGroup: 3000
        runAsNonRoot: true
        fsGroup: 2000
      containers:
        - name: grafana
          image: grafana/grafana:main-ubuntu
          ports:
            - containerPort: 3000
          resources:
            requests:
              cpu: "250m"
              memory: "256Mi"
            limits:
              cpu: "500m"
              memory: "512Mi"
          securityContext:
            readOnlyRootFilesystem: true
            allowPrivilegeEscalation: false
            capabilities:
              drop:
                - ALL
          volumeMounts:
            - name: grafana-data
              mountPath: /var/lib/grafana
            - name: grafana-config
              mountPath: /etc/grafana/grafana.ini
              subPath: grafana.ini
      volumes:
        - name: grafana-data
          persistentVolumeClaim:
            claimName: grafana-pvc
        - name: grafana-config
          configMap:
            name: grafana-config
```

### Service for Grafana (grafana-service.yaml):
```yaml
apiVersion: v1
kind: Service
metadata:
  name: grafana-service
spec:
  selector:
    app: grafana
  ports:
    - protocol: TCP
      port: 3000
      targetPort: 3000
  type: NodePort
```
### ConfigMap for Grafana (grafana-configmap.yaml):
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: grafana-config
data:
  grafana.ini: |
    [security]
    admin_user = ${GF_SECURITY_ADMIN_USER}
    admin_password = ${GF_SECURITY_ADMIN_PASSWORD}
```
### Persistent Volume Claim for Grafana (grafana-pvc.yaml):
```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: grafana-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 5Gi
```

> [!NOTE]
> These manifest files help you set up the **Python app**, **Prometheus**, and **Grafana** in a Kubernetes cluster.

> [!TIP]
> Handling Gunicorn Worker Timeouts
If you encounter issues such as worker timeouts in Gunicorn (e.g., **`WORKER TIMEOUT`** errors in the logs), you can adjust the worker timeout directly in the **`start_app.py`** script. The current configuration in **`start_app.py`** sets a timeout of 30 seconds, which can be increased if necessary to prevent premature worker timeouts during long-running processes or slow startup times.
The configuration looks like this:
```python
options = {
    'bind': '0.0.0.0:5000',
    'workers': 4,
    'timeout': 30,  # Default timeout set to 30 seconds
}
```

If needed, you can increase the timeout by modifying the timeout value in this script.


This configuration ensures that the Gunicorn workers have enough time to handle requests, especially during long-running processes or slow startup times.

## 📌 Roadmap: Next Steps for Improvements

### This section outlines potential improvements and enhancements for the **_AI-Powered Alerting System_** to make it more robust, scalable, and feature-rich:

## 🔔 Notification System
### :white_check_mark: Implement Email Notifications --> implemented via **`yagmail`** library
#### Integrate email notifications (e.g., using **_SMTP_** libraries like **`smtplib`** or third-party **_APIs_** like **_SendGrid_**) to send alerts for critical logs detected by the system.
#### **_Why?_** Provides real-time updates to stakeholders.

### :white_check_mark: Integrate Slack Notifications --> implemented via **`slack_bolt`** library
#### Use **_Slack_** webhooks to send log classifications and critical alerts directly to dedicated Slack channels.
#### **_Why?_** Improves communication within teams and ensures swift responses to critical events.

## 🧠 Enhanced AI/ML Capabilities
### :white_large_square: Experiment with Alternative Language Models (LLMs)
#### Test with other transformer-based models like **`GPT`**, **`T5`**, or fine-tuned versions of **`BERT`** specific to log analysis or sentiment classification (e.g., **_Hugging Face's_** **`bert-for-log-analysis`** models).

### :white_large_square: Implement Model Monitoring and Retraining Pipelines
#### Automate periodic retraining of the ML model using up-to-date logs to improve accuracy. Tools like **_MLflow_** or **_TensorFlow Serving_** can be helpful.
#### **_Why?_** Maintains the model's effectiveness as log patterns evolve over time.

## 📈 Scalability Enhancements
### :white_large_square: NGINX Integration
#### Add **_NGINX_** as a reverse proxy to improve load balancing and handle multiple simultaneous requests efficiently.
#### **_Why?_** Enhances performance and security, especially under heavy traffic.

### :white_large_square: Service Mesh with Istio
#### Use **_Istio_** to manage service-to-service communication, observability, and security within your Kubernetes cluster.
#### **_Why?_** Simplifies networking, provides traffic encryption, and facilitates microservice observability.

### :white_large_square: Adopt Horizontal Pod Autoscaling
#### Enable Kubernetes Horizontal Pod Autoscaling (HPA) for the Python app to dynamically scale based on CPU or memory utilization.
#### **_Why?_** Ensures that the system can handle varying workloads efficiently.

## 🚀 Deployment & CI/CD
### :white_large_square: ArgoCD for GitOps Deployment
#### Implement **_ArgoCD_** to manage Kubernetes deployments via GitOps principles.
#### **_Why?_** Automates and synchronizes deployment workflows, reducing manual intervention and ensuring consistency.

### :white_check_mark: Add Unit Testing to CI/CD Pipelines
#### Include unit tests in the GitHub Actions pipeline for verifying individual components in isolation.
#### **_Why?_** Ensures the correctness of each function or module, catching bugs early in development.

### :white_large_square: Add Integration Testing to CI/CD Pipelines
#### Include integration tests for end-to-end system verification in the GitHub Actions pipeline.
#### **_Why?_** Ensures that new code changes don’t break interdependent components.

## 🔒 Security Improvements
### :white_large_square: Enforce HTTPS with Cert-Manager
#### Use **_Cert-Manager_** in Kubernetes to automatically issue and renew **_TLS_** certificates for secure communication.
#### **_Why?_** Protects sensitive data and avoids exposing the application over HTTP.

### :white_large_square: Implement Role-Based Access Control (RBAC)
#### Define and enforce fine-grained access permissions within the Kubernetes cluster.
#### **_Why?_** Enhances security by limiting access to resources based on user roles.

## 🛠 Additional Improvements
### :white_large_square: Centralized Logging with ELK Stack
#### Integrate **_Elasticsearch_**, **_Logstash_**, and **_Kibana_** to provide powerful log aggregation and analysis capabilities.
#### **_Why?_** Enables deeper insights into logs and simplifies debugging.

### :white_large_square: Performance Benchmarking
#### Conduct stress testing and performance benchmarking (e.g., with **_k6_**, **_Apache JMeter_**) to identify bottlenecks.
#### **_Why?_** Helps optimize the system for high availability.

### :white_large_square: Support Multiple Alert Channels
#### Extend the alerting framework to integrate with additional tools like **_PagerDuty_**, **_Microsoft Teams_**, or **_Opsgenie_**.
#### **_Why?_** Provides flexibility for different organizations.

[:arrow_up:](#top)
