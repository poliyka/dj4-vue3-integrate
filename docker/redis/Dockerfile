FROM redis:7.0.5

USER root

COPY docker/redis/config/logrotate /etc/logrotate.d/

RUN chmod 777 -R /etc/logrotate.d/*
