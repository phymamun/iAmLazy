#!/bin/bash

install() {
  sudo apt install curl -y
  curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
  echo 'deb [arch=amd64] https://download.docker.com/linux/debian buster stable' > /etc/apt/sources.list.d/docker.list
  sudo apt-get update -y

  # sudo apt-get install lxc-docker
  apt-get install docker-ce -y
  docker login
  # docker pull alexeiled/docker-oracle-xe-11g
  git clone https://github.com/orangehrm/docker-oracle-xe-11g.git ../../docker-oracle
  cd ../../docker-oracle
  sudo systemctl start docker
  sudo docker image build -t oracle-xe:1.0 .
  # sudo docker run -d --shm-size=2g -p 1521:1521 -p 8080:8080 alexeiled/docker-oracle-xe-11g
  sudo docker container run --shm-size=2g --publish 1521:1521 --publish 8000:8080 --detach --name oracle oracle-xe:1.0
  echo -e "Connect database with following setting:
    hostname: localhost
    port: 1521
    sid: xe
    username: system
    password: oracle

    Password for SYS user
    oracle

    Connect to Oracle Application Express web management console with following settings:
    url: http://localhost:8080/apex
    workspace: internal
    user: admin
    password: oracle

    Do not forget to change admin password!"

}

run() {
  sudo docker container run --shm-size=2g --publish 1521:1521 --publish 8000:8080 --detach --name oracle oracle-xe:1.0
}

if [[ $1 == 'i' ]]; then
    install
elif [[ $1 == 'r' ]]; then
    run
fi
