#!/bin/bash

# Update Cache
sudo apt update -y

# Install the Must have packages
sudo apt install -y git libibus-1.0-dev ibus autotools-dev automake autoconf gjs gir1.2-ibus-1.0

# Clone the base repo
git clone git://github.com/sarim/ibus-avro.git
cd ibus-avro

# Make Configurations
aclocal && autoconf && automake --add-missing
./configure --prefix=/usr

# Install using cmake
sudo make install

# Make .deb
# sudo checkinstall

# Removing downloaded repo
cd ..
rm -rf ibus-avro

# iBus must be restarted
ibus restart

exit