# Milestone 4.13 — Creating and Running a First Python Script

## Objective
The goal for this milestone was to create a Python script that loads the BheedRadar tourism dataset and prints basic inspection statistics.

## Implementation: `src/first_analysis.py`
The script performs the following operations:
- Loads `data/raw/sample_footfall.csv` using Pandas.
- Prints the **shape** of the dataset (Rows, Columns).
- Lists all **column names**.
- Displays the **first 5 rows** for visual inspection.
- Computes **basic statistics** (mean, std, min, max, percentiles) for numeric columns.

## Execution Output
```text
Loading data/raw/sample_footfall.csv...

--- Dataset Shape ---
(1000, 6)

--- Column Names ---
['city', 'zone', 'date', 'visitor_count', 'temperature', 'is_holiday']

--- First 5 Rows ---
     city    zone        date  visitor_count  temperature  is_holiday
0  Jaipur  Zone A  2021-01-01           1659         5.38           1
1  Jaipur  Zone A  2021-01-31           1133         8.35           1
2  Jaipur  Zone A  2021-03-02           1180        15.15           0
3  Jaipur  Zone A  2021-04-01           1452        16.74           0
4  Jaipur  Zone A  2021-05-01           1026        15.60           0

--- Basic Statistics ---
       visitor_count  temperature  is_holiday
count     1000.00000  1000.000000  1000.00000
mean      1204.42200    16.616960     0.36000
std        416.90623     7.344102     0.48024
min        448.00000     5.040000     0.00000
25%        881.75000    10.842500     0.00000
50%       1164.50000    16.055000     0.00000
75%       1478.25000    20.150000     1.00000
max       2336.00000    35.000000     1.00000
```

## Observations
- The dataset has 1000 records.
- Average footfall is around 1204 visitors per city-zone-month.
- High footfall reaches up to 2336 visitors, indicating clear peak periods.

## Next Step
**Milestone 4.14**: Investigating specific Python data types within this dataset.
