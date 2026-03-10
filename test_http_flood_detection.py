import requests
from datetime import datetime
import time
import random

url = 'http://localhost:8585/sensor/'
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Api-Key': 'e8abc9f3617a3ed865e61e5cd4d4e1c7'
}

def send_event(user, ip, event_url, title, event_type='page_view'):
    data = {
        'userName': user,
        'ipAddress': ip,
        'url': event_url,
        'userAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0',
        'eventTime': datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3],
        'eventType': event_type,
        'emailAddress': f'{user}@example.com',
        'pageTitle': title
    }
    return requests.post(url, data=data, headers=headers)

# Normal user behavior (human-like)
print("📊 Simulating NORMAL user behavior...")
normal_pages = ['/problems/two-sum', '/problems/add-two-numbers', '/submit/two-sum', '/problems/longest-substring']
for page in normal_pages:
    send_event('bhuvanesh3602', '103.21.45.67', page, page.split('/')[-1], 'page_view')
    time.sleep(random.uniform(2, 5))  # Human reading time
print("✅ Normal behavior complete\n")

# HTTP-GET flood attack pattern
print("⚠️  Simulating HTTP-GET FLOOD attack...")
attack_urls = ['/problems/two-sum', '/api/submissions', '/problems/list', '/contest/weekly']
for i in range(50):  # Rapid requests
    page = random.choice(attack_urls)
    send_event('attacker_bot', '45.142.212.61', page, 'Bot Request', 'page_view')
    time.sleep(0.1)  # Abnormally fast
print("⚠️  Attack simulation complete\n")

print("🔍 Check tirreno dashboard for anomaly detection at http://localhost:8585/")
