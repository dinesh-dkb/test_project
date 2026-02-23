import boto3
import json
import random
import time
from datetime import datetime

# Configure boto3 to talk to LocalStack Kinesis
kinesis = boto3.client(
    "kinesis",
    aws_access_key_id="test",
    aws_secret_access_key="test",
    region_name="us-east-1",
    endpoint_url="http://localhost:4566"  # LocalStack endpoint
)

STREAM_NAME = "vehicle-telematics"

# Ensure stream exists (create if not already created)
def create_stream():
    try:
        kinesis.create_stream(StreamName=STREAM_NAME, ShardCount=1)
        print(f"Stream {STREAM_NAME} created.")
        # Wait until stream is active
        waiter = kinesis.get_waiter("stream_exists")
        waiter.wait(StreamName=STREAM_NAME)
    except kinesis.exceptions.ResourceInUseException:
        print(f"Stream {STREAM_NAME} already exists.")

# Generate random vehicle telemetry data
def generate_vehicle_data(vehicle_id):
    return {
        "vehicle_id": vehicle_id,
        "timestamp": datetime.utcnow().isoformat(),
        "speed": round(random.uniform(0, 120), 2),          # km/h
        "fuel_level": round(random.uniform(10, 100), 2),    # percentage
        "engine_temp": round(random.uniform(70, 120), 2),   # Celsius
        "latitude": round(random.uniform(12.90, 13.10), 6), # Example coords near Chennai
        "longitude": round(random.uniform(80.10, 80.30), 6)
    }

# Push data into Kinesis
def push_to_kinesis(data):
    response = kinesis.put_record(
        StreamName=STREAM_NAME,
        Data=json.dumps(data),
        PartitionKey=data["vehicle_id"]
    )
    print(f"Record sent: {data['vehicle_id']} | SequenceNumber: {response['SequenceNumber']}")

if __name__ == "__main__":
    create_stream()
    vehicle_ids = []
    for i in range(35):
        i = i + 10
        vehicle_ids.append(f'BUS1{i}')
    # vehicle_ids = ["CAR-101", "CAR-102", "CAR-103"]

    # Continuously simulate telemetry
    while True:
        for vid in vehicle_ids:
            record = generate_vehicle_data(vid)
            push_to_kinesis(record)
        time.sleep(2)  # send every 2 seconds