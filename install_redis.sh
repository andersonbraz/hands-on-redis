#!/bin/bash
mkdir -p ~/Apps/redis && cd ~/Apps/redis
curl -O http://download.redis.io/redis-stable.tar.gz
tar xzvf redis-stable.tar.gz
cd redis-stable
make
sudo make install
