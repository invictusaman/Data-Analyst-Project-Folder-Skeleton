# Data Analysis Project Skeleton

## Overview

This project skeleton was created to standardize and streamline data analysis workflows in organizational settings. It provides a structured, modular approach to data analysis tasks, enhancing productivity, maintainability, and collaboration among data analysts.

## Importance of This Approach

1.  **Modularity**: Each component (pre-processing, analysis, visualization) is separate, making it easier to maintain and update individual parts without affecting others.
2.  **Reusability**: Functions and modules can be easily reused across different projects or shared with team members.
3.  **Consistency**: A standardized structure ensures all data analysis projects within the organization follow the same pattern, improving readability and understanding.
4.  **Collaboration**: Clear organization allows multiple analysts to work on different parts of the project simultaneously without conflicts.
5.  **Reproducibility**: Well-structured code, along with environment specifications, ensures that analyses can be easily reproduced by others.
6.  **Scalability**: As projects grow, the modular structure makes it easier to add new features or expand existing functionality.
7.  **Version Control**: The structure is designed to work well with version control systems, making it easier to track changes and collaborate.
8.  **Productivity**: By providing a ready-to-use structure, analysts can focus on actual data analysis rather than project setup and organization.

## Project Structure

- `data/`:
  - `raw/`: Original, immutable data
  - `cleaned/`: Processed, analysis-ready data
- `src/`:
  - `config/`: Configuration files (e.g., paths)
  - `preprocessing/`: Data loading and processing scripts
  - `analysis/`: Data analysis functions
  - `visualization/`: Data visualization scripts
- `notebooks/`: Jupyter notebooks for exploratory analysis
- `reports/`: Output directory for figures and final reports
- `.gitignore`: Ignore the files and folders when uploading to Github
- `main.py`: Entry point for running the entire pipeline
- `requirements.txt`: Project dependencies
- `README.md`: Project documentation

## How It Works

1.  The project uses modular programming to separate the process of:
    - Data loading and pre-processing
    - Analysis
    - Visualization
2.  `main.py` runs the entire data analysis pipeline
3.  Individual modules can be imported into Jupyter notebooks for interactive analysis

## Required Steps

1.  Clone the repository and remove `.gitkeep`.
2.  Place your raw data in `data/raw/`
3.  Make necessary changes in python files.
4.  Run the analysis: `python main.py`
5.  Utilize Quarto to generate final reports.

Note: If you are initially uncomfortable with running python files, code your program in `notebooks/original-notebook.ipynb` and convert each step into functions and append them in `processor.py` or `analyzer.py` or `visualizer.py` accordingly.

## Generating requirements.txt

You can use `pipreqs` to automatically generate the `requirements.txt` file.

```python
pip install pipreqs
```

Run `pipreqs --force` in your project folder directory, if not pass the path as `pipreqs --force path/to/project/directory`.

---

[Visit my personal portfolio](https://amanbhattarai.com.np) to check more data analyst stuffs.
