#!/bin/bash
###
# File: c-cpp.bash
# Created: Sunday, 2nd February 2020 9:46:41 pm
# Author: Rakibul Yeasin (ryeasin03@gmail.com)
# -----
# Last Modified: Wednesday, 5th February 2020 1:24:27 am
# Modified By: Rakibul Yeasin (ryeasin03@gmail.com)
# -----
# Copyright (c) 2020 Slishee
###

if [[ $1 == 'c' ]]; then
    gcc -c $2 -o out
    chmod +x ./out
    ./out
elif [[ $1 == 'cpp' ]]; then
    g++ -c "$2" -o out
    chmod +x ./out
    ./out
fi