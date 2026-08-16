# Milestone 4.5 — Installing Python and Anaconda

## Installation Steps
1.  **Download Anaconda**: Visited [anaconda.com](https://www.anaconda.com/download) and downloaded the installer for macOS (Apple Silicon/Intel).
2.  **Run Installer**: Followed the graphical installation wizard.
3.  **Verify Installation**: Opened Terminal and ran `conda --version`.
4.  **Create Environment**:
    ```bash
    conda create -n bheedradar python=3.10 -y
    ```
5.  **Activate Environment**:
    ```bash
    conda activate bheedradar
    ```

## Python Version Verification
*   **Target**: Python 3.10.x
*   **Actual**: Python 3.10.12 (as verified in terminal).

## Initial Dependencies
We have drafted the `requirements.txt` file with the following core libraries:
*   `pandas` (Data manipulation)
*   `numpy` (Vectorized operations)
*   `matplotlib` & `seaborn` (Visualization)
*   `scikit-learn` (Machine Learning)
*   `streamlit` (Dashboarding)

## Setup Guide for Team
A combined setup guide has been created to ensure both Piyush and Uday have identical environments.

### Step-by-Step for New Joiners
1.  Install Anaconda.
2.  Clone the repository.
3.  Run `conda env create -f environment.yml` (or manual create).
4.  Run `pip install -r requirements.txt`.
