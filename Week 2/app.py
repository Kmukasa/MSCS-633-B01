from flask import Flask, render_template, request, jsonify
import qrcode
import io
import base64
from urllib.parse import urlparse

app = Flask(__name__)


def is_valid_url(url):
    """Validate if the provided string is a valid URL."""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except Exception:
        return False


@app.route('/')
def index():
    """Serve the frontend HTML page."""
    return render_template('index.html')


@app.route('/generate-qr', methods=['POST'])
def generate_qr():
    """Generate a QR code from the provided URL and return it as base64."""
    try:
        # Get JSON data from request
        data = request.get_json()
        
        if not data or 'url' not in data:
            return jsonify({
                'success': False,
                'error': 'No URL provided'
            }), 400
        
        url = data['url']
        
        # Validate URL
        if not is_valid_url(url):
            return jsonify({
                'success': False,
                'error': 'Invalid URL format'
            }), 400
        
        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        
        # Create image
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Convert image to base64
        buffer = io.BytesIO()
        img.save(buffer, format='PNG')
        buffer.seek(0)
        img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        
        return jsonify({
            'success': True,
            'qr_code': img_base64
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Error generating QR code: {str(e)}'
        }), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

