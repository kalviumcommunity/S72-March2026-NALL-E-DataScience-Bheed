# Milestone 4.22 — Creating NumPy Arrays from Python Lists

## Objective
To transition from standard Python data structures to NumPy arrays, enabling high-performance numerical operations for tourism footfall forecasting.

## Key Learning Outcomes
1.  **NumPy Arrays (`ndarray`)**: Unlike Python lists, NumPy arrays are homogeneous (all elements must be of the same type) and stored contiguously in memory, making them significantly faster for mathematical operations.
2.  **Performance Visualization**: A simple benchmarking example in `notebooks/05_numpy_basics.ipynb` demonstrates that NumPy aggregations (like `.sum()`) are exponentially faster than standard Python list operations on large datasets.
3.  **Vectorization**: The fundamental concept behind NumPy, allowing for complex data transformations without manual for-loops.

## Implementation: `notebooks/05_numpy_basics.ipynb`
The notebook includes:
- Importing NumPy for the first time.
- Hand-crafting visitor count lists for Jaipur, Goa, and Shimla.
- Converting these lists into NumPy arrays.
- Performance comparisons on a 1-million-record list vs. array.

## Next Step
**Milestone 4.23**: Understanding Array Shape, Dimensions, and slicing for multi-city analysis.
