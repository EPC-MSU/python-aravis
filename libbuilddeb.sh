#!/usr/bin/env bash
g++ -c -fPIC lib.cpp `pkg-config --cflags aravis-0.8`
g++ -shared -o libara.so lib.o `pkg-config --libs aravis-0.8`
