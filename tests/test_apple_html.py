import unittest
from bs4 import BeautifulSoup

class TestAppleHtml(unittest.TestCase):
    def setUp(self):
        with open('../../examples/4511ef29-a813-476c-97ed-28c92f502ccb/apple.html', 'r', encoding='utf-8') as file:
            self.soup = BeautifulSoup(file, 'html.parser')

    def test_title(self):
        title = self.soup.title.string
        self.assertEqual(title, 'About Apple', "Title should be 'About Apple'.")

    def test_h1(self):
        h1 = self.soup.find('h1').string
        self.assertEqual(h1, 'Apple', "<h1> should be 'Apple'.")

    def test_h2_health_benefits(self):
        h2_health = self.soup.find('h2', string='Health Benefits')
        self.assertIsNotNone(h2_health, "There should be an <h2> tag with 'Health Benefits'.")

    def test_h2_varieties(self):
        h2_varieties = self.soup.find('h2', string='Varieties')
        self.assertIsNotNone(h2_varieties, "There should be an <h2> tag with 'Varieties'.")

    def test_paragraph_existence(self):
        paragraphs = self.soup.find_all('p')
        self.assertGreaterEqual(len(paragraphs), 2, "There should be at least two <p> tags, one for each section.")

    def test_meta_charset(self):
        meta_charset = self.soup.find('meta', charset='UTF-8')
        self.assertIsNotNone(meta_charset, "There should be a meta charset='UTF-8' tag.")

    def test_meta_viewport(self):
        meta_viewport = self.soup.find('meta', attrs={'name': 'viewport'})
        self.assertIsNotNone(meta_viewport, "There should be a meta name='viewport' tag.")

    def test_styling_existence(self):
        style = self.soup.find('style')
        self.assertIsNotNone(style, "There should be a <style> tag present.")

if __name__ == '__main__':
    unittest.main()
