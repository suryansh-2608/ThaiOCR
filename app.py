from flask import Flask, request, jsonify
from flask_cors import CORS
from google.cloud import vision_v1
from google.cloud.vision_v1 import types

app = Flask(__name__)
CORS(app)

@app.route('/api/ocr', methods=['POST'])
def ocr():
    # You need to replace 'YOUR_GOOGLE_VISION_API_KEY' with your actual API key
    client = vision_v1.ImageAnnotatorClient()

    image = request.files.get('image').read()
    image = types.Image(content=image)

    response = client.text_detection(image=image)
    texts = response.text_annotations

    if texts:
        result = {
            "identification_number": "123456789",
            "name": "John",
            "last_name": "Doe",
            "date_of_birth": "01/01/1990",
            "date_of_issue": "01/01/2022",
            "date_of_expiry": "01/01/2025"
        }
        return jsonify(result)
    else:
        return jsonify({"error": "OCR failed"}), 400

if __name__ == '__main__':
    app.run(debug=True)
