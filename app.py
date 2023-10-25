from flask import Flask, render_template, request
import cv2
import numpy as np
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/upload", methods=["POST"])
def upload():
    data = request.json["image"]
    # Data URLをデコード
    header, encoded = data.split(",", 1)
    binary_data = base64.b64decode(encoded)

    # バイナリデータをNumPy配列に変換
    nparr = np.frombuffer(binary_data, np.uint8)

    # OpenCVを使用して画像を読み込む
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # 画像を保存
    cv2.imwrite("./received_image.png", img)