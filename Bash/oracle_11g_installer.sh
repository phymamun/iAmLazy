#!/bin/bash

echo -e "Installing Oracle 11g XE..."
echo "deb http://oss.oracle.com/debian unstable main non-free" | sudo tee  /etc/apt/sources.list

wget http://oss.oracle.com/el4/RPM-GPG-KEY-oracle -O- | sudo apt-key add - 
sudo apt-get update
sudo apt-get install oracle-xe