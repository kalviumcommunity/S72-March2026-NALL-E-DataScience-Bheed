# Milestone 4.4 — Building the Project Plan and MVP

## Problem Statement
Tourism departments often lack predictive insights, leading to overcrowding and resource mismanagement during peak seasons. BheedRadar provides a data-driven solution to forecast visitor footfall and recommend department-level actions.

## Dataset Plan
*   **Source**: Synthetic tourism footfall data (generated for Rajasthan, Goa, and Himachal Pradesh).
*   **Schema**: Cities (5), Zones (4), Date (Monthly, 5 years), Visitor Count, Temperature, Is_Holiday.
*   **Size**: ~300 rows (60 months × 5 cities).

## ML Approach
1.  **Baseline**: Naive model (Predict $t+1 = t$).
2.  **Simple Model**: Linear Regression using months and holidays.
3.  **Advanced Model**: Random Forest Regressor for non-linear seasonality and feature importance.

## MVP Definition
A working 6-month forecast for 3 major tourist cities (Jaipur, Goa, Shimla) displayed on an interactive Streamlit dashboard with:
*   City-level filtering.
*   KPI cards for peak footfall and risk levels.
*   Forecast vs. Historical trend charts.

## Success Criteria
*   Model performance: Mean Absolute Error (MAE) < 15% of average visitor count.
*   Deployable Streamlit dashboard with all tabs functional.
*   Cleanly documented repository following DS best practices.

## Risk & Mitigation
| Risk | Impact | Mitigation |
| :--- | :--- | :--- |
| Insufficient Data | High | Generate realistic synthetic data with historical seasonality. |
| Model Overfitting | Med | Use cross-validation and keep features simple initially. |
| Dashboard Lag | Low | Optimize Pandas operations and use Streamlit caching. |
