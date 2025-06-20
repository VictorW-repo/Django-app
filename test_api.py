import requests
import json

# Replace with your actual token from step 2
TOKEN = "3180853e28e2758eba03f965d1082c5b6f675c8f"
BASE_URL = "http://127.0.0.1:8000"

# Test payload - "AQ==" decodes to hex "01" which means "passing"
payload_passing = {
    "fCnt": 100,
    "devEUI": "abcdabcdabcdabcd",
    "raw_data": "AQ=="  # Base64 for hex "01"
}

# Test payload - "AA==" decodes to hex "00" which means "failing"
payload_failing = {
    "fCnt": 101,
    "devEUI": "abcdabcdabcdabcd",
    "raw_data": "AA=="  # Base64 for hex "00"
}

headers = {
    "Authorization": f"Token {TOKEN}",
    "Content-Type": "application/json"
}

print("Testing IoT Payload API...")
print("-" * 50)

# Test 1: Passing payload
print("\n1. Sending PASSING payload:")
response = requests.post(f"{BASE_URL}/api/payload/", json=payload_passing, headers=headers)
print(f"Status: {response.status_code}")
print(f"Response: {json.dumps(response.json(), indent=2)}")

# Test 2: Failing payload
print("\n2. Sending FAILING payload:")
response = requests.post(f"{BASE_URL}/api/payload/", json=payload_failing, headers=headers)
print(f"Status: {response.status_code}")
print(f"Response: {json.dumps(response.json(), indent=2)}")

# Test 3: Duplicate (should fail)
print("\n3. Sending DUPLICATE payload (should fail):")
response = requests.post(f"{BASE_URL}/api/payload/", json=payload_passing, headers=headers)
print(f"Status: {response.status_code}")
print(f"Response: {json.dumps(response.json(), indent=2)}")

# Test 4: No auth (should fail)
print("\n4. Sending without auth token (should fail):")
response = requests.post(f"{BASE_URL}/api/payload/", json=payload_failing)
print(f"Status: {response.status_code}")
print(f"Response: {json.dumps(response.json(), indent=2)}")