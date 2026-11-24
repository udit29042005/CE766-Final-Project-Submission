# Ujani Reservoir CE766 final submission files

## Important scope note
The supplied workbook contains 24 CWC weekly bulletins from 14-Nov-2024 to 01-May-2025. It does not contain the monthly inflow, evaporation, sectoral demand or release inputs required by `ujani_model.py`. Therefore, the original 2000–2024 monthly mass-balance model and demand-satisfaction figures cannot be reproduced from this dataset. The final report explicitly revises the analysis to a descriptive weekly-storage assessment and does not invent model outputs.

## Files
- `Ujani_Final_Project_Report.docx`: report with the two allowed result figures.
- `Figure_1_Weekly_Storage_Comparison.png`: current, previous-year and 10-year-normal live storage.
- `Figure_2_Storage_Percentage.png`: current and normal storage as percentage of live capacity.
- `ujani_cleaned_weekly_data.csv`: cleaned 24-bulletin dataset, including storage converted from BCM to MCM.
- `ujani_weekly_analysis.py`: reproducible script to recreate the cleaned CSV and figures.
- `ujani_model.py`: original proposed monthly model, included for traceability only; it cannot run on the supplied weekly workbook as-is.
- `Ujani_Reservoir_Weekly_Storage_Data-v3.xlsx`: original supplied workbook.

## Run
Install dependencies: `pip install pandas openpyxl matplotlib`
Then run: `python ujani_weekly_analysis.py`

## Key observed results
- 14-Nov-2024: 1,517 MCM (100% of live capacity).
- 24-Apr-2025: reported live storage first reaches 0 MCM.
- 01-May-2025: remains at 0 MCM; 10-year normal is 143 MCM (9.4%).
- Current storage first falls below the 10-year normal on 20-Mar-2025.
- The 10-Apr-2025 bulletin is absent; there is a two-week gap from 03-Apr to 17-Apr.
