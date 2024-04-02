import json
import os

from kafka import KafkaProducer

KAFKA_HOST = os.getenv("KAFKA_HOST", "localhost")
KAFKA_PORT = os.getenv("KAFKA_PORT", "9092")
KAFKA_BROKER_URL = f"{KAFKA_HOST}:{KAFKA_PORT}"


def init():
    return {
        "kafka-producer": KafkaProducer(
            bootstrap_servers=KAFKA_BROKER_URL,
            value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        )
    }
