# 플라스크 rest-api 생성
import io
import shutil
import os
import sys
from cv2 import matchShapes
import torch
import json
import glob

from PIL import Image
from flask import Flask, render_template, request, redirect
from flask_cors import CORS, cross_origin

from models.tumor_detect import tumor_detect
sys.path.append("../tuna-ai-app")
from ipAdress import ipAdress


# 서버 띄우고 접속 허용
# 'static_url_path = '로 특정 url 또는 'static_folder = ' 로 특정 폴더를 지정해주어야 해당 url 혹은 폴더의 파일은
# static하다고 판단(동적 변화 X)하여 그대로 불러올 수 있게 된다. (default 폴더명 = static)
# 이미지, css 파일 등이 가능
app = Flask(__name__, static_folder='./postman')
# 보안해제
CORS(app)

# 변수
ipAdress = ipAdress
port = 5001
# True: 진단한 적 있음 / False: 진단한 적 없음


def read_file():
    if "file" not in request.files:
        return redirect(request.url)
    file = request.files["file"]
    if not file:
        return
    # app에서 넘겨준 form의 파일명
    file_name = request.form["fileName"]
    # 이미지 저장 폴더 생성 및 파일 저장
    save_path = './postman/' + file_name
    path_original = save_path + "/original"
    return file, file_name, save_path, path_original


@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        file, file_name, save_path, path_original = read_file()
        detection = "첫 진단"  # 임시, 나중에 삭제
    # 이미지 파일 읽기
        img_bytes = file.read()
        img = Image.open(io.BytesIO(img_bytes))

        if os.path.isdir(path_original):
            shutil.rmtree(path_original)  # 있으면 지우기

        os.makedirs(path_original)
        save_file = path_original + "/" + file_name + ".jpg"
        img.save(save_file)

        with torch.no_grad():
            img_saved, diagnosis = tumor_detect(path_original)
            if img_saved != None:
                message = {
                    "diagnosis": diagnosis,
                    "original_image": f"http://localhost:{port}" + save_file.strip("."),
                    "img_url": f"http://localhost:{port}" + img_saved.strip("."),
                    "detection": detection,
                }
            elif img_saved == None:
                message = {
                    "diagnosis": diagnosis,
                    "original_image": f"http://localhost:{port}" + save_file.strip("."),
                    "detection": detection,
                }
            return message


@app.route("/predict2", methods=["GET", "POST"])
def predict2():
    if request.method == "POST":
        file, file_name, save_path, path_original = read_file()
        if os.path.isdir(save_path):
            detection = "진단된 것 가져오기"  # 임시, 나중에 삭제
            save_file = path_original + "/" + file_name + ".jpg"
            if os.path.isdir(save_path + "/detected"):
                diagnosis = "뇌종양입니다."
                img_saved = save_path + "/detected" + "/" + file_name + ".jpg"
            else:
                diagnosis = "이상 소견 없음"
                img_saved = None
            with torch.no_grad():
                if img_saved != None:
                    message = {
                        "diagnosis": diagnosis,
                        "original_image": ipAdress + f"{port}" + save_file.strip("."),
                        "img_url": ipAdress + f"{port}" + img_saved.strip("."),
                        "detection": detection,

                    }
                elif img_saved == None:
                    message = {
                        "diagnosis": diagnosis,
                        "original_image": ipAdress + f"{port}" + save_file.strip("."),
                        "detection": detection,
                    }
        else:
            message = {
                "error": "불러오기 실패",
            }
        return message


if __name__ == '__main__':
    # debug=True causes Restarting with stat
    app.run(host="0.0.0.0", port=port)
