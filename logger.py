import csv
from datetime import datetime

def log_results(results, log_file="ping_log.csv"):
    """
    Logs the ping results dictionary to a CSV file.
    Each row: timestamp, IP, min, max, avg, std, count, failed
    """
    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    
    with open(log_file, mode="a", newline="") as f:
        writer = csv.writer(f)
        for target, metrics in results.items():
            writer.writerow([
                timestamp,
                target,
                metrics.get("min"),
                metrics.get("max"),
                metrics.get("avg")
            ])
