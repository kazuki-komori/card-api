from src.colorPicker import ColorPicker
import os
import cv2
from flask import Flask, request
from flask_cors import CORS, cross_origin
import base64
import io
from PIL import Image

app = Flask(__name__)
CORS(app, support_credentials=True)
app.debug = True


@app.route('/send', methods=['POST'])
@cross_origin(supports_credentials=True)
def send():
    if request.method == 'POST':
        data_path = './data/data.jpg'
        base64_img = request.json["image"]
        img = base64.b64decode(str(base64_img))
        jpg = Image.open(io.BytesIO(img))
        jpg.save(data_path)
        result_img = cv2.imread(data_path)
        res = ColorPicker(result_img).main()
        os.remove(data_path)
        return { "colors": res }

@app.route('/', methods=['GET'])
def index():
    return "<h1>Welcome to our server !!</h1>"

if __name__ == '__main__':
    app.run()
