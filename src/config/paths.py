import os
from pathlib import Path
import sys

def get_project_root():
    # Check if running in a Jupyter notebook since __file__ is not supported
    if 'ipykernel' in sys.modules:
        # Navigate one level up from the notebooks folder
        return Path.cwd().parent
    else:
        # Use the script's location for standard Python scripts
        return Path(__file__).parent.parent.parent

def get_data_paths(dataset_name):
    root = get_project_root()
    return {
        'raw': root / 'data' / 'raw' / dataset_name,
        'cleaned': root / 'data' / 'cleaned' / f'cleaned_{dataset_name}'
    }

def get_output_paths():
    root = get_project_root()
    return {
        'figures': root / 'reports' / 'figures'
    }

def ensure_directories_exist(paths):
    for path in paths.values():
        path.parent.mkdir(parents=True, exist_ok=True)
