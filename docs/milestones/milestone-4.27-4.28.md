# Milestone 4.27 & 4.28 — Pandas Series, DataFrames, Indexing, and Groupby Basics

In this milestone, we explore the core building blocks of Pandas, the primary library for data manipulation in Python.

## Key Concepts

### 1. Pandas Series
A one-dimensional array-like object that can hold any data type. It includes an index (label) for each element.

### 2. Pandas DataFrames
A two-dimensional, size-mutable, potentially heterogeneous tabular data structure with labeled axes (rows and columns). It is the central object in Pandas.

### 3. Indexing and Slicing (loc and iloc)
*   `.loc[]`: Label-based indexing.
*   `.iloc[]`: Integer-based indexing (positional).

### 4. Groupby Basics
The `groupby()` operation involves some combination of splitting the object, applying a function, and combining the results. This is essential for aggregating data by city, zone, or month.

## Why use Pandas for BheedRadar?
*   **Efficiency**: Handles large CSV files much better than native Python lists.
*   **Aggregations**: Easy to calculate average footfall per month for each city.
*   **Time Series**: Built-in support for dates and times.

## Reference
See `notebooks/06_pandas_basics.ipynb` for the interactive demo.
