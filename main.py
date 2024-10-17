from src.config.paths import get_data_paths, get_output_paths, ensure_directories_exist
from src.preprocessing.processor import process_data
from src.preprocessing.cleaner import clean_data
from src.analysis.analyzer import analyze_data
from src.visualization.visualizer import create_visualizations

def main():
    print("Starting data analysis...")

    # Initialize paths
    data_paths = get_data_paths("sample.csv")  # Replace with your dataset name
    output_paths = get_output_paths()

    # Ensure all necessary directories exist
    ensure_directories_exist({**data_paths, **output_paths})

    print("\nStep 1: Processing data")
    process_data(data_paths)

    print("\nStep 2: Cleaning data")
    clean_data(data_paths)

    print("\nStep 3: Analyzing data")
    analyze_data(data_paths)

    print("\nStep 4: Creating visualizations")
    create_visualizations(data_paths, output_paths)

    print("\nAnalysis completed successfully.")

if __name__ == "__main__":
    main()
