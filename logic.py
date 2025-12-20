from ping3 import ping
from logger import log_results  # import the function from logger.py
import configparser

# Load config
config = configparser.ConfigParser()
config.read("config.ini")

# Network
ROUTER_IP = config.get("NETWORK", "ROUTER_IP")
PUBLIC_IP = config.get("NETWORK", "PUBLIC_IP")
LAN_DEVICES = [ip.strip() for ip in config.get("NETWORK", "LAN_DEVICES").split(",")]
PING_COUNT = config.getint("NETWORK", "PING_COUNT")
TIMEOUT = config.getint("NETWORK", "TIMEOUT")

# Logging
LOG_DIR = config.get("LOGGING", "LOG_FILE")

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