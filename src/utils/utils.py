import logging

def setup_logging():
    logging.basicConfig(filename='logs/scan.log', 
                        format='%(asctime)s %(message)s', 
                        level=logging.INFO)

def log_scan_results(results):
    setup_logging()
    for result in results:
        payload = result['payload']
        vulnerable = result['vulnerable']
        logging.info(f"Payload: {payload}, Vulnerable: {vulnerable}")
