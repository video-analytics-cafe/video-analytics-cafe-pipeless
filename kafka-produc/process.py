import hashlib
import json
import os
from datetime import datetime

KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "event_server")


def on_send_success(record_metadata):
    print(
        f"Message delivered to {record_metadata.topic} [{record_metadata.partition}]"
    )


def on_send_error(excp):
    print(f"errback: {str(excp)}")


def hash_json(json_object: dict) -> bytes:
    json_string = json.dumps(json_object, sort_keys=True)

    hash_object = hashlib.sha256(json_string.encode('utf-8'))
    hash_string = hash_object.hexdigest()

    return hash_string.encode('utf-8')


def hook(frame_data, context):
    kafka_producer = context['kp']
    frame = frame_data['modified']
    user_data = frame_data['user_data']
    user_data["_datetime"] = datetime.utcnow().isoformat()
    key_ = hash_json(user_data)
    kafka_producer.send(
        KAFKA_TOPIC, key=key_, value=user_data
    ).add_callback(on_send_success).add_errback(on_send_error)

    kafka_producer.flush()
    frame_data['modified'] = frame
