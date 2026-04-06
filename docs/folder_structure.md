# BheedRadar — Repository Folder Structure

This project follows a modular and reproducible data science repository structure.

## Directories
- `data/`: Version-controlled data storage.
    - `raw/`: Unaltered source data (e.g., historical visitor logs).
    - `processed/`: Cleaned and engineered datasets for modeling.
- `notebooks/`: Jupyter notebooks for exploratory analysis and model prototyping.
- `outputs/`: Generated analysis artifacts.
    - `eda_charts/`: Visualizations (PNG/PDF) saved during EDA.
- `src/`: Core Python source code.
    - `dashboard.py`: Streamlit interface.
    - `data_pipeline.py`: Cleaning and engineering scripts.
- `docs/`: Detailed project documentation and milestone logs.

## Files
- `README.md`: Project introduction and setup guide.
- `requirements.txt`: Python package dependencies with pinned versions.
- `project_overview.md`: High-level problem and solution summary.
- `.gitignore`: Ensures large data and temp files are not tracked by Git.
