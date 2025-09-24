#!/usr/bin/env python3
import requests

# URL of the application to check
URL = "http://example.com"

def check_app_health(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"[UP] Application is running fine at {url}")
        else:
            print(f"[DOWN] Application returned status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"[DOWN] Could not reach application: {e}")

if __name__ == "__main__":
    check_app_health(URL)
