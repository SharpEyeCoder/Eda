import unittest
from bs4 import BeautifulSoup

class TestHTMLStructure(unittest.TestCase):

    def setUp(self):
        with open('../../examples/a9eb280a-831f-4337-a8fc-5e960fb3cba3/index.html', 'r') as file:
            self.soup = BeautifulSoup(file, 'html.parser')

    def test_header_exists(self):
        header = self.soup.find('header')
        self.assertIsNotNone(header, "Header element should exist")

    def test_main_sections(self):
        sections = self.soup.find_all('section')
        self.assertEqual(len(sections), 4, "There should be four section elements")

    def test_contact_information(self):
        contact_section = self.soup.find(id='contact')
        self.assertIn('contact@flux-platform.com', contact_section.text, "Contact email should be present")

if __name__ == '__main__':
    unittest.main()