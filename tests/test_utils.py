import unittest
from src.utils.utils import log_scan_results

class TestUtils(unittest.TestCase):

    def test_log_scan_results(self):
        # Test logging function with sample data
        results = [{'payload': "<script>alert('XSS')</script>", 'vulnerable': True}]
        log_scan_results(results)
        # Check if the log file exists and contains the right log
        with open('logs/scan.log', 'r') as log_file:
            logs = log_file.read()
            self.assertIn("Payload: <script>alert('XSS')</script>, Vulnerable: True", logs)

if __name__ == '__main__':
    unittest.main()
