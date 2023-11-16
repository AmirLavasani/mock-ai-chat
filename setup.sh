#!/bin/bash

conda create --name chat-server python=3.11

make install-deps
make install-dev-deps

make run