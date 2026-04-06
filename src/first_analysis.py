import pandas as pd
import os

def main():
    # File path
    file_path = 'data/raw/sample_footfall.csv'
    
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return

    # Load data
    print(f"Loading {file_path}...")
    df = pd.read_csv(file_path)
    
    # 1. Shape of the data
    print("\n--- Dataset Shape ---")
    print(df.shape)
    
    # 2. Column names
    print("\n--- Column Names ---")
    print(df.columns.tolist())
    
    # 3. First 5 rows
    print("\n--- First 5 Rows ---")
    print(df.head())
    
    # 4. Basic Statistics
    print("\n--- Basic Statistics ---")
    print(df.describe())

if __name__ == "__main__":
    main()
