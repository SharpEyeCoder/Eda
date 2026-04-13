import unittest
from bs4 import BeautifulSoup

class TestAppleHTML(unittest.TestCase):
    def setUp(self):
        with open('../../examples/99abc337-e63d-496a-88c0-759a49c95a5d/apple.html', 'r', encoding='utf-8') as file:
            self.soup = BeautifulSoup(file, 'html.parser')

    def test_title_exists_and_correct(self):
        title = self.soup.find('title')
        self.assertIsNotNone(title, 'Title tag should be present')
        self.assertEqual(title.string, 'About Apple', 'Title should be "About Apple"')

    def test_h1_exists_and_correct(self):
        h1 = self.soup.find('h1')
        self.assertIsNotNone(h1, 'H1 tag should be present')
        self.assertEqual(h1.string, 'Apple', 'H1 should be "Apple"')

    def test_health_benefits_section(self):
        section = self.soup.find('h2', text='Health Benefits')
        self.assertIsNotNone(section, 'There should be an H2 tag for Health Benefits')
        paragraph = section.find_next_sibling('p')
        self.assertIsNotNone(paragraph, 'Health Benefits section should have a paragraph')
        self.assertIn('Apples are incredibly good for you', paragraph.text)

    def test_varieties_section(self):
        section = self.soup.find('h2', text='Varieties')
        self.assertIsNotNone(section, 'There should be an H2 tag for Varieties')
        paragraph = section.find_next_sibling('p')
        self.assertIsNotNone(paragraph, 'Varieties section should have a paragraph')
        self.assertIn('Fuji', paragraph.text)
        self.assertIn('Granny Smith', paragraph.text)
        self.assertIn('Gala', paragraph.text)

if __name__ == '__main__':
    unittest.main()