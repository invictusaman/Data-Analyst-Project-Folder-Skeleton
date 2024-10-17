import pandas as pd
from src.preprocessing.loader import load_cleaned_data

def analyze_data(data_paths) -> None:
    df = load_cleaned_data(data_paths)
    if df.empty:
        print("No data to analyze.")
        return

    print("Performing data analysis...")
    summary_stats = calculate_summary_statistics(df)
    print("Summary Statistics:\n")
    print(summary_stats)

    print("Information Statistics:\n")
    calculate_info_statistics(df)

    corr_matrix = calculate_corr_matrix(df)
    print("\nCorrelation Matrix:\n")
    print(corr_matrix)

    category_stats = calculate_categorical_col_statistics(df)
    print("Summary of categorical columns\n")
    print(category_stats)

def initial_eda(df: pd.DataFrame) -> None:
    """Perform initial exploratory data analysis on the DataFrame."""
    print("Printing first five rows:")
    print(df.head(5))
    print(f"\nDataset shape: {df.shape}")

    print("\nInformation Statistics:")
    calculate_info_statistics(df)

    print("\nMissing values:")
    print(df.isnull().sum())

    print("\nDuplicate rows:", df.duplicated().sum())

    summary_stats = calculate_summary_statistics(df)
    print("\nSummary Statistics:")
    print(summary_stats)

    print("\nUnique values in categorical columns:")
    for col in df.select_dtypes(include=['object']):
        print(f"{col}: {df[col].nunique()}")

    category_stats = calculate_categorical_col_statistics(df)
    print("\nCategorical column statistics:")
    print(category_stats)

def calculate_summary_statistics(df):
    return df.describe()

def calculate_info_statistics(df):
    df.info()

def calculate_corr_matrix(df):
    numeric_df = df.select_dtypes(include=['number'])
    return numeric_df.corr()

def calculate_categorical_col_statistics(df):
    categorical_columns = df.select_dtypes(include=['object']).columns
    result = ''
    for col in categorical_columns:
        result += f"Value Counts of {col}:\n{df[col].value_counts().to_string()}\n\n"
    return result
