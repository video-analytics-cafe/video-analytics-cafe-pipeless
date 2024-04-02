#!/bin/sh

# Wait for Kafka to be ready
echo "Waiting for Kafka to be ready..."
while ! nc -z kafka1 9092; do
  sleep 1
done

echo "Kafka is up, waiting an additional 10 seconds..."
sleep 10

## Execute the original command
#exec "$@"
