"""Display and validate the Week10 semantic topic contract."""

import json
from datetime import datetime, timezone
from uuid import uuid4

TOPIC_NAME = "/vlm/semantic_description"
MESSAGE_TYPE = "std_msgs/msg/String"
QOS_DEPTH = 10
REQUIRED_FIELDS = {
    "schema_version",
    "observation_id",
    "timestamp_utc",
    "task",
    "status",
    "source_image",
    "question",
    "answer",
    "model_id",
}


def main() -> None:
    payload = {
        "schema_version": "1.0",
        "observation_id": str(uuid4()),
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "task": "caption",
        "status": "ok",
        "source_image": "outputs/camera.jpg",
        "question": None,
        "answer": "a desk with a laptop",
        "model_id": "Salesforce/blip-image-captioning-base",
    }
    missing = sorted(REQUIRED_FIELDS - payload.keys())
    print("topic:", TOPIC_NAME)
    print("message type:", MESSAGE_TYPE)
    print("QoS depth:", QOS_DEPTH)
    print("contract valid:", not missing)
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
