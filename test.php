<?php
require 'vendor/autoload.php';

// Test 1: Normal login
$tracker = new TirrenoTracker('http://localhost:8585', 'e8abc9f3617a3ed865e61e5cd4d4e1c7');
$tracker->setUserName('user123')
    ->setEmailAddress('test@example.com')
    ->setIpAddress('192.168.1.1')
    ->setEventTypeAccountLogin()
    ->track();
echo "Test 1: Normal login sent\n";

// Test 2: Suspicious login (different country)
$tracker = new TirrenoTracker('http://localhost:8585', 'e8abc9f3617a3ed865e61e5cd4d4e1c7');
$tracker->setUserName('user123')
    ->setEmailAddress('test@example.com')
    ->setIpAddress('185.220.101.1')
    ->setEventTypeAccountLogin()
    ->track();
echo "Test 2: Suspicious login sent\n";

// Test 3: Multiple failed logins (credential stuffing)
for ($i = 0; $i < 10; $i++) {
    $tracker = new TirrenoTracker('http://localhost:8585', 'e8abc9f3617a3ed865e61e5cd4d4e1c7');
    $tracker->setEmailAddress('test@example.com')
        ->setIpAddress('192.168.1.1')
        ->setEventTypeAccountLoginFail()
        ->track();
}
echo "Test 3: 10 failed logins sent\n";

echo "\nAll events sent! Check dashboard at http://localhost:8585\n";
