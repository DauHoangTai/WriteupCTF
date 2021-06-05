#!/bin/bash
docker rm -f web_pcalc
docker build -t web_pcalc . && \
docker run --name=web_pcalc --rm -p1337:80 -it web_pcalc