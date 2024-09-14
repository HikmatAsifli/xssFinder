import requests
from payloads.xss_payloads import PAYLOADS

class Scanner:
    def __init__(self, target_url):
        self.target_url = target_url

    def test_payload(self, payload):
        # Prepare the request with the payload
        try:
            response = requests.get(self.target_url, params={'q': payload})
            if payload in response.text:
                return True
            return False
        except requests.exceptions.RequestException as e:
            print(f"Error testing payload: {payload}, Error: {e}")
            return False

    def run_scan(self):
        results = []
        for payload in PAYLOADS:
            is_vulnerable = self.test_payload(payload)
            results.append({'payload': payload, 'vulnerable': is_vulnerable})
        return results
