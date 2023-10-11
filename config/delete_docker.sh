#!/bin/bash

echo "Delete containers"
PS=$(docker ps -qa)
docker rm -f "$PS"
echo
echo "Delete images"
IMG=$(docker images -q)
docker rmi -f "$IMG"
echo
echo "Delete Volume"
VL=$(docker volume ls -q)
docker volume rm -f "$VL"