Real-Time SCADA Simulation & Visualization

Simulates real-time electrical substation data and visualizes it using Grafana dashboards powered by InfluxDB and Python. This project mimics SCADA/EMS telemetry to showcase operational technology (OT) data pipelines, real-time observability, and dashboard development.

🔧 Tech Stack

Python (data simulation & streaming)

InfluxDB 2.x (time-series database)

Grafana (dashboard and visualization)

Docker + Docker Compose (containerized deployment)

⚡ Features

Simulates telemetry data for 3 substations: Voltage, Current, Frequency, Load

Streams data every 5 seconds to InfluxDB using Python

Visualizes metrics in real-time using Grafana + Flux queries

Includes tags (e.g., substation name) and timestamped fields for full SCADA-like structure

Fully containerized: launch with a single command

📁 Project Structure
scada_simulation/
│
├── docker-compose.yml        # Sets up InfluxDB and Grafana
├── requirements.txt          # Python dependencies
├── scada_simulation.py       # Python script to simulate and write data
└── README.md                 # This file

🚀 Getting Started


2. Launch InfluxDB + Grafana via Docker
docker-compose up -d


InfluxDB → http://localhost:8086

Grafana → http://localhost:3000

Default Grafana credentials: admin / admin (change after login)

3. Set Up InfluxDB (first-time only)

Log into InfluxDB UI

Create:

Organization: my-org

Bucket: scada_bucket

Token: (copy it and paste into your Python script)

4. Install Python Dependencies
pip install -r requirements.txt

5. Run the Data Simulation
python scada_simulation.py


You’ll see output like:

Wrote data for 3 substations.


Data is streamed every 5 seconds into InfluxDB.

6. Set Up Grafana Dashboard

In Grafana, add InfluxDB as a data source

Use Flux queries to visualize fields like voltage, current, frequency, load

Example Flux query:

from(bucket: "scada_bucket")
  |> range(start: -1h)
  |> filter(fn: (r) => r._measurement == "scada_metrics")
  |> filter(fn: (r) => r._field == "voltage")
  |> filter(fn: (r) => r.substation == "Substation_A")
  |> aggregateWindow(every: 10s, fn: mean)
  |> yield(name: "mean")

📊 Sample Metrics
Substation	Voltage (V)	Current (A)	Frequency (Hz)	Load (MW)
Substation_A	115.4	32.1	50.1	48.2
Substation_B	119.7	28.9	49.9	55.4
Substation_C	113.3	44.6	50.3	62.7
📌 Use Cases

Demonstrates a real-world OT data pipeline for control centers

Mimics data from SCADA/EMS platforms in energy and utilities

Useful for interview projects, dashboards, or portfolio building

🧠 Learnings

Built real-time dashboards for operational metrics

Gained experience with time-series databases and Flux querying

Learned how OT visibility is achieved using modern data stacks