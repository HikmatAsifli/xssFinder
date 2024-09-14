import json

def generate_report(vulnerabilities, file_name="xss_report.json"):
    with open(file_name, 'w') as report_file:
        json.dump(vulnerabilities, report_file, indent=4)

    print(f"Report generated: {file_name}")
