# Configurations for XSS Finder
TIMEOUT = 5  # Request timeout in seconds

# Default target URL (can be overridden via command line)
TARGET_URL = ""  # Set to empty to require command-line input

# Scan settings
DEFAULT_CATEGORIES = ['basic', 'encoded', 'event_handlers', 'dom_based', 'filter_bypass']
MAX_CONCURRENT_REQUESTS = 5  # For future multi-threading support

# Output settings
LOG_FILE = 'logs/scan.log'
DEFAULT_REPORT_FILE = 'xss_report.json'

