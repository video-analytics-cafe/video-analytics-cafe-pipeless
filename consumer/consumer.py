import json
import logging
import os
import signal
import threading

from kafka import KafkaConsumer
from dotenv import load_dotenv
from sqlalchemy import text
from database import get_db

load_dotenv()

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
KAFKA_GROUP_ID = os.getenv("KAFKA_GROUP_ID", "0")

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
            # Insert user_data into the database
            db = next(get_db())
            # try:
            #     logger.info(f"DATA: {json.dumps(user_data, indent=2)}")
            # except Exception as e:
            #     logger.error(f"Error inserting user data: {e}")

            # consumer.commit()
            
            try:
                # extract data from user_data json
                # iterate through each obj on image if multiple objects are present
                n_obj = len(user_data['obj_track_ids'])
                for i in range(n_obj):
                    id = user_data['_id']
                    datetime = user_data['_datetime']
                    obj_track_id = user_data['obj_track_ids'][i]
                    label = user_data['labels'][i]
                    score = user_data['scores'][i]
                    bbox = user_data['bboxes'][i]
                    
                    insert_query = f"INSERT INTO logs (ids, msg_datetime, obj_track_id, labels, scores, left_coords, upper_coords, right_coords, down_coords) VALUES ('{id}', '{datetime}', {obj_track_id}, '{label}', {score}, {bbox[0]}, {bbox[1]}, {bbox[2]}, {bbox[3]})"
                    logger.info(f"\n\tINSERT QUERY: {text(insert_query)}")
                    new_user = db.execute(text(insert_query))
                    
                    db.commit()  # Commit the transaction

                logger.info(f"Inserted: {json.dumps(user_data)}")
            except Exception as e:
                logger.error(f"Error inserting user data: {e}")
                db.rollback()
            finally:
                db.close()

            consumer.commit()


if __name__ == "__main__":
    signal.signal(signal.SIGINT, shutdown)
    threading.Thread(target=start_consumer).start()