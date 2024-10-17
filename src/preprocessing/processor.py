import pandas as pd
import numpy as np
from .loader import load_raw_data, save_processed_data
from src.analysis.analyzer import initial_eda

def process_data(data_paths):
    df = load_raw_data(data_paths)
    if df.empty:
        print("No data to process.")
        return

    print("Performing Initial Exploratory Data Analysis...")
    initial_eda(df)
    print("\nProcessing data...")
    df = remove_duplicates(df)
    df = convert_date_columns(df)
    df = handle_missing_values(df)

    save_processed_data(df, data_paths)
    print("Data processing completed.")

def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    initial_rows = len(df)
    df = df.drop_duplicates()
    removed_rows = initial_rows - len(df)
    print(f"Removed {removed_rows} duplicate rows.")
    return df

def convert_date_columns(df: pd.DataFrame) -> pd.DataFrame:
    for col in df.select_dtypes(include=['object']):
        try:
            df[col] = pd.to_datetime(df[col])
            print(f"Converted '{col}' to datetime.")
        except ValueError:
            pass
    return df

def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    for col in df.columns:
        missing = df[col].isnull().sum()
        if missing > 0:
            pct_missing = missing / len(df) * 100
            if pct_missing < 5:
                if df[col].dtype in ['int64', 'float64']:
                    df[col].fillna(df[col].median(), inplace=True)
                    print(f"Filled missing values in '{col}' with median.")
                else:
                    df[col].fillna(df[col].mode()[0], inplace=True)
                    print(f"Filled missing values in '{col}' with mode.")
            else:
                print(f"Warning: '{col}' has {pct_missing:.2f}% missing values. Consider further investigation.")
    return df
