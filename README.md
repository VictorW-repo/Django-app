# IoT Payload Parser

## Project Goal
Provide a secure Django REST API that ingests, de‐duplicates and interprets payloads from IoT devices, marking each as passing or failing based on its decoded data.

## Features
- **Token Authentication**  
- **Duplicate Prevention** via `fCnt` per device  
- **Automatic Base64→Hex Decoding**  
- **Pass/Fail Status** (hex `"1"` ⇒ passing; otherwise failing)  
- **Device Status Tracking** (latest pass/fail)

## Tech Stack
- Python 3  
- Django 5  
- Django REST Framework  

## Models
- **Device**  
  - `devEUI` (unique identifier)  
  - `latest_status` (passing / failing)  
- **Payload**  
  - FK to `Device` via `devEUI`  
  - `fCnt` (message counter, unique per device)  
  - `raw_data` (Base64 string)  
  - `hex_data` (decoded)  
  - `status` (passing / failing)

## Setup

1. Clone & enter project  
   ```bash
   git clone https://github.com/<your-org>/iot-parser.git
   cd iot-parser
