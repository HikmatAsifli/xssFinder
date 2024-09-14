# XSS Finder

**XSS Finder** is an automated tool designed to detect Cross-Site Scripting (XSS) vulnerabilities in web applications. It uses a set of predefined payloads to scan target URLs and logs the results. Additionally, the tool generates detailed reports of any identified vulnerabilities in JSON format, allowing for easy tracking and analysis.


## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Basic Scanning](#basic-scanning)
  - [Advanced Scanning](#advanced-scanning)
- [Configuration](#configuration)
- [Logging](#logging)
- [Report Generation](#report-generation)
- [Extending the Tool](#extending-the-tool)
- [Best Practices](#best-practices)
- [Contributing](#contributing)
- [License](#license)
## Features

- **Targeted XSS Scanning**: Input a target URL to test against various XSS payloads.
- **Configurable Payloads**: Easily add or modify payloads for testing.
- **Detailed Logging**: Capture the results of each scan, including payloads tested and vulnerabilities found.
- **Automated Reporting**: Generate comprehensive JSON reports of vulnerabilities.
- **Customizable Settings**: Set request timeouts, and log locations, and manage scan configurations with ease.
## Installation

### Prerequisites

Ensure that you have `Python 3.x` installed. You can download it from the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/).

### Clone the Repository

```bash
git clone https://github.com/HikmatAsifli/xssFinder.gitk
cd xssFinder
```


## Install Dependencies

Install the required dependencies using pip:
```bash
pip install -r requirements.txt
```


## Usage

Basic Scanning

To run a basic scan against a target URL, execute the following command:

```bash
python src/main.py
```

You will be prompted to enter the target URL:

```bash 
Enter the target URL: https://example.com
```
The script will then inject predefined XSS payloads and log any detected vulnerabilities.
## Advanced Scanning

For advanced users, XSS Finder offers several customization options. You can modify payloads, adjust settings, and generate more comprehensive reports.

### Custom Payloads

To use custom payloads, simply modify or add new payloads to the `src/payloads/payloads.py` file:

```python
PAYLOADS = [
    "<script>alert('XSS')</script>",
    "<img src=x onerror=alert('XSS')>",
    "';alert(String.fromCharCode(88,83,83))//",
    "<svg onload=alert(1)>"
]
```
## Timeout Configuration

If you need to adjust the request timeout for slower servers, modify the TIMEOUT variable in settings.py:

```pyhton
TIMEOUT = 10  # Set timeout to 10 seconds
```
## Batch Scanning

You can scan multiple URLs by looping through them in the `main.py` file. For example:

```python
urls = ["https://example1.com", "https://example2.com"]

for url in urls:
    # Call scanner for each URL
    scan_url(url)
```
## Configuration

The `config/settings.py` file contains key settings for the script:

- **TARGET_URL**: Input the URL for scanning. This can be set directly or prompted during runtime.
- **TIMEOUT**: Define the request timeout in seconds.
*Example settings:*

```python
TARGET_URL = input("Enter the target URL: ")
TIMEOUT = 5  # Request timeout in seconds
```
## Payload Configuration

Payloads are defined in `src/payloads/payloads.py`. Modify the predefined payloads or add new ones to extend the scanning capabilities:

```python
PAYLOADS = [
    "<script>alert('XSS')</script>",
    "<img src=x onerror=alert('XSS')>",
    "';alert(String.fromCharCode(88,83,83))//",
    "<svg onload=alert(1)>"
]
```
## Logging

XSS Finder maintains a detailed log of all scan results in `logs/scan.log`. The log contains information about which payloads were tested and whether the target was vulnerable:

```log
2024-09-14 10:15:30 Payload: <script>alert('XSS')</script>, Vulnerable: True
2024-09-14 10:15:32 Payload: <img src=x onerror=alert('XSS')>, Vulnerable: False
```

To customize the logging format or log location, edit `utils/utils.py`:

```python
logging.basicConfig(filename='logs/scan.log',
                    format='%(asctime)s %(message)s',
                    level=logging.INFO)
```
## Log Customization

You can also log additional data such as HTTP responses, payload execution time, and more by extending the `log_scan_results` function in `utils/utils.py`.
## Report Generation
At the end of each scan, XSS Finder generates a JSON report detailing the vulnerabilities found. The report is saved as `xss_report.json` in the project directory and includes all tested payloads and the vulnerability status of the target.

To customize report generation, edit `src/reports/report_generator.py`:

```python
def generate_report(vulnerabilities, file_name="xss_report.json"):
    with open(file_name, 'w') as report_file:
        json.dump(vulnerabilities, report_file, indent=4)
    print(f"Report generated: {file_name}")
```
### Sample Report

```json
{
    "target_url": "https://example.com",
    "vulnerabilities": [
        {
            "payload": "<script>alert('XSS')</script>",
            "vulnerable": true
        },
        {
            "payload": "<img src=x onerror=alert('XSS')>",
            "vulnerable": false
        }
    ]
}
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


