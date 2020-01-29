#!/bin/bash

install() {
  curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
  echo 'deb [arch=amd64] https://download.docker.com/linux/debian buster stable' > /etc/apt/sources.list.d/docker.list
  sudo apt-get update -y

#   sudo apt-get install lxc-docker
  apt-get install docker-ce
  docker pull alexeiled/docker-oracle-xe-11g
}

run() {
  docker run -d -p 49160:22 -p 49161:1521 -p 49162:8080 alexeiled/docker-oracle-xe-11g
}

if [[ $1 == 'i' ]]; then
    install
elif [[ $1 == 'r' ]]; then
    run
fi
