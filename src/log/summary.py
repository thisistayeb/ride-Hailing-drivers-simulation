"""This script appends a summary report of each driver in the `summary` file"""
import sys

import pandas as pd

filename = sys.argv[-1]
df = pd.read_csv(f"{filename}")

SNAPP_COMMISION = 0.15
TAPSI_COMMISION = 0.15

total_minutes = (
    sum(df["minutes_to_origin"])
    + sum(df["minutes_to_dest"])
    + sum(df["minutes_for_wait"])
)
total_hours = round(total_minutes / 60.0, 2)
total_km = round(sum(df["km_to_origin"]) + sum(df["km_to_dest"]), 2)
total_snapp_income = round(sum(df["snapp_income"]) * (1 - SNAPP_COMMISION), 2)
total_tapsi_income = round(sum(df["tapsi_income"]) * (1 - TAPSI_COMMISION), 2)
per_hour_snapp = round(total_snapp_income / (total_hours - 0.5), 2)
per_hour_tapsi = round(total_tapsi_income / (total_hours - 0.5), 2)
per_km_snapp = round(total_snapp_income / (total_km), 2)
per_km_tapsi = round(total_tapsi_income / (total_km), 2)

with open("summary", "a", encoding="UTF-8") as summary:
    summary.writelines(
        f"{per_hour_snapp},{per_hour_tapsi},{per_km_snapp},{per_km_tapsi},{total_snapp_income},{total_tapsi_income},{total_hours},{total_km}\n"
    )
