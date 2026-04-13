import unittest
from cssutils import parseFile

class TestCSSStyles(unittest.TestCase):

    def setUp(self):
        self.sheet = parseFile('../../examples/a9eb280a-831f-4337-a8fc-5e960fb3cba3/styles.css')

    def test_body_background_color(self):
        rules = [rule for rule in self.sheet if rule.type == rule.STYLE_RULE]
        body_rule = next(rule for rule in rules if rule.selectorText == 'body')
        background_color = body_rule.style.getPropertyValue('background-color').strip()
        self.assertEqual(background_color, '#f4f4f9', "Background color of body should be #f4f4f9")

    def test_header_background(self):
        rules = [rule for rule in self.sheet if rule.type == rule.STYLE_RULE]
        header_rule = next(rule for rule in rules if rule.selectorText == 'header')
        background = header_rule.style.getPropertyValue('background').strip()
        self.assertEqual(background, '#35424a', "Header background should be #35424a")

if __name__ == '__main__':
    unittest.main()