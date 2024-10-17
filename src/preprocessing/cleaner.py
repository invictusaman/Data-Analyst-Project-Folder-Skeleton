import pandas as pd
from .loader import load_processed_data, save_cleaned_data

def clean_data(data_paths):
    df = load_processed_data(data_paths)
    if df.empty:
        return

    df = handle_missing_values(df)
    save_cleaned_data(df, data_paths)
    print("Data cleaning completed.")

def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    numeric_cols = df.select_dtypes(include=['number']).columns
    categorical_cols = df.select_dtypes(include=['object']).columns

    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
    df[categorical_cols] = df[categorical_cols].fillna(df[categorical_cols].mode().iloc[0])

    return df
