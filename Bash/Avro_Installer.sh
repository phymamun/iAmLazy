#!/bin/bash

# Install the Must have packages
sudo apt install -y git libibus-1.0-0 libibus-1.0-dev ibus automake autoconf gjs gir1.2-gjsdbus-1.0 gir1.2-ibus-1.0

git clone git://github.com/sarim/ibus-avro.git
cd ibus-avro
aclocal && autoconf && automake --add-missing
./configure --prefix=/usr
sudo make install

cd ..
rm -rf ibus-avro