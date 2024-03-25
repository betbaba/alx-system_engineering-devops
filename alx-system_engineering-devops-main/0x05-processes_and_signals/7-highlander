#!/usr/bin/env bash
#diplays a message and another message if SIGTERM signal is recieved
i=true

while [ $i ]
do
  echo "To inifinity and beyond"
  sleep 2
  trap 'echo "I am invincible!!!"' SIGTERM
done
