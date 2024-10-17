import os
from pathlib import Path

def get_project_root():
    return Path(__file__).parent.parent.parent

def get_data_paths(dataset_name):
    root = get_project_root()
    return {
        'raw': root / 'data' / 'raw' / f'raw_{dataset_name}',
        'processed': root / 'data' / 'processed' / f'processed_{dataset_name}',
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
