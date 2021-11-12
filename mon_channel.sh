#!/bin/zsh
sudo airodump-ng \
  --channel $1 \
  --write results/channel-$1 \
  --write-interval 10 \
  --output-format csv\
  --update 10 \
  wlan0
        