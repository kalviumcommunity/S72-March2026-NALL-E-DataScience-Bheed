# BheedRadar — Dataset Summary

## Dataset Information
- **Name**: `sample_footfall.csv`
- **Location**: `data/raw/`
- **Rows**: 1000
- **Time Range**: 50 monthly periods (approx. 4 years).
- **Cities**: Jaipur, Goa, Shimla, Udaipur, Manali.

## Data Schema
| Column | Description | Data Type | Range/Possible Values |
| :--- | :--- | :--- | :--- |
| `city` | Name of the tourist city. | String | Jaipur, Goa, Shimla, Udaipur, Manali |
| `zone` | Sub-area within the city. | String | Zone A, Zone B, Zone C, Zone D |
| `date` | Date of the recording (Month-Level). | Date | YYYY-MM-DD |
| `visitor_count` | Number of recorded visitors for the period. | Integer | 500 – 2500+ |
| `temperature` | Average monthly temperature (°C). | Float | 5.0 – 40.0 |
| `is_holiday` | Whether the month contains major public holidays (flag). | Boolean/Int | 0 (No), 1 (Yes) |

## Data Conventions
- **Raw Data**: Never edit directly.
- **Processed Data**: All data cleaning must be scripted in `src/data_pipeline.py`.
- **Naming**: Use lowercase with underscores for all column names.
