"""Reproduce the descriptive analysis and figures for the supplied Ujani CWC weekly workbook.
This is NOT the original monthly water-balance simulation: the workbook has no inflow,
evaporation, sectoral demand or release series.
"""
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "Ujani_Reservoir_Weekly_Storage_Data-v3.xlsx"
OUT = ROOT

raw = pd.read_excel(SOURCE, sheet_name="Ujani_Weekly_Data", header=None)
columns = [
    "bulletin_date", "latest_date_available", "frl_m", "live_capacity_bcm",
    "current_level_m", "current_live_storage_bcm", "current_storage_pct",
    "last_year_level_m", "last_year_live_storage_bcm", "last_year_storage_pct",
    "normal_storage_bcm", "normal_storage_pct", "this_year_vs_last_year_pct",
    "this_year_vs_normal_pct", "bulletin_storage_change_bcm", "bulletin_level_change_m"
]
df = raw.iloc[5:29, :16].copy()
df.columns = columns
df = df[df.bulletin_date.notna()].copy()
df["bulletin_date"] = pd.to_datetime(df["bulletin_date"], dayfirst=True, errors="coerce")
for col in columns[1:]:
    df[col] = pd.to_numeric(df[col], errors="coerce")
df = df.dropna(subset=["bulletin_date"]).sort_values("bulletin_date")
for src, dst in [
    ("current_live_storage_bcm", "current_live_storage_mcm"),
    ("last_year_live_storage_bcm", "last_year_live_storage_mcm"),
    ("normal_storage_bcm", "normal_storage_mcm")
]:
    df[dst] = df[src] * 1000
df.to_csv(OUT / "ujani_cleaned_weekly_data.csv", index=False)

plt.figure(figsize=(11, 5.6))
plt.plot(df.bulletin_date, df.current_live_storage_mcm, marker="o", label="Current season (2024–25)")
plt.plot(df.bulletin_date, df.last_year_live_storage_mcm, marker="s", label="Previous season (2023–24)")
plt.plot(df.bulletin_date, df.normal_storage_mcm, marker="^", label="10-year normal")
plt.ylabel("Live storage (MCM)"); plt.xlabel("CWC bulletin date")
plt.title("Ujani Reservoir: weekly live storage comparison")
plt.grid(True, alpha=.25); plt.legend(); plt.xticks(rotation=35, ha="right")
plt.tight_layout(); plt.savefig(OUT / "Figure_1_Weekly_Storage_Comparison.png", dpi=220); plt.close()

plt.figure(figsize=(11, 5.2))
plt.plot(df.bulletin_date, df.current_storage_pct, marker="o", label="Current storage (% of live capacity)")
plt.plot(df.bulletin_date, df.normal_storage_pct, marker="^", label="10-year normal (% of live capacity)")
plt.ylabel("Storage (% of live capacity at FRL)"); plt.xlabel("CWC bulletin date")
plt.title("Ujani Reservoir: current storage relative to 10-year normal")
plt.ylim(-3, 108); plt.grid(True, alpha=.25); plt.legend()
plt.xticks(rotation=35, ha="right"); plt.tight_layout()
plt.savefig(OUT / "Figure_2_Storage_Percentage.png", dpi=220); plt.close()

print("Bulletins:", len(df))
print("Start:", df.iloc[0].bulletin_date.date(), df.iloc[0].current_live_storage_mcm, "MCM")
print("End:", df.iloc[-1].bulletin_date.date(), df.iloc[-1].current_live_storage_mcm, "MCM")
print("First zero-storage bulletin:", df.loc[df.current_live_storage_mcm.eq(0), "bulletin_date"].min())
print("First bulletin below normal:", df.loc[df.current_live_storage_bcm < df.normal_storage_bcm, "bulletin_date"].min())
