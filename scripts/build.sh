#!/bin/bash

IMG_NAME=docker.roshka.com/pablo/curious-pablo

docker build -t $IMG_NAME ..
docker push $IMG_NAME