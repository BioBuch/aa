from flask import Flask, request, jsonify
import base64
from io import BytesIO
from PIL import Image

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    if 'image' in data:
        image_data = base64.b64decode(data['image'])
        image = Image.open(BytesIO(image_data))

        # Here you would run your emotion analysis (mock response for now)
        mood = "happy"  # Replace with your actual analysis logic

        return jsonify({'mood': mood})
    return jsonify({'error': 'No image provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)