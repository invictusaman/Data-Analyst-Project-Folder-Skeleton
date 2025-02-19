from src.config.paths import get_data_paths, get_output_paths, ensure_directories_exist
from src.preprocessing.processor import process_and_clean_data
from src.analysis.analyzer import analyze_data
from src.visualization.visualizer import create_visualizations

def main():
    print("\nStarting data analysis...")

    # Initialize paths
    data_paths = get_data_paths("sample_data.csv")  # Replace with your dataset name
    output_paths = get_output_paths()

    # Ensure all necessary directories exist
    ensure_directories_exist({**data_paths, **output_paths})

    print("\nStep 1: Loading, preprocessing, and cleaning data...\n")
    process_and_clean_data(data_paths)

    print("\nStep 2: Performing data analysis...\n")
    analyze_data(data_paths)

    print("\nStep 3: Creating visualizations...\n")
    create_visualizations(data_paths, output_paths)

    print("\nData Analysis pipeline completed successfully.\n")

if __name__ == "__main__":
    main()
