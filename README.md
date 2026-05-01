# XSS Finder

**XSS Finder** is an automated tool designed to detect Cross-Site Scripting (XSS) vulnerabilities in web applications. It uses a comprehensive set of predefined payloads organized by category to scan target URLs and logs the results. Additionally, the tool generates detailed reports of any identified vulnerabilities in JSON format, allowing for easy tracking and analysis.

## 🚀 New Features (Version 2.0)

- **Categorized Payloads**: payloads organized into 5 categories (basic, encoded, event_handlers, dom_based, filter_bypass)
- **Advanced CLI**: Full command-line interface with multiple options
- **Category-based Scanning**: Scan with specific payload categories
- **Multiple Parameter Testing**: Tests against common parameters (q, search, query, input, etc.)
- **URL Path Injection**: Tests payload injection in URL paths
- **Enhanced Reporting**: Comprehensive JSON reports with statistics, risk levels, and recommendations
- **Verbose Mode**: Real-time scan progress output
- **Input Validation**: URL validation and input sanitization utilities
- **Better Logging**: Enhanced logging with parameter, method, and status code information

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Basic Scanning](#basic-scanning)
  - [Advanced Scanning](#advanced-scanning)
  - [CLI Options](#cli-options)
- [Payload Categories](#payload-categories)
- [Configuration](#configuration)
- [Logging](#logging)
- [Report Generation](#report-generation)
- [Testing](#testing)
- [Extending the Tool](#extending-the-tool)
- [Best Practices](#best-practices)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Targeted XSS Scanning**: Input a target URL to test against various XSS payloads
- **Configurable Payloads**: 25+ payloads organized in 5 categories for comprehensive testing
- **Multi-Parameter Testing**: Automatically tests common parameters (q, search, query, input, text, keyword, id, name, page)
- **Multiple Injection Points**: Tests GET parameters, POST data, and URL path injection
- **Detailed Logging**: Capture the results of each scan, including payloads tested, parameters, methods, and status codes
- **Automated Reporting**: Generate comprehensive JSON reports with statistics, risk assessment, and remediation recommendations
- **Customizable Settings**: Set request timeouts, choose payload categories, and manage scan configurations
- **Verbose Output**: Real-time progress tracking during scans
## Installation

### Prerequisites

Ensure that you have `Python 3.x` installed. You can download it from the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/).

### Clone the Repository

```bash
git clone https://github.com/HikmatAsifli/xssFinder.git
cd xssFinder
```


## Install Dependencies

Install the required dependencies using pip:
```bash
pip install -r requirements.txt
```


## Usage

### Basic Scanning

To run a basic scan against a target URL, execute the following command:

```bash
cd src
python main.py -u https://example.com
```

The script will test all payloads against common parameters and log any detected vulnerabilities.

### Advanced Scanning

XSS Finder offers several advanced options for customized scanning:

#### CLI Options

```bash
python main.py --help

usage: main.py [-h] [-u URL] [-c {basic,encoded,event_handlers,dom_based,filter_bypass,all}] [-v] [-r REPORT] [-t TIMEOUT]

XSS Finder - Automated XSS Vulnerability Scanner

options:
  -h, --help            show this help message and exit
  -u URL, --url URL     Target URL to scan
  -c {basic,encoded,event_handlers,dom_based,filter_bypass,all}, --category 
                        Payload category to test (default: all)
  -v, --verbose         Enable verbose output
  -r REPORT, --report REPORT
                        Generate report to specified file
  -t TIMEOUT, --timeout TIMEOUT
                        Request timeout in seconds (default: 5)
```

#### Examples

**Scan with verbose output:**
```bash
python main.py -u https://example.com -v
```

**Scan only basic payloads:**
```bash
python main.py -u https://example.com -c basic
```

**Custom timeout and report file:**
```bash
python main.py -u https://example.com -t 10 -r custom_report.json
```

**Scan with filter bypass payloads:**
```bash
python main.py -u https://example.com -c filter_bypass -v
```

## Payload Categories

XSS Finder includes 25+ payloads organized into 5 categories:

| Category | Description | Count |
|----------|-------------|-------|
| `basic` | Standard XSS payloads | 5 |
| `encoded` | URL and HTML encoded payloads | 4 |
| `event_handlers` | Event handler-based payloads | 5 |
| `dom_based` | DOM-based XSS payloads | 3 |
| `filter_bypass` | WAF/filter bypass payloads | 5 |

### Category Examples

**Basic:**
```python
"<script>alert('XSS')</script>"
"<img src=x onerror=alert('XSS')>"
"<svg onload=alert(1)>"
```

**Encoded:**
```python
"%3Cscript%3Ealert('XSS')%3C/script%3E"
"&#60;script&#62;alert('XSS')&#60;/script&#62;"
```

**Filter Bypass:**
```python
"<ScRiPt>alert('XSS')</ScRiPt>"
"<scr<script>ipt>alert('XSS')</scr</script>ipt>"
```
## Configuration

The `src/configs/settings.py` file contains key settings for the script:

- **TIMEOUT**: Request timeout in seconds (default: 5)
- **TARGET_URL**: Default target URL (empty by default, use CLI to specify)
- **DEFAULT_CATEGORIES**: List of payload categories to use
- **LOG_FILE**: Location of the log file
- **DEFAULT_REPORT_FILE**: Default report output filename

*Example settings:*

```python
TIMEOUT = 5  # Request timeout in seconds
TARGET_URL = ""  # Empty requires CLI input
DEFAULT_CATEGORIES = ['basic', 'encoded', 'event_handlers', 'dom_based', 'filter_bypass']
```

## Logging

XSS Finder maintains a detailed log of all scan results in `logs/scan.log`. The log contains comprehensive information about each test:

```log
2024-09-14 10:15:30 Payload: <script>alert('XSS')</script>, Vulnerable: True, Parameter: q, Method: GET/POST, Status: 200
2024-09-14 10:15:32 Payload: <img src=x onerror=alert('XSS')>, Vulnerable: False, Parameter: search, Method: GET/POST, Status: 200
```

## Report Generation

At the end of each scan, XSS Finder generates a comprehensive JSON report. The report includes:

- **Metadata**: Tool version, generation timestamp
- **Scan Summary**: Target URL, total tests, vulnerabilities found, risk level
- **Vulnerabilities by Category**: Grouped findings by payload category
- **Vulnerabilities by Parameter**: Grouped findings by vulnerable parameter
- **Detailed Findings**: Complete list of all vulnerabilities
- **Recommendations**: Security remediation suggestions

### Sample Report Structure

```json
{
    "report_metadata": {
        "generated_at": "2024-09-14T10:15:30",
        "tool_name": "XSS Finder",
        "version": "2.0"
    },
    "scan_summary": {
        "target_url": "https://example.com",
        "total_tests": 25,
        "vulnerabilities_found": 3,
        "risk_level": "MEDIUM"
    },
    "vulnerabilities_by_category": {
        "basic": [...],
        "event_handlers": [...]
    },
    "recommendations": [
        "Implement proper input validation and sanitization",
        "Use Content Security Policy (CSP) headers",
        "Encode output data appropriately"
    ]
}
```

## Testing

Run the test suite to verify functionality:

```bash
# Run utility tests
cd tests
python test_utils.py -v

# Run scanner tests (may take longer due to network requests)
python test_scanner.py -v
```

## Extending the Tool

### Adding New Payloads

To add new XSS payloads, edit `src/payloads/xss_payloads.py`:

```python
PAYLOADS = {
    "basic": [
        "<script>alert('XSS')</script>",
        # Add your new payloads here
    ],
    # ... other categories
}
```

### Custom Parameters

To test additional parameters, modify the `common_params` list in `src/scanner.py`:

```python
common_params = ['q', 'search', 'query', 'input', 'text', 'keyword', 'id', 'name', 'page', 'your_param']
```
## Extending the Tool
### Adding New Payloads

To add new XSS payloads, simply append them to the `PAYLOADS` list in `src/payloads/payloads.py`. You can also import payloads from external sources or files.
### Advanced Logging

For more advanced logging (e.g., recording HTTP response headers, request bodies), extend the `log_scan_results` function to capture additional information about each request.

### Multi-threaded Scanning

For faster scanning, implement multi-threading using Python’s `threading` module. This can be particularly useful when scanning multiple URLs or a target with a large number of input fields.

```python
import threading

# Example of multi-threaded scanning
thread = threading.Thread(target=scan_url, args=(url,))
thread.start()
```
## Best Practices

- Always seek permission before testing websites for vulnerabilities.
- Update the payloads regularly to include new XSS patterns.
- Keep the logging and reporting structured for easy analysis.
## Contributing

We welcome contributions! If you would like to report an issue, suggest a feature, or submit a pull request, please follow the standard GitHub workflow.

1. Fork the repository
1. Create your feature branch (`git checkout -b feature/your-feature`)
1. Commit your changes (`git commit -am 'Add your feature'`)
1. Push to the branch (`git push origin feature/your-feature`)
1. Open a pull request
## License

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License - see the LICENSE file for details.


