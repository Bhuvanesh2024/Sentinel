import requests
from datetime import datetime
import time

url = 'http://localhost:8585/sensor/'
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Api-Key': 'e8abc9f3617a3ed865e61e5cd4d4e1c7'
}

# Simulate multiple LeetCode activities
events = [
    {'url': '/problems/two-sum', 'pageTitle': 'Two Sum', 'eventType': 'page_view'},
    {'url': '/problems/add-two-numbers', 'pageTitle': 'Add Two Numbers', 'eventType': 'page_view'},
    {'url': '/submit/two-sum', 'pageTitle': 'Submit Solution', 'eventType': 'page_edit'},
    {'url': '/problems/longest-substring', 'pageTitle': 'Longest Substring', 'eventType': 'page_view'},
]

for i, event in enumerate(events, 1):
    data = {
        'userName': 'bhuvanesh3602',
        'ipAddress': '103.21.45.67',
        'url': event['url'],
        'userAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0',
        'eventTime': datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3],
        'eventType': event['eventType'],
        'emailAddress': 'bhuvanesh3602@example.com',
        'pageTitle': event['pageTitle']
    }
    
    response = requests.post(url, data=data, headers=headers)
    print(f"{i}. {event['pageTitle']}: Status {response.status_code}")
    time.sleep(1)

print("\n 💯All events sent Check .dashboard at http://localhost:8585/")
