#!/bin/bash

# Update Cache
sudo apt update -y

# Install the Must have packages
sudo apt install -y git libibus-1.0-dev ibus autotools-dev automake autoconf gjs gir1.2-ibus-1.0

git clone git://github.com/sarim/ibus-avro.git
cd ibus-avro
aclocal && autoconf && automake --add-missing
./configure --prefix=/usr
sudo make install

cd ..
rm -rf ibus-avro