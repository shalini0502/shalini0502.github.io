from flask import Flask, render_template, request
from PIL import Image
import pytesseract

app = Flask(__name__)

# Set the path to the Tesseract executable (Change this to your Tesseract installation path)
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'  # Default path for Tesseract on Replit

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    handwriting_image = request.files['handwritingImage']
    image = Image.open(handwriting_image)

    # Perform OCR using Tesseract-OCR
    text = pytesseract.image_to_string(image)
    print(text)
    return text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
