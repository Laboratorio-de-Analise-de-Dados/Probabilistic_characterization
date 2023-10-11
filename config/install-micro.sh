#!/bin/bash

echo "Install Micro"
sleep 10

sudo apt update
sudo apt -y install micro

echo ""
echo "------------------------------------------------------------------------------------------"
echo "Micro Instaled"
micro --version
echo ""
echo "------------------------------------------------------------------------------------------"
echo ""
