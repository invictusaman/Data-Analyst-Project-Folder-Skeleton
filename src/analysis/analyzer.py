import pandas as pd
import numpy as np
from src.preprocessing.loader import load_cleaned_data

def perform_eda(df: pd.DataFrame, is_initial: bool = True) -> None:
    """
    Perform Exploratory Data Analysis on the given DataFrame.

    Args:
    df (pd.DataFrame): The DataFrame to analyze
    is_initial (bool): Whether this is the initial EDA or post-cleaning EDA
    """
    print(f"{'Initial' if is_initial else 'Post-Cleaning'} Exploratory Data Analysis\n")

    print_basic_info(df)
    print_missing_values(df)

    if is_initial:
        print_duplicates(df)

    print_summary_stats(df)
    print_categorical_stats(df)
    print_numerical_stats(df)

    if not is_initial:
        print_correlation(df)

def print_basic_info(df: pd.DataFrame) -> None:
    print("Basic Information:")
    print(f"Shape: {df.shape}")
    print(f"Memory Usage: {df.memory_usage(deep=True).sum() / 1e6:.2f} MB")
    print("\nColumn Types:")
    print(df.dtypes)
    print()

def print_missing_values(df: pd.DataFrame) -> None:
    print("Missing Values:")
    missing = df.isnull().sum()
    print(missing[missing > 0])
    print()

def print_duplicates(df: pd.DataFrame) -> None:
    print(f"Duplicate Rows: {df.duplicated().sum()}")
    print()

def print_summary_stats(df: pd.DataFrame) -> None:
    print("Summary Statistics:")
    print(df.describe(include='all'))
    print()

def print_categorical_stats(df: pd.DataFrame) -> None:
    cat_columns = df.select_dtypes(include=['object', 'category']).columns
    print("Categorical Columns Statistics:")
    for col in cat_columns:
        print(f"{col}:")
        print(f"  Unique Values: {df[col].nunique()}")
        print("  Top 5 Values:")
        print(df[col].value_counts().nlargest(5))
        print()

def print_numerical_stats(df: pd.DataFrame) -> None:
    num_columns = df.select_dtypes(include=[np.number]).columns
    print("Numerical Columns Statistics:")
    for col in num_columns:
        print(f"{col}:")
        print(f"  Skewness: {df[col].skew():.2f}")
        print(f"  Kurtosis: {df[col].kurtosis():.2f}")
        print_outliers(df[col])
        print()

def print_outliers(series: pd.Series) -> None:
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = ((series < lower_bound) | (series > upper_bound)).sum()
    print(f"  Outliers: {outliers} (Lower bound: {lower_bound:.2f}, Upper bound: {upper_bound:.2f})")

def print_correlation(df: pd.DataFrame) -> None:
    num_columns = df.select_dtypes(include=[np.number]).columns
    corr = df[num_columns].corr()
    print("Strong Correlations (|correlation| > 0.7):")
    for i in range(len(num_columns)):
        for j in range(i+1, len(num_columns)):
            if abs(corr.iloc[i, j]) > 0.7:
                print(f"  {num_columns[i]} - {num_columns[j]}: {corr.iloc[i, j]:.2f}")
    print()

def analyze_data(data_paths: str) -> None:
    df = load_cleaned_data(data_paths)
    if df.empty:
        print("No data to analyze.")
        return
    perform_eda(df, is_initial=False)
