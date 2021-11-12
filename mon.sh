#!/bin/zsh
sudo airodump-ng \
  --band abg \
  --write results/full \
  --write-interval 10 \
  --output-format csv\
  --update 10 \
  wlan0
        