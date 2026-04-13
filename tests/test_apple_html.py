import unittest
from bs4 import BeautifulSoup

class TestAppleHtml(unittest.TestCase):

    def setUp(self):
        with open('../apple.html', 'r', encoding='utf-8') as file:
            self.soup = BeautifulSoup(file, 'html.parser')

    def test_title(self):
        title = self.soup.title.string
        self.assertEqual(title, "About Apple", "Title should be 'About Apple'")

    def test_headings(self):
        h1 = self.soup.find('h1')
        self.assertEqual(h1.string, "Apple", "H1 should be 'Apple'")

        h2_tags = self.soup.find_all('h2')
        self.assertEqual(h2_tags[0].string, "Health Benefits", "First H2 should be 'Health Benefits'")
        self.assertEqual(h2_tags[1].string, "Varieties", "Second H2 should be 'Varieties'")

    def test_paragraphs(self):
        paragraphs = self.soup.find_all('p')
        self.assertIn("Apples are incredibly good for you", paragraphs[0].text)
        self.assertIn("There are over 7,500 different varieties", paragraphs[1].text)

    def test_structure(self):
        self.assertTrue(self.soup.html is not None, "HTML tag should exist")
        self.assertTrue(self.soup.body is not None, "Body tag should exist")
        self.assertTrue(self.soup.head is not None, "Head tag should exist")

if __name__ == '__main__':
    unittest.main()