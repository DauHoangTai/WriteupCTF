FROM ubuntu:latest

RUN apt-get update -y && apt-get upgrade -y && apt-get install nginx supervisor -y && apt-get install -y python3 python3-pip

RUN useradd service && mkdir /home/service

WORKDIR /home/service

COPY src/ .
COPY supervisor.conf /etc/supervisor.conf
COPY default  /etc/nginx/sites-available/default

RUN pip install flask
RUN pip install flask-socketio

RUN rm /etc/nginx/sites-available/default && rm /etc/nginx/sites-enabled/default && ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default

RUN chown -R service:root /home/service/ && chmod 770 -R /home/service/

RUN ln -sf /dev/stdout /var/log/nginx/access.log && \
    ln -sf /dev/stderr /var/log/nginx/error.log

USER root
# flag random
COPY flag* /

CMD ["supervisord", "-c", "/etc/supervisor.conf"]