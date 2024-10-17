import pandas as pd
from pathlib import Path

def load_data(file_path: Path) -> pd.DataFrame:
    """Load data from a file, supporting CSV, Excel, and JSON formats."""
    try:
        suffix = file_path.suffix.lower()
        if suffix == '.csv':
            return pd.read_csv(file_path)
        elif suffix in ['.xls', '.xlsx']:
            return pd.read_excel(file_path)
        elif suffix == '.json':
            return pd.read_json(file_path)
        else:
            raise ValueError(f"Unsupported file format: {suffix}")
    except Exception as e:
        print(f"Error loading data from {file_path}: {str(e)}")
        return pd.DataFrame()

def save_data(df: pd.DataFrame, file_path: Path) -> None:
    """Save data to a file, supporting CSV, Excel, and JSON formats."""
    try:
        file_path.parent.mkdir(parents=True, exist_ok=True)
        suffix = file_path.suffix.lower()
        if suffix == '.csv':
            df.to_csv(file_path, index=False)
        elif suffix in ['.xls', '.xlsx']:
            df.to_excel(file_path, index=False)
        elif suffix == '.json':
            df.to_json(file_path, orient='records')
        else:
            raise ValueError(f"Unsupported file format: {suffix}")
        print(f"Data successfully saved to {file_path}")
    except Exception as e:
        print(f"Error saving data to {file_path}: {str(e)}")

def load_raw_data(data_paths):
    return load_data(data_paths['raw'])

def load_cleaned_data(data_paths):
    return load_data(data_paths['cleaned'])

def save_cleaned_data(df, data_paths):
    save_data(df, data_paths['cleaned'])
