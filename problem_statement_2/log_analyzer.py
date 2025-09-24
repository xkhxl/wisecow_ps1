#!/usr/bin/env python3
import re
from collections import Counter

# Path to your log file
LOG_FILE = "access.log"

# Regex for parsing Apache/Nginx combined log format
log_pattern = re.compile(
    r'(?P<ip>\S+) \S+ \S+ \[(?P<date>.*?)\] "(?P<method>\S+) (?P<url>\S+) \S+" (?P<status>\d{3})'
)

def analyze_log(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()

    status_counts = Counter()
    url_counts = Counter()
    ip_counts = Counter()

    for line in lines:
        match = log_pattern.search(line)
        if match:
            ip = match.group("ip")
            url = match.group("url")
            status = match.group("status")

            status_counts[status] += 1
            url_counts[url] += 1
            ip_counts[ip] += 1

    print("\n===== Log Analysis Report =====")
    print(f"Total requests: {len(lines)}")
    print(f"Total 404 errors: {status_counts['404']}")
    
    print("\nTop 10 Requested Pages:")
    for url, count in url_counts.most_common(10):
        print(f"{url} -> {count} requests")

    print("\nTop 10 IP Addresses:")
    for ip, count in ip_counts.most_common(10):
        print(f"{ip} -> {count} requests")
    print("================================\n")

if __name__ == "__main__":
    analyze_log(LOG_FILE)
