# Configurations for XSS Finder
TIMEOUT = 5  # Request timeout

# Configurations for XSS Finder
TARGET_URL = input("Enter the target URL: ")

# Check if the target URL has a scheme, if not, add 'http://'
if not TARGET_URL.startswith(('http://', 'https://')):
    TARGET_URL = 'http://' + TARGET_URL

