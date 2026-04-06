# Milestone 4.23 — Understanding Array Shape, Dimensions, and Index Positions

## Objective
To master the ability to navigate and manipulate multi-dimensional NumPy arrays, which is essential for handling complex tourism datasets involving multiple cities and time periods.

## Key Learning Outcomes
1.  **Array Attributes**:
    *   `.shape`: Returns a tuple representing the size of each dimension (e.g., `(3, 6)` for a matrix of 3 cities and 6 months).
    *   `.ndim`: The number of axes or dimensions (e.g., 1 for a vector, 2 for a matrix).
    *   `.size`: Total number of elements in the array.
2.  **Indexing and Slicing**:
    *   Accessing specific values (e.g., `arr[2]` for the 3rd element).
    *   Slicing ranges (e.g., `arr[0:3]` for the first quarter).
    *   Negative indexing (e.g., `arr[-2:]` for the last two entries).
3.  **2D Arrays (Matrices)**: Combining multiple 1D arrays into a single structure for cross-city analysis.

## Implementation: `notebooks/05_numpy_basics.ipynb`
The notebook has been updated to include:
- Printing attributes for City arrays.
- Examples of standard and range-based indexing.
- Creation of a `tourism_matrix` representing Jaipur, Goa, and Shimla data in a 2x2 grid.

## Next Step
**Milestone 4.27**: Transitioning from NumPy to Pandas Series for labeled data analysis.
