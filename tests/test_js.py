import unittest

class TestJavaScript(unittest.TestCase):

    def test_dom_content_loaded(self):
        with open('../../examples/a9eb280a-831f-4337-a8fc-5e960fb3cba3/script.js', 'r') as file:
            content = file.read()
            self.assertIn('DOMContentLoaded', content, "DOMContentLoaded event listener should be set up.")

if __name__ == '__main__':
    unittest.main()