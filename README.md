# IoT Device Payload API

A Django REST API for receiving and processing IoT device payloads with token authentication. - by victor wang

## Features

- Token-based authentication
- Base64 payload decoding
- Pass/fail classification
- Duplicate prevention via frame counter (fCnt)
- Device status tracking

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Create superuser:**
   ```bash
   python manage.py createsuperuser
   ```

4. **Generate auth token:**
   ```bash
   python manage.py shell
   >>> from django.contrib.auth.models import User
   >>> from rest_framework.authtoken.models import Token
   >>> user = User.objects.get(username='your_username')
   >>> token = Token.objects.create(user=user)
   >>> print(token.key)
   ```

5. **Run server:**
   ```bash
   python manage.py runserver
   ```

## API Usage

### Endpoint
`POST /api/payload/`

### Headers
```
Authorization: Token <your_token>
Content-Type: application/json
```

### Request Body
```json
{
  "fCnt": 100,
  "devEUI": "abcdabcdabcdabcd",
  "raw_data": "AQ=="
}
```

### Response (Success - 201)
```json
{
  "id": 1,
  "devEUI": "abcdabcdabcdabcd",
  "fCnt": 100,
  "status": "passing",
  "decoded_data": "01",
  "created_at": "2024-01-01T12:00:00Z"
}
```

### Response (Duplicate - 400)
```json
{
  "error": "Duplicate payload. This fCnt already exists for this device."
}
```

## Environment Variables

Create a `.env` file:
```
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

## Models

- **Device**: Stores device identifier (devEUI) and latest status
- **Payload**: Stores frame counter, raw/decoded data, and status

## Status Logic

- Decoded hex value `01` → `passing`
- Any other value → `failing`