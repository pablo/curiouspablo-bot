#!/bin/bash

VERSION=0.0.4

IMG_NAME=docker.roshka.com/pablo/curious-pablo:$VERSION

docker build --platform linux/amd64 -t $IMG_NAME ..
docker push $IMG_NAME
