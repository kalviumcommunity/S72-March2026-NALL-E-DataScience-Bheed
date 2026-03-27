# BheedRadar — Project Overview

## Problem Statement
Tourism departments operate blindly during peak seasons due to a lack of predictive insights. Crowding leads to mismanagement of transport, sanitation, and safety.

## Proposed Solution
BheedRadar is a forecasting system that uses historical visitor data, climate variables, and holiday schedules to predict tourist footfall and provide actionable resource recommendations.

## Key Features
- **Data Pipeline**: Clean and engineer features for 5 major tourist cities.
- **Interactive EDA**: Visual insights into seasonal trends and outliers.
- **ML Forecasting**: Predictive modeling (Random Forest) for 6-month projections.
- **Live Dashboard**: A Streamlit interface for department officials.

## Milestones Summary
1.  **Planning**: Tech orientation and DS lifecycle definition.
2.  **Environment**: Anaconda setup and Jupyter literacy.
3.  **Engine**: Data pipeline, NumPy/Pandas foundations.
4.  **EDA**: Summaries, distributions, and correlation maps.
5.  **Dashboard**: Incremental build-up and final polish.

## Quick Start
```bash
conda activate bheedradar
streamlit run src/dashboard.py
```
