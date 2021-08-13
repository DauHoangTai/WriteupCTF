FROM python:3

RUN mkdir /usr/src/app
WORKDIR /usr/src/app

# create user
RUN groupadd chalusr
RUN useradd -ms /bin/bash -g chalusr chalusr

# pip
COPY ./src/webserver/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# chal files
RUN mkdir static templates
COPY ./src/wasm/index.html ./static
COPY ./src/wasm/index.js ./static
COPY ./src/wasm/index.wasm ./static

COPY src/webserver/server.py .
RUN chmod 775 ./server.py

USER chalusr
CMD [ "python3", "./server.py" ]

