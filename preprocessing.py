import pandas as pd
import os

def clean_and_map(file_path):
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()

    # Drop missing FNSKU/MSKU rows
    df.dropna(subset=['FNSKU', 'MSKU'], inplace=True)

    # Ensure Quantity is numeric and replace negative values with 0
    if 'Quantity' in df.columns:
        df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce').fillna(0)
        df['Quantity'] = df['Quantity'].clip(lower=0)  # Set negative quantities to 0

    # Save cleaned file
    output_path = os.path.join("processed", "cleaned_output.csv")
    df.to_csv(output_path, index=False)
    return df, output_path