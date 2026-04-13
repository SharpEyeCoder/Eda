import os
from bs4 import BeautifulSoup
import unittest

class TestAppleHTML(unittest.TestCase):

    def setUp(self):
        # Setup path for apple.html
        self.file_path = os.path.join(os.path.dirname(__file__), 'apple.html')
        
        # Ensure the file exists
        self.assertTrue(os.path.exists(self.file_path), 'apple.html file does not exist.')
        
        # Read the file content
        with open(self.file_path, 'r', encoding='utf-8') as file:
            self.soup = BeautifulSoup(file, 'html.parser')

    def test_title(self):
        # Test for page title
        title_tag = self.soup.find('title')
        self.assertIsNotNone(title_tag, '<title> tag is missing.')
        self.assertEqual(title_tag.string, 'About Apple', "Page title should be 'About Apple'.")

    def test_main_headings(self):
        # Test for main heading
        h1_tag = self.soup.find('h1')
        self.assertIsNotNone(h1_tag, '<h1> tag is missing.')
        self.assertEqual(h1_tag.string, 'Apple', "Main heading should be 'Apple'.")

    def test_subheadings(self):
        # Test for Health Benefits subheading
        h2_tags = self.soup.find_all('h2')

        health_benefits = any(tag.string == 'Health Benefits' for tag in h2_tags)
        varieties = any(tag.string == 'Varieties' for tag in h2_tags)

        self.assertTrue(health_benefits, "<h2>Health Benefits</h2> tag is missing.")
        self.assertTrue(varieties, "<h2>Varieties</h2> tag is missing.")

    def test_content_paragraphs(self):
        # Test for content paragraphs
        paragraphs = self.soup.find_all('p')
        self.assertGreaterEqual(len(paragraphs), 2, "There should be at least two paragraphs.")

    def test_html_well_formed(self):
        # Test HTML structure
        self.assertTrue(self.soup.prettify())  # This will raise an error if the HTML is not well-formed

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()