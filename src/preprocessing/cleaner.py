import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from .loader import load_processed_data, save_cleaned_data

def clean_data(data_paths):
    df = load_processed_data(data_paths)
    if df.empty:
        print("No data to clean.")
        return

    print("Cleaning data...")
    df = handle_outliers(df)
    df = normalize_numeric_columns(df)
    df = encode_categorical_columns(df)

    save_cleaned_data(df, data_paths)
    print("Data cleaning completed.")


def handle_outliers(df: pd.DataFrame) -> pd.DataFrame:
    numeric_cols = df.select_dtypes(include=['number']).columns
    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outliers = ((df[col] < lower_bound) | (df[col] > upper_bound)).sum()
        if outliers > 0:
            print(f"Detected {outliers} outliers in '{col}'.")
            df[col] = df[col].clip(lower_bound, upper_bound)
            print(f"Clipped outliers in '{col}' to [{lower_bound:.2f}, {upper_bound:.2f}].")
    return df

def normalize_numeric_columns(df: pd.DataFrame) -> pd.DataFrame:
    numeric_cols = df.select_dtypes(include=['number']).columns
    scaler = StandardScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    print(f"Normalized {len(numeric_cols)} numeric columns.")
    return df

def encode_categorical_columns(df: pd.DataFrame) -> pd.DataFrame:
    categorical_cols = df.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        if df[col].nunique() < 10:  # You can adjust this threshold
            df = pd.get_dummies(df, columns=[col], prefix=col)
            print(f"One-hot encoded '{col}'.")
        else:
            df[col] = df[col].astype('category').cat.codes
            print(f"Label encoded '{col}'.")
    return df
