import unittest
import pandas as pd

class TestAdditionalPandasTasks(unittest.TestCase):

    def setUp(self):
        self.data = {
            'Name': ['Alice', 'Bob', 'Charlie', 'David'],
            'Age': [24, 27, 22, 32],
            'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
        }
        self.df = pd.DataFrame(self.data)

    def test_dataframe_initialization(self):
        """Test if DataFrame initializes correctly from dictionary."""
        df_expected = pd.DataFrame({
            'Name': ['Alice', 'Bob', 'Charlie', 'David'],
            'Age': [24, 27, 22, 32],
            'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
        })
        pd.testing.assert_frame_equal(self.df, df_expected)

    def test_add_column(self):
        """Test adding a new column to DataFrame."""
        self.df['Salary'] = [70000, 80000, 75000, 85000]
        self.assertIn('Salary', self.df.columns)
        self.assertEqual(list(self.df['Salary']), [70000, 80000, 75000, 85000])

    def test_remove_column(self):
        """Test removing a column from DataFrame."""
        self.df.drop('City', axis=1, inplace=True)
        self.assertNotIn('City', self.df.columns)

    def test_sorting_by_name(self):
        """Test sorting DataFrame by Name column."""
        df_sorted = self.df.sort_values(by='Name')
        self.assertEqual(list(df_sorted['Name']), ['Alice', 'Bob', 'Charlie', 'David'])

    def test_empty_dataframe(self):
        """Test operations on an empty DataFrame."""
        empty_df = pd.DataFrame()
        self.assertEqual(empty_df.empty, True)
        self.assertEqual(empty_df.shape, (0, 0))

    def test_plot_creation(self):
        """Ensure plotting doesn't raise exceptions and plot object is created."""
        try:
            plot = self.df.plot(x='Name', y='Age', kind='bar')
            self.assertIsNotNone(plot)
        except Exception as e:
            self.fail(f"Plotting failed: {e}")

if __name__ == '__main__':
    unittest.main()
