import requests
import pandas as pd
from datetime import datetime
import os

URL = "https://velib-metropole-opendata.smovengo.cloud/opendata/Velib_Metropole/station_status.json"

def fetch_data():
    response = requests.get(URL, timeout=10)
    response.raise_for_status()
    data = response.json()["data"]["stations"]
    return pd.DataFrame(data)

def save_snapshot():
    df = fetch_data()
    df["snapshot_time"] = datetime.now()

    filename = "velib_history.csv"

    if not os.path.exists(filename):
        df.to_csv(filename, index=False)
    else:
        df.to_csv(filename, mode="a", header=False, index=False)

    print("Snapshot ajouté.")

if __name__ == "__main__":
    save_snapshot()
