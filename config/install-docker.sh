#!/bin/bash

echo "Install Docker"
sleep 10

sudo apt update

sudo apt -y install ca-certificates curl gnupg lsb-release

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt update

sudo apt -y install docker-ce docker-ce-cli containerd.io

sudo usermod -aG docker ubuntu

sudo apt install -y docker-compose

echo ""
echo "------------------------------------------------------------------------------------------"
echo "Docker and Docker-compose Instaled"
docker --version
echo ""
echo "------------------------------------------------------------------------------------------"
echo ""
