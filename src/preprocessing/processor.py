import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from .loader import load_raw_data, save_cleaned_data
from src.analysis.analyzer import perform_eda

def process_and_clean_data(data_paths):
    df = load_raw_data(data_paths)
    if df.empty:
        print("No data to process.")
        return

    print("Performing Initial Exploratory Data Analysis...\n")
    perform_eda(df, is_initial=True)

    print("\nProcessing and cleaning data...\n")
    df = remove_duplicates(df)
    #df = convert_date_columns(df)
    df = handle_missing_values(df)
    #df = handle_outliers(df, exclude_cols=['col_name1', 'col_name2'])
    #df = normalize_numeric_columns(df, exclude_cols=['col_name1','col_name2'])
    #df = encode_categorical_columns(df, exclude_cols=['col_name1', 'col_name2'])

    save_cleaned_data(df, data_paths)
    print("Data processing and cleaning completed.")

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

def handle_outliers(df: pd.DataFrame, exclude_cols: list = None) -> pd.DataFrame:
    if exclude_cols is None:
        exclude_cols = []
    # Select numeric columns, excluding specified columns
    numeric_cols = df.select_dtypes(include=['number']).columns.difference(exclude_cols) 
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

def normalize_numeric_columns(df: pd.DataFrame, exclude_cols: list = None) -> pd.DataFrame:
    if exclude_cols is None:
        exclude_cols = []
    # Select numeric columns, excluding specified columns
    numeric_cols = df.select_dtypes(include=['number']).columns.difference(exclude_cols) 
    scaler = StandardScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    print(f"Normalized {len(numeric_cols)} numeric columns, excluding: {exclude_cols}.")
    return df

def encode_categorical_columns(df: pd.DataFrame, exclude_cols: list = None) -> pd.DataFrame:
    if exclude_cols is None:
        exclude_cols = []
    # Select categorical columns, excluding specified columns
    categorical_cols = df.select_dtypes(include=['object']).columns.difference(exclude_cols)
    for col in categorical_cols:
        if df[col].nunique() < 10:  # Adjust this threshold if needed
            df = pd.get_dummies(df, columns=[col], prefix=col)
            print(f"One-hot encoded '{col}'.")
        else:
            df[col] = df[col].astype('category').cat.codes
            print(f"Label encoded '{col}'.")
    return df
