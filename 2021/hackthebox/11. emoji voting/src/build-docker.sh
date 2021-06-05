#!/bin/bash
docker build --tag=web_emoji_voting .
docker run -p 1337:1337 --rm --name=web_emoji_voting -it web_emoji_voting
