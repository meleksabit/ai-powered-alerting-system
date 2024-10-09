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
