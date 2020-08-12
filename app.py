from src.colorPicker import ColorPicker
import cv2
from flask import Flask, request
import base64
import io
from PIL import Image

app = Flask(__name__)
app.debug = True


@app.route('/send', methods=['POST'])
def send():
    if request.method == 'POST':
        image = request.data
        image = Image.open(io.BytesIO(image))
        # データを一時保存
        image.save('./data/data.jpg')
        # 配列で色を返す
        img = cv2.imread('./data/data.jpg')
        res = ColorPicker(img).main()
        return {"colors": res}


if __name__ == '__main__':
    app.run()
