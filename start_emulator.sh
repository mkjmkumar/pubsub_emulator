#!/bin/bash
#PUBSUB

gcloud beta emulators pubsub start --host-port=0.0.0.0:8085 
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start PubSub emulator: $status"
  exit $status
fi