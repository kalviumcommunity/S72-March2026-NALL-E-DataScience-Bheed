# Milestone 4.3 — Reading a Sample DS Repository

## Reference Repository: `cookiecutter-data-science`
We studied the structure of the [drivendata/cookiecutter-data-science](https://github.com/drivendata/cookiecutter-data-science) template, which is a gold standard for DS projects.

### Standard Folder Layout
*   `data/`: Version-controlled data (raw, processed, external).
*   `notebooks/`: Jupyter notebooks for EDA and modeling.
*   `src/`: Modular Python code (data ingestion, cleaning, features).
*   `models/`: Trained model binaries and logs.
*   `reports/`: Final visualizations and analysis.
*   `requirements.txt`: Project dependencies.

### Comparison Table: BheedRadar vs. Template
| Feature | cookiecutter-data-science | BheedRadar Replicated/Adapted |
| :--- | :--- | :--- |
| **Data Storage** | `data/raw`, `data/processed`, `data/interim` | Using `data/raw` and `data/processed`. |
| **Code Structure** | Large `src/` modules for everything. | Smaller `src/` scripts for Data Pipeline and Dashboard. |
| **Documentation** | Focused on `docs/` and `README`. | Adding detailed `milestone-X.md` for daily tracking. |
| **Analysis** | Heavy use of Jupyter notebooks. | Mix of notebooks for EDA and Streamlit for dashboarding. |

## Initial README.md Skeleton
```markdown
# BheedRadar - Tourist Footfall Forecasting

BheedRadar helps city departments manage transport, safety, and cleanliness by predicting visitor footfall.

## Project Structure
- `data/`: Raw and processed tourist footfall data.
- `notebooks/`: EDA and model exploration.
- `src/`: Core Python modules (data cleaning, dashboard).
- `outputs/`: Charts and forecasting reports.

## Getting Started
(Details to be added in Milestone 4.5)
```
