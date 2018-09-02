FROM grafana/grafana:4.3.2

RUN apt-get update && \
    apt-get install -y curl gettext-base && \
    rm -rf /var/lib/apt/lists/*

COPY ./grafana/grafana.ini /etc/grafana/grafana.ini
COPY ./grafana/dashboards /etc/grafana/dashboards
COPY ./grafana/datasources /etc/grafana/datasources

COPY ./grafana/entrypoint.sh .
RUN chmod +x entrypoint.sh

RUN rm -rf /var/lib/grafana/.init

ENTRYPOINT ["./entrypoint.sh"]