import matplotlib.pyplot as plt
import seaborn as sns
from src.preprocessing.loader import load_cleaned_data

def create_visualizations(data_paths, output_paths):
    df = load_cleaned_data(data_paths)
    if df.empty:
        return

    plot_histogram(df, 'some_numeric_column', output_paths)
    plot_time_series(df, 'date_column', 'value_column', output_paths)
    plot_category_comparison(df, 'category_column', 'value_column', output_paths)
    print("Visualizations created and saved in the 'reports/figures/' directory.")

def plot_histogram(df, column, output_paths):
    plt.figure(figsize=(10, 6))
    df[column].hist()
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.savefig(output_paths['figures'] / f'{column}_distribution.png')
    plt.show()
    plt.close()

def plot_time_series(df, date_column, value_column, output_paths):
    plt.figure(figsize=(12, 6))
    df.groupby(date_column)[value_column].sum().plot()
    plt.title(f'{value_column} Over Time')
    plt.xlabel(date_column)
    plt.ylabel(value_column)
    plt.savefig(output_paths['figures'] / f'{value_column}_trend.png')
    plt.show()
    plt.close()

def plot_category_comparison(df, category_column, value_column, output_paths):
    plt.figure(figsize=(10, 6))
    sns.barplot(x=category_column, y=value_column, data=df)
    plt.title(f'{value_column} by {category_column}')
    plt.xlabel(category_column)
    plt.ylabel(value_column)
    plt.xticks(rotation=45)
    plt.savefig(output_paths['figures'] / f'{value_column}_by_{category_column}.png')
    plt.show()
    plt.close()
