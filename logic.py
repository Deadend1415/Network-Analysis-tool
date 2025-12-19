from ping3 import ping
from logger import log_results  # import the function from logger.py

ROUTER_IP = "192.168.0.1"
PUBLIC_IP = "8.8.8.8"
LAN_DEVICES = ["192.168.0.46","192.168.0.98","192.168.0.174","192.168.0.97","192.168.0.163","192.168.0.237","192.168.0.122","192.168.0.16"]
TIMEOUT = 2  # seconds
PING_COUNT = 15
LOG_FILE = "router_ping.csv"

# Combine all targets into one list
targets = [ROUTER_IP] + [PUBLIC_IP]

# Add only the first 3 LAN devices that respond
count = 0
for device in LAN_DEVICES:

    if ping(device, timeout=TIMEOUT, unit="ms"): # only non-false, non-zero values
        targets.append(device)
        count += 1
        
    if count >= 3:
        break

# Dictionary to hold results
results = {}

for target in targets:
    probes = []
    for _ in range(PING_COUNT):
        delay = ping(target, timeout=TIMEOUT, unit="ms")
        probes.append(delay)
        #end for
        
    #probes for the target have been filled  
    
    results[target] = {
        "min": round(min(probes), 2),
        "max": round(max(probes), 2),
        "avg": round(sum(probes) / len(probes), 2)
    }
    print(target, ":", results[target])
#end for

# Call the logger
log_results(results)
print("Ping results logged.")