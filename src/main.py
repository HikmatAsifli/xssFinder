from scanner import Scanner
from configs.settings import TARGET_URL
from utils.utils import log_scan_results

if TARGET_URL:
    scanner = Scanner(TARGET_URL)
    scan_results = scanner.run_scan()
    log_scan_results(scan_results)
    print("Scan completed. Results saved in logs/scan.log")
else:
    print("No URL provided. Exiting.")
