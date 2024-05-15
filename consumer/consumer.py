import json
import logging
import os
import signal
import threading

from kafka import KafkaConsumer

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)

# Kafka configuration
# KAFKA_HOST = os.getenv("KAFKA_HOST", "localhost")
# KAFKA_PORT = os.getenv("KAFKA_PORT", "9092")
# KAFKA_BROKER_URL = f"{KAFKA_HOST}:{KAFKA_PORT}"
KAFKA_BROKER_URL = os.getenv("KAFKA_BROKER_URL", "localhost:9092")

KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "event_server")
KAFKA_GROUP_ID = os.getenv("KAFKA_GROUP_ID")

# Kafka Consumer Setup using kafka-python
consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=KAFKA_BROKER_URL,
    group_id=KAFKA_GROUP_ID,
    auto_offset_reset='earliest',
    enable_auto_commit=False,
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)


def shutdown(signal, frame):
    logger.info("Shutting down consumer...")
    consumer.close()
    exit(0)


def start_consumer():
    while True:
        for msg in consumer:
            user_data = msg.value
            try:
                logger.info(f"DATA: {json.dumps(user_data, indent=2)}")
            except Exception as e:
                logger.error(f"Error inserting user data: {e}")

            consumer.commit()


if __name__ == "__main__":
    signal.signal(signal.SIGINT, shutdown)
    threading.Thread(target=start_consumer).start()
