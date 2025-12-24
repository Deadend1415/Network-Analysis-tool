import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv(
    "ping_log.csv",
    header=None,
    names=["time", "ip", "min", "max", "avg"],
    parse_dates=["time"],
    dayfirst=True
)

df = df.sort_values("time")

metrics = ["min", "max", "avg"]

for metric in metrics:
    plt.figure()

    for ip, group in df.groupby("ip"):
        plt.plot(group["time"], group[metric], label=ip)

    plt.title(f"{metric.upper()} latency over time by IP")
    plt.xlabel("Time")
    plt.ylabel("Latency (ms)")
    plt.legend(fontsize="small", ncol=2)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
