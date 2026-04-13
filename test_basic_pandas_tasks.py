# test_basic_pandas_tasks.py

import unittest
import pandas as pd

class TestBasicPandasTasks(unittest.TestCase):

    def setUp(self):
        self.data = {
            'Name': ['Alice', 'Bob', 'Charlie', 'David'],
            'Age': [24, 27, 22, 32],
            'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
        }
        self.df = pd.DataFrame(self.data)

    def test_dataframe_creation(self):
        # Check DataFrame shape
        self.assertEqual(self.df.shape, (4, 3))
        
        # Check DataFrame content
        self.assertEqual(list(self.df.columns), ['Name', 'Age', 'City'])
        self.assertTrue('Alice' in self.df['Name'].values)

    def test_column_selection(self):
        names = self.df['Name']
        self.assertEqual(list(names), ['Alice', 'Bob', 'Charlie', 'David'])
        
    def test_filtering_rows(self):
        older_than_25 = self.df[self.df['Age'] > 25]
        self.assertTrue('Bob' in older_than_25['Name'].values)
        self.assertEqual(len(older_than_25), 2)

    def test_descriptive_statistics(self):
        stats = self.df.describe()
        self.assertEqual(stats.loc['max', 'Age'], 32)
        self.assertEqual(stats.loc['min', 'Age'], 22)

    def test_add_remove_columns(self):
        # Add new column
        self.df['Profession'] = ['Engineer', 'Doctor', 'Artist', 'Lawyer']
        self.assertEqual(list(self.df['Profession']), ['Engineer', 'Doctor', 'Artist', 'Lawyer'])
        
        # Remove 'City' column
        self.df = self.df.drop(columns='City')
        self.assertNotIn('City', self.df.columns)

    def test_sorting(self):
        df_sorted = self.df.sort_values(by='Age')
        self.assertEqual(list(df_sorted['Name']), ['Charlie', 'Alice', 'Bob', 'David'])

    def test_plot(self):
        try:
            df_sorted = self.df.sort_values(by='Age')
            plot = df_sorted.plot(x='Name', y='Age', kind='bar')
            self.assertIsNotNone(plot)
        except Exception as e:
            self.fail(f"Plotting failed: {e}")

if __name__ == '__main__':
    unittest.main()
