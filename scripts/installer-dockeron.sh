#!/bin/bash

WHERE=/root/install
DIR_NAME=curiouspablo-bot
BASE_DIR=$WHERE/$DIR_NAME
IMAGE_NAME=curious-pablo
CONTAINER_NAME=curious-pablo
TAG_NAME=latest

set -o errexit

echo "CDing into $WHERE"
cd $WHERE
echo "Removing existing files in $BASE_DIR"
rm -rvf $BASE_DIR
echo "Cloning master"
git clone git@github-deploy-bot:pablo/curiouspablo-bot.git $DIR_NAME
cd $BASE_DIR
echo "Current directory is $(pwd)"
echo "Building container"
docker build -t $IMAGE_NAME .
echo "Stopping container if exists"
docker stop $CONTAINER_NAME || true
echo "Removing container if exists"
docker rm $CONTAINER_NAME || true
echo "Starting new container"
docker run -d --mount source=bot-data,target=/bot/data --mount type=bind,source=$WHERE/curious-pablo/local_settings.py,target=/bot/local_settings.py --name $CONTAINER_NAME $IMAGE_NAME:$TAG_NAME
echo "Removing files"
rm -rvf $BASE_DIR
