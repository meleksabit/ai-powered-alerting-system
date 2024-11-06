<a name="top"></a>
# $\color{SeaGreen}{AI-Powered\ Alerting\ System:}$ $\color{OrangeRed}{Critical\ Alerts\ Only}$

![alt text](Prometheus_Grafana_Python_Hugging_Face.png)
 
### This repository implements an AI-powered alerting system that uses a **Hugging Face BERT model** to classify and prioritize log alerts based on severity, specifically notifying only for **critical alerts**. The system integrates with **Prometheus** for metrics collection and **Grafana** for visualization and alerting, and is built with **Python** for log processing.

## Table of Contents
- [Introduction](#📢introduction)
- [Features](#🚀features)
- [Prerequisites](#📜prerequisites)
- [Project Structure](#🏗️project-structure)
- [Installation](#🧑‍🔧installation)
- [Docker-Related Files](#🐋docker-related-files)
- [Configuration](#🛠️configuration)
- [Usage](#⚡usage)
- [Testing and Alerts](#📝testing-and-alerts)
- [Prometheus and Grafana Setup](#🔥🔅prometheus-and-grafana-setup)
- [Demo](#💡demo)
- [Additional Improvements](#➕📶🔝🆙additional-improvements)
  - [Kubernetes Deployment](#☸️kubernetes-deployment)

## 📢Introduction

This project demonstrates how to classify log events using **Hugging Face's BERT model** to filter critical log messages and trigger alerts only when critical issues arise. **Prometheus** is used to scrape the log metrics, and **Grafana** is used for visualization and alert notifications. This approach reduces noise by ensuring that only critical logs are flagged and alerted.

## 🚀Features:
* **`AI-Based Log Classification`**: Uses machine learning to classify log messages based on severity.
* **`Critical Alerts`**: Alerts are triggered only for critical logs, reducing noise and improving response time.
* **`Prometheus & Grafana Integration`**: Real-time metrics collection and visualization.
* **`Production-Ready Deployment`**: Now uses **Gunicorn** to run the Flask app in a production environment.
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
<td width="33%"">
<th>🗝️ **INFO**</th>
In short, <b>Flask**</b> handles the logic of the web application, while <b>Gunicorn</b> ensures that the application can serve requests at scale in a production environment.
</td>
</tr>
</table>

## 🏗️Project Structure

Here’s the structure of the project:

```bash
.
├── docker-compose.yml
├── k8s
│   ├── grafana-deployment.yaml
│   ├── grafana-service.yaml
│   ├── prometheus-configmap.yaml
│   ├── prometheus-deployment.yaml
│   ├── prometheus-pvc.yaml
│   ├── prometheus-service.yaml
│   ├── python-app-deployment.yaml
│   └── python-app-service.yaml
├── LICENSE
├── my-app
│   ├── app.py
│   ├── Dockerfile.app
│   ├── requirements.txt
│   ├── start_app.py
│   └── static
│       └── favicon.ico
├── prometheus-grafana
│   ├── alert_rules.yml
│   ├── Dockerfile.grafana
│   └── prometheus.yml
├── Prometheus_Grafana_Python_Hugging_Face.png
└── README.md

5 directories, 20 files
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

# Install necessary system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt

# Preload Hugging Face models to avoid downloading on startup
RUN python -c "from transformers import AutoModelForSequenceClassification, AutoTokenizer; \
    AutoModelForSequenceClassification.from_pretrained('distilbert-base-uncased-finetuned-sst-2-english'); \
    AutoTokenizer.from_pretrained('distilbert-base-uncased-finetuned-sst-2-english')"

# Copy the rest of the application code
COPY . .

# Expose necessary ports for Flask (5000) and Prometheus metrics (8000)
EXPOSE 5000
EXPOSE 8000

# Run the application (starting both Prometheus and Gunicorn from Python)
CMD ["python", "start_app.py"]
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
  # Prometheus service
  prometheus:
    image: cgr.dev/chainguard/prometheus:latest
    volumes:
      - ./prometheus-grafana/prometheus.yml:/etc/prometheus/prometheus.yml  # Mount config
      - ./prometheus-grafana/alert_rules.yml:/etc/prometheus/alert_rules.yml  # Mount alert rules
      - /home/angel3/data/:/etc/prometheus/data  # Data storage
    user: "65534"  # Run Prometheus as `nobody`
    ports:
      - "9090:9090"  # Expose Prometheus on port 9090
    command: ["--config.file=/etc/prometheus/prometheus.yml", "--storage.tsdb.path=/etc/prometheus/data"]
    restart: unless-stopped
    networks:
      - monitor-net

  # Grafana service
  grafana:
    build:
      context: ./prometheus-grafana
      dockerfile: Dockerfile.grafana
    ports:
      - "3000:3000"  # Expose Grafana on port 3000
    restart: unless-stopped
    networks:
      - monitor-net

  # Python Flask app service
  python-app:
    build:
      context: ./my-app
      dockerfile: Dockerfile.app
    ports:
      - "5000:5000"  # Expose Flask app on port 5000
      - "8000:8000"  # Expose Prometheus metrics on port 8000
    volumes:
      - ./my-app:/app  # Mount app source code
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

# Define a volume for Prometheus data storage
volumes:
  prometheus_data:
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
        expr: log_severity{level="critical"} > 0  # Alert when critical logs are detected
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
In the **`my-app/app.py file`**, we’ll load the **BERT** model from **Hugging Face** and classify log messages.

```python
from transformers import pipeline

# Load Hugging Face's BERT model (sentiment analysis as a placeholder)
classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

def classify_log_event(log_message):
    """
    Classify log messages using Hugging Face DistilBERT model for sentiment analysis.
    Lazily loads the model and tokenizer if they are not already loaded.
    """
    lazy_load_model()

    result = classifier(log_message)

    # Determine severity based on sentiment
    if result[0]['label'] == 'POSITIVE':
        severity = 'not_critical'
    else:
        severity = 'critical'

    log_severity.labels(severity=severity).inc()

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
Below are the Kubernetes manifest files located in the k8s/ directory:

### Deployment for Python App (python-app-deployment.yaml):
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: python-app
spec:
  replicas: 2
  selector:
    matchLabels:
      app: python-app
  template:
    metadata:
      labels:
        app: python-app
    spec:
      containers:
        - name: python-app
          image: angel3/ai-powered-alerting-system-python-app:latest
          ports:
            - containerPort: 5000
```

### Service for Python App (python-app-service.yaml):
```yaml
apiVersion: v1
kind: Service
metadata:
  name: python-app-service
spec:
  type: ClusterIP
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
      containers:
        - name: prometheus
          image: cgr.dev/chainguard/prometheus:latest
          ports:
            - containerPort: 9090
          volumeMounts:
            - name: prometheus-config
              mountPath: /etc/prometheus/prometheus.yml
              subPath: prometheus.yml
      volumes:
        - name: prometheus-config
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
  type: ClusterIP
  selector:
    app: prometheus
  ports:
    - protocol: TCP
      port: 9090
      targetPort: 9090
```

### Deployment for Grafana (grafana-deployment.yaml):
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: grafana
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
      containers:
        - name: grafana
          image: cgr.dev/chainguard/grafana:latest
          ports:
            - containerPort: 3000
```

### Service for Grafana (grafana-service.yaml):
```yaml
apiVersion: v1
kind: Service
metadata:
  name: grafana-service
spec:
  type: ClusterIP
  selector:
    app: grafana
  ports:
    - protocol: TCP
      port: 3000
      targetPort: 3000
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

[:arrow_up:](#top)
