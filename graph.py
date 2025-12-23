import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ping_log.csv",
                 names=["timestamp","ip","min","max","avg"])
df["timestamp"] = pd.to_datetime(df["timestamp"], format="%d-%m-%Y %H:%M:%S")

plt.figure(figsize=(12,6))  # make plot bigger
for ip in df["ip"].unique():
    device_data = df[df["ip"] == ip]
    plt.plot(device_data["timestamp"], device_data["avg"], label=ip)

plt.xlabel("Time")
plt.ylabel("Average Ping (ms)")
plt.title("Ping Over Time")
plt.legend()

# Improve x-axis formatting
plt.gcf().autofmt_xdate()  # rotates dates nicely
plt.show()

