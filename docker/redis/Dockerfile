FROM redis:7.0.5

USER root

COPY docker/redis/config/redis_logrotate.conf /etc/

RUN apt-get update && apt-get -y install logrotate vim

RUN logrotate -f /etc/redis_logrotate.conf && \
    echo 'vm.overcommit_memory = 1' >> /etc/sysctl.conf
