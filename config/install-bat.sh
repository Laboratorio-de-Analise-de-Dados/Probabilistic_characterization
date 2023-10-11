#!/bin/bash

echo "Install Bat"
sleep 10

wget https://github.com/sharkdp/bat/releases/download/v0.9.0/bat_0.9.0_amd64.deb
sudo dpkg -i bat_0.9.0_amd64.deb

echo ""
echo "------------------------------------------------------------------------------------------"
echo "Bat Installed"
bat --version

echo ""
echo "------------------------------------------------------------------------------------------"
echo ""
