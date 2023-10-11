#!/bin/bash

echo "Install Fd-find"
sleep 10

sudo apt update
sudo apt -y install fd-find

echo ""
echo "------------------------------------------------------------------------------------------"
echo "FD-Find Instaled"
fdfind --version
echo ""
echo "------------------------------------------------------------------------------------------"
echo ""
