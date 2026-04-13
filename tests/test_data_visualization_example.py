import pytest
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Unit test for data loading

def test_iris_data_loading():
    """Test loading of iris dataset"""
    try:
        iris = sns.load_dataset('iris')
        assert not iris.empty, "The iris dataset should not be empty"
    except Exception as e:
        pytest.fail(f"Iris dataset loading failed: {str(e)}")

# Unit test for scatter plot rendering

def test_scatter_plot():
    """Test rendering of scatter plot"""
    try:
        iris = sns.load_dataset('iris')
        sns.scatterplot(data=iris, x='sepal_length', y='sepal_width', hue='species')
        plt.title('Scatter Plot of Sepal Length vs Sepal Width')
        plt.close()
    except Exception as e:
        pytest.fail(f"Scatter plot rendering failed: {str(e)}")

# Unit test for histogram rendering

def test_histogram():
    """Test rendering of histogram"""
    try:
        iris = sns.load_dataset('iris')
        sns.histplot(data=iris, x='petal_length', bins=20, hue='species', kde=True)
        plt.title('Histogram of Petal Length')
        plt.close()
    except Exception as e:
        pytest.fail(f"Histogram rendering failed: {str(e)}")

# Unit test for box plot rendering

def test_box_plot():
    """Test rendering of box plot"""
    try:
        iris = sns.load_dataset('iris')
        sns.boxplot(data=iris, x='species', y='petal_width')
        plt.title('Box Plot of Petal Width by Species')
        plt.close()
    except Exception as e:
        pytest.fail(f"Box plot rendering failed: {str(e)}")

# Unit test for line plot rendering

def test_line_plot():
    """Test rendering of line plot"""
    try:
        iris = sns.load_dataset('iris')
        sns.lineplot(data=iris, x='sepal_length', y='sepal_width', hue='species')
        plt.title('Line Plot of Sepal Length vs Sepal Width')
        plt.close()
    except Exception as e:
        pytest.fail(f"Line plot rendering failed: {str(e)}")
