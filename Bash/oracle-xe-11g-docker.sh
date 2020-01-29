#!/bin/bash

install() {
  sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 36A1D7869245C8950F966E92D8576A8BA88D21E9
  sudo sh -c "echo deb http://get.docker.io/ubuntu docker main > /etc/apt/sources.list.d/docker.list"
  sudo apt-get update

  sudo apt-get install lxc-docker
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
