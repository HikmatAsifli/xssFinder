import unittest
from src.scanner import Scanner

class TestScanner(unittest.TestCase):

    def test_payload(self):
        scanner = Scanner("http://example.com")
        payload = "<script>alert('XSS')</script>"
        result = scanner.test_payload(payload)
        self.assertIsInstance(result, bool)

if __name__ == '__main__':
    unittest.main()
