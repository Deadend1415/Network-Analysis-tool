""" from ping3 import ping
from datetime import datetime
import statistics

ROUTER_IP = "192.168.0.1"
LOG_FILE = "router_ping.csv"
PING_COUNT = 5
TIMEOUT = 2  # seconds

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
latencies = []

for _ in range(PING_COUNT):
    delay = ping(ROUTER_IP, timeout=TIMEOUT, unit="ms")
    if delay is not None:
        latencies.append(delay)

with open(LOG_FILE, "a") as f:
    if latencies:
        avg = round(statistics.mean(latencies), 2)
        f.write(f"{timestamp},{ROUTER_IP},{avg}\n")
    else:
        f.write(f"{timestamp},{ROUTER_IP},FAIL\n")
 """
print("Hello world")