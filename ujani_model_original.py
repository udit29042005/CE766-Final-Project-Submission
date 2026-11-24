"""
Ujani Reservoir (Upper Bhima) monthly water-balance model - CE766 final project
Input : data/ujani_monthly.csv  with columns
        date (YYYY-MM-01), inflow_mcm, pan_evap_mm, storage_obs_mcm (month-end, observed)
Output: results/monthly_results.csv, fig1_storage.png, fig2_reliability.png
Priority: municipal -> irrigation -> environmental flow.
"""
import pandas as pd, numpy as np, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---- Published reservoir parameters (CWC / Maharashtra WRD) ----
S_MAX, S_DEAD, A_FRL = 3320.0, 1802.0, 337.0      # MCM, MCM, km2
# ---- Annual demand assumptions (MCM) - REPLACE with MWRRA/WRD allocations ----
ANNUAL = {"mun": 300.0, "irr": 2000.0, "env": 110.0}   # total ~2,410 MCM utilisation
# Monthly distribution weights (sum to 1), Jan..Dec
W_MUN = np.full(12, 1/12)
W_IRR = np.array([.10,.10,.10,.08,.06,.02,.02,.04,.10,.14,.14,.10]); W_IRR /= W_IRR.sum()
W_ENV = np.full(12, 1/12)

df = pd.read_csv("data/ujani_monthly.csv", parse_dates=["date"]).sort_values("date")
S = df["storage_obs_mcm"].iloc[0]            # start from observed storage
rows = []
for _, r in df.iterrows():
    m = r["date"].month - 1
    A = A_FRL * (S / S_MAX) ** (2 / 3)       # simple area-storage relation
    E = min(A * r["pan_evap_mm"] * 0.7 / 1000, max(S - S_DEAD, 0))  # km2*mm/1000 = MCM
    avail = max(S + r["inflow_mcm"] - E - S_DEAD, 0)   # water above dead storage
    d = {"mun": ANNUAL["mun"] * W_MUN[m], "irr": ANNUAL["irr"] * W_IRR[m],
         "env": ANNUAL["env"] * W_ENV[m]}
    rel = {}
    for k in ("mun", "irr", "env"):          # fixed priority
        rel[k] = min(d[k], avail); avail -= rel[k]
    S_new = S + r["inflow_mcm"] - E - sum(rel.values())
    spill = max(S_new - S_MAX, 0); S_new = min(S_new, S_MAX)
    rows.append({"date": r["date"], "storage_sim": S_new, "evap": E, "spill": spill,
                 **{f"dem_{k}": d[k] for k in d}, **{f"rel_{k}": rel[k] for k in rel},
                 "storage_obs": r["storage_obs_mcm"]})
    S = S_new

out = pd.DataFrame(rows)
os.makedirs("results", exist_ok=True)
out.to_csv("results/monthly_results.csv", index=False)

# ---- Measures: annual volumetric reliability per sector ----
out["year"] = out["date"].dt.year
ann = out.groupby("year")[[c for c in out.columns if c.startswith(("dem_", "rel_"))]].sum()
for k in ("mun", "irr", "env"):
    ann[f"sat_{k}"] = 100 * ann[f"rel_{k}"] / ann[f"dem_{k}"]
ann.to_csv("results/annual_results.csv")

# ---- Figure 1: simulated vs observed storage ----
fig, ax = plt.subplots(figsize=(10, 4.5))
ax.plot(out["date"], out["storage_obs"], label="Observed storage (CWC/India-WRIS)", lw=2)
ax.plot(out["date"], out["storage_sim"], "--", label="Simulated storage (model)", lw=2)
ax.axhline(S_DEAD, color="red", ls=":", label="Dead storage (1,802 MCM)")
ax.set_xlabel("Month"); ax.set_ylabel("Storage (MCM)")
ax.set_title("Figure 1: Ujani Reservoir monthly storage, observed vs simulated")
ax.legend(); fig.tight_layout(); fig.savefig("results/fig1_storage.png", dpi=200)

# ---- Figure 2: annual demand satisfaction ----
fig, ax = plt.subplots(figsize=(10, 4.5))
x = np.arange(len(ann)); w = 0.27
for i, (k, lab) in enumerate([("mun", "Municipal"), ("irr", "Irrigation"), ("env", "Environmental flow")]):
    ax.bar(x + (i - 1) * w, ann[f"sat_{k}"], w, label=lab)
ax.set_xticks(x); ax.set_xticklabels(ann.index)
ax.set_xlabel("Year"); ax.set_ylabel("Demand satisfied (%)"); ax.set_ylim(0, 105)
ax.set_title("Figure 2: Annual demand satisfaction by sector under the baseline priority rule")
ax.legend(); fig.tight_layout(); fig.savefig("results/fig2_reliability.png", dpi=200)
print(ann.round(1))
