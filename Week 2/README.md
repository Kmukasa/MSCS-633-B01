# Python QR Code Generator

The following project is a qr code generator. The main page allows a user to put in a url and get a qrcode generated to visit the provided url. The url is validated before a call to the generate-qr enpoint is made. This uses the python [qrcode](https://pypi.org/project/qrcode/) library to convert the url into a qrcode. The encoded bytes for the image are then sent back in the response to be renderd on the page.

## Set up the application

### 1. Open

```bash
cd "MSCS-633-B01/Week 2"
```

### 2. Activate the virtual environment

```bash
source venv/bin/activate
```

### 3. Run the Flask application

```bash
python app.py
```

### 4. Access the application

Open your web browser and navigate to:

```
http://localhost:5001
```

or

```
http://127.0.0.1:5001
```

## Running the Application

1. Enter a URL in the input field (e.g., `https://www.google.com`)
2. Click "Generate QR Code"
3. The QR code will be displayed on the page
4. You can scan the QR code with your phone to verify it works!

## Testing the API Endpoint Directly

You can also test the API endpoint using curl:

```bash
curl -X POST http://localhost:5001/generate-qr \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.example.com"}'
```
