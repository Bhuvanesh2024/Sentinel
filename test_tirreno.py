import requests
from datetime import datetime

url = 'http://localhost:8585/sensor/'
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Api-Key': 'e8abc9f3617a3ed865e61e5cd4d4e1c7'
}

# Test with your LeetCode username
data = {
    'userName': 'bhuvanesh3602',
    'ipAddress': '103.21.45.67',
    'url': '/problems/two-sum',
    'userAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0',
    'eventTime': datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3],
    'eventType': 'page_view',
    'emailAddress': 'bhuvanesh3602@example.com',
    'pageTitle': 'Two Sum - LeetCode'
}

response = requests.post(url, data=data, headers=headers)
print(f"Status: {response.status_code}")
print(f"Response: {response.text}")
