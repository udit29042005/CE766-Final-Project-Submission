
# Ujani Reservoir (Bhima) – CE766 Final Project

## Weekly Storage Stress Assessment Using CWC Data

**Study Area:** Ujani (Bhima) Reservoir, Upper Bhima Basin, Maharashtra, India  
**Observation Period:** 14 November 2024 – 1 May 2025  
**Temporal Resolution:** Weekly  
**Data Source:** Central Water Commission (CWC), Weekly Reservoir Storage Reports

---

## 1. Project Overview

Ujani Reservoir is a major water-storage asset in the Upper Bhima basin. It supports competing water demands, particularly irrigation and municipal supply, while reservoir releases also influence downstream river conditions.

The preliminary project proposed a monthly water-balance model for 2000–2024 to investigate a fixed release-priority rule: municipal supply, followed by irrigation and environmental flow.

However, the available dataset consists of weekly reservoir-storage observations for the 2024–25 season rather than the historical monthly inflow, evaporation, release and sectoral-demand data required for the proposed allocation simulation.

The final analysis therefore examines the observed seasonal storage behaviour of Ujani Reservoir and compares current storage with previous-year storage and the reported ten-year normal. The study retains the original reservoir-management problem and water-allocation motivation while adapting the empirical analysis to the available site-specific observations.

### Research Objectives

1. Analyse the weekly variation in Ujani Reservoir's live storage.
2. Identify when current storage falls below the reported ten-year normal.
3. Identify the occurrence of zero live storage.
4. Compare the current season with previous-year storage and the ten-year normal.
5. Examine the implications of seasonal storage depletion for reservoir management.

---

## 2. Dataset Description

The study uses 24 weekly observations consolidated from Central Water Commission reservoir storage bulletins between 14 November 2024 and 1 May 2025.

The dataset contains:

- Current reservoir level.
- Current live storage (BCM).
- Current storage as a percentage of FRL capacity.
- Previous-year reservoir level and live storage.
- Ten-year normal live storage.
- Ten-year normal storage percentage.
- Weekly changes in reservoir level and storage.

The reported live capacity at FRL is 1.517 BCM, with an FRL of 496.83 m.

Storage values are converted from billion cubic metres (BCM) to million cubic metres (MCM):

\[
Storage_{MCM} = Storage_{BCM} \times 1000
\]

---

## 3. Methodology

A descriptive weekly time-series analysis is used to evaluate reservoir storage behaviour.

The current-season storage series is compared against:

1. Corresponding previous-year live storage.
2. CWC-reported ten-year normal live storage.

The analysis uses the following indicators:

- **Net Storage Change:** Difference between the ending and starting live storage.
- **Storage Percentage:** Current live storage expressed as a percentage of live capacity.
- **Normal Storage Gap:** Difference between current storage and ten-year normal storage.
- **Below-Normal Date:** First observation when current storage falls below the ten-year normal.
- **Zero-Storage Date:** First observation when reported live storage reaches zero.

Python is used for data extraction, cleaning, numerical analysis and figure generation.

Libraries used:
- Pandas
- NumPy
- Matplotlib
- OpenPyXL

---

## 4. Results

The analysis covers 24 weekly observations from November 2024 to May 2025.

Key findings include:

- Live storage declined from 1,517 MCM on 14 November 2024 to zero on 1 May 2025.
- The first reported zero-live-storage observation occurred on 24 April 2025.
- Current storage first fell below the ten-year normal on 20 March 2025.
- On 1 May 2025, ten-year normal storage was approximately 143 MCM, equivalent to 9.4% of live capacity.

### Figure 1: Weekly Reservoir Storage Comparison

Compares current-season live storage with previous-year live storage and the ten-year normal.

### Figure 2: Reservoir Storage Percentage

Shows current-season and ten-year normal storage as percentages of the reported live capacity.

---

## 5. Discussion

The observed storage decline highlights the seasonal water-stress conditions experienced at Ujani Reservoir during the 2024–25 period.

The comparison with ten-year normal storage provides a useful benchmark for identifying periods of below-normal reservoir availability. The decline below normal storage from March onwards indicates increasing seasonal storage stress.

These findings are relevant to reservoir monitoring and water-resource planning, particularly when considering irrigation requirements, municipal supply and downstream environmental needs.

However, storage observations alone cannot establish the actual contribution of inflows, evaporation, upstream releases or withdrawals to the observed decline. They also cannot quantify sector-wise demand satisfaction.

Further work can improve the analysis by incorporating:

- Historical monthly inflow and reservoir storage data.
- Evaporation estimates.
- Actual reservoir releases and canal diversions.
- Municipal, irrigation and environmental-flow demand records.
- Upstream reservoir operations.
- Alternative release-priority rules and multi-objective optimisation.

The original monthly water-balance allocation model can be developed further once these additional datasets are available.

---

## 6. Repository Structure

```text
CE766/
│
├── README.md
│
├── Ujani_Reservoir_Weekly_Storage_Data-v3.xlsx
│
├── ujani_weekly_analysis.py
│
├── ujani_model_original.py
│
├── ujani_cleaned_weekly_data.csv
│
├── Figure_1_Weekly_Storage_Comparison.png
│
├── Figure_2_Storage_Percentage.png
│
├── key_results.txt
│
└── Ujani_Final_Project_Report.docx
```

---

## 7. Reproducibility

### Requirements

Install the required Python libraries:

```bash
pip install pandas numpy matplotlib openpyxl
```

### Run the Analysis

```bash
python ujani_weekly_analysis.py
```

The script processes the weekly reservoir observations, generates the cleaned dataset and produces the two analytical figures.

---

## 8. References

1. Central Water Commission (CWC). *Weekly Reservoir Storage Reports – Bhima (Ujjani)*. Observations consolidated for November 2024–May 2025.

2. Loucks, D. P. and van Beek, E. (2017). *Water Resource Systems Planning and Management: An Introduction to Methods, Models, and Applications*. Springer.

3. Central Water Commission and Maharashtra Engineering Research Institute (MERI), Nashik. *Sedimentation Assessment of Ujjani Reservoir through Remote Sensing*.

---

## Project Repository

**GitHub:** https://github.com/udit29042005/CE766
