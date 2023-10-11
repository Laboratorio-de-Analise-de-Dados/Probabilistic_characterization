#!/bin/bash

echo "Install Tree"
sleep 10

sudo apt update
sudo apt -y install tree

echo ""
echo "------------------------------------------------------------------------------------------"
echo "Tree Instaled"
tree --version
echo ""
echo "------------------------------------------------------------------------------------------"
echo ""
