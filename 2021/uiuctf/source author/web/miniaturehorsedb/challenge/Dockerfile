FROM python:3.9-slim

RUN pip3 install flask mysql-connector-python gunicorn

WORKDIR /app

COPY ponydb.py ./
COPY templates templates/

ENV SECRET_KEY=4a934945892d152be33a8423c5aa87d4
ENV DB_HOST=127.0.0.1
ENV DB_USER=iheartponies
ENV DB_PASS=224beabe72313014d9a8fe9ab84e0b75
ENV DB=ponies
ENV FLAG=uiuctf{wh0ops_th1s_on3_was_harder_r1ght_9fa2b}

EXPOSE 1337

CMD mount -t tmpfs none /tmp && python3 /app/ponydb.py
