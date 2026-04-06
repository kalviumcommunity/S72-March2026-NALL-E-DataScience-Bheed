# Milestone 4.7 — Launching Jupyter & Understanding the Home Interface

## Launching Jupyter
1.  **Terminal Method**: Open terminal, activate the environment, and run:
    ```bash
    conda activate bheedradar
    jupyter lab
    ```
2.  **Home Browser**: The web browser opens at `http://localhost:8888`.

## Navigating the Interface
*   **File Browser**: Located on the left sidebar. Use it to navigate into the `notebooks/` folder.
*   **Creating Notebooks**: Click the `+` button in the launcher or `File > New > Notebook`.
*   **Renaming**: Right-click the notebook in the file browser and select `Rename`.

## Project-Specific Tips (BheedRadar)
*   **Storage**: Always save your experimental analysis in `notebooks/`.
*   **Deliverables**: Final cleaned scripts should go to `src/`.
*   **Outputs**: Charts generated in notebooks should be saved to `outputs/eda_charts/`.

## Kernel Management
*   **Restarting**: Use `Kernel > Restart Kernel...` if variables get messy.
*   **Shutting Down**: Go to the `Running Terminals and Kernels` tab (circle icon on the left) and click `Shut Down` for inactive notebooks to save memory.
