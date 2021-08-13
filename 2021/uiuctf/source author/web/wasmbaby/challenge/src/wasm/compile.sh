#!/bin/bash
# install emscripten 
source ~/emsdk/emsdk_env.sh
emcc main.c -o index.html
