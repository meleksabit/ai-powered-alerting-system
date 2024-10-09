# $\color{SeaGreen}{AI-Powered\ Alerting\ System:}$ $\color{OrangeRed}{Critical\ Alerts\ Only}$

This repository implements an AI-powered alerting system that uses a **Hugging Face BERT model** to classify and prioritize log alerts based on severity, specifically notifying only for **critical alerts**. The system integrates with **Prometheus** for metrics collection and **Grafana** for visualization and alerting, and is built with **Python** for log processing.

## Table of Contents
- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Installation](#installation)
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
