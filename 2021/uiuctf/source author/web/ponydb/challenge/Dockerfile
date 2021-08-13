FROM python:3.9-slim

RUN pip3 install flask mysql-connector-python gunicorn

WORKDIR /app

COPY ponydb.py ./
COPY templates templates/

ENV SECRET_KEY=2f22baf683182bd72a51c3d53f0fee79
ENV DB_HOST=127.0.0.1
ENV DB_USER=iheartponies
ENV DB_PASS=5a21f99b09ea1608f9419d717421410a
ENV DB=ponies
ENV FLAG=uiuctf{My_l33tle_p0ny_5fb234}

EXPOSE 1337

CMD mount -t tmpfs none /tmp && python3 /app/ponydb.py
