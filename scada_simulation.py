import os
import time
import random
from datetime import datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision
from dotenv import load_dotenv

load_dotenv()

# InfluxDB config
url = "http://localhost:8086"
token = os.getenv("INFLUXDB_TOKEN")      
org = "my-org"                
bucket = "scada_bucket"

# Create InfluxDB client
client = InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api()

substations = ["Substation_A", "Substation_B", "Substation_C"]

def generate_data():
    for substation in substations:
        voltage = random.uniform(110, 130)     # volts
        current = random.uniform(10, 50)       # amps
        frequency = random.uniform(49.5, 50.5) # Hz
        load = random.uniform(20, 80)          # MW

        point = (
            Point("scada_metrics")
            .tag("substation", substation)
            .field("voltage", voltage)
            .field("current", current)
            .field("frequency", frequency)
            .field("load", load)
            .time(datetime.utcnow(), WritePrecision.NS)  # Add timestamp here
        )
        yield point

def main():
    print("Starting SCADA data simulation. Press Ctrl+C to stop.")
    try:
        while True:
            points = list(generate_data())
            write_api.write(bucket=bucket, org=org, record=points)
            print(f"Wrote data for {len(substations)} substations.")
            time.sleep(5)  # send data every 5 seconds
    except KeyboardInterrupt:
        print("Simulation stopped.")

if __name__ == "__main__":
    main()
