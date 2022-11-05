FROM nginx:stable-alpine

COPY nginx.conf /etc/nginx/nginx.conf
COPY app_nginx.conf /etc/nginx/sites-available/

RUN mkdir -p /etc/nginx/sites-enabled/ && \
    ln -sf /etc/nginx/sites-available/app_nginx.conf /etc/nginx/sites-enabled/

CMD ["nginx", "-g", "daemon off;"]
