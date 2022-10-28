FROM nginx:stable-alpine

COPY nginx.conf /etc/nginx/nginx.conf
COPY gpim_nginx.conf /etc/nginx/sites-available/

RUN mkdir -p /etc/nginx/sites-enabled/ && \
    ln -sf /etc/nginx/sites-available/gpim_nginx.conf /etc/nginx/sites-enabled/

CMD ["nginx", "-g", "daemon off;"]
