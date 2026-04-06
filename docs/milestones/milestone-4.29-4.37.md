# Milestone 4.29, 4.30 & 4.37 — CSV Loading, Data Inspection, and Summary Statistics

In this milestone, we practice the initial steps of the Data Science lifecycle: Data Acquisition and Data Preparation.

## Key Concepts

### 1. CSV Loading
We use `pd.read_csv()` to import external tourist footfall data. This allows us to work with real-world datasets that are larger than what we can manually type into a Python dictionary.

### 2. Data Inspection
*   `.head()`: View the first few rows (default 5).
*   `.info()`: Check column data types and missing values (Non-Null Counts).
*   `.shape`: Get numeric rows and columns count.
*   `.columns`: List the names of all headers.

### 3. Summary Statistics
*   `.describe()`: Generates a table of count, mean, std, min, 25%, 50%, 75%, and max for all numerical columns. This is crucial for understanding the central tendency and spread of visitor numbers.
*   `.value_counts()`: To see how many records we have for each city or zone.

## Why this matters for BheedRadar?
This step reveals the "health" of our data. We identify if any months are missing data, if visitor counts have unrealistic outliers (e.g., negative numbers), and get a quick bird's-eye view of which cities have the highest average tourist traffic.

## Reference
See `notebooks/07_data_inspection.ipynb` for the interactive demo.
