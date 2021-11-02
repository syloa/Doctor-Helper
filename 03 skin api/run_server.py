# from flask_cors import CORS, cross_origin
# from flask import Flask, render_template, request, redirect
# from PIL import Image
# import os
# import shutil
# import io
# from numpy import random
# import torch.backends.cudnn as cudnn
# import torch
# import cv2
# from pathlib import Path
# import time
# import argparse
# from flask import Flask, jsonify
# from torchvision import models
# from torch._C import device
# import os
# import cv2
# import itertools
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
# import numpy as np
# import pandas as pd
# from tqdm import tqdm
# from glob import glob
# from PIL import Image
# # pytorch libraries
# import torch
# from torch import optim, nn
# from torch.autograd import Variable
# from torch.utils.data import DataLoader, Dataset
# from torchvision import models, transforms
# import argparse

# # # sklearn libraries
# # from sklearn.metrics import confusion_matrix
# # from sklearn.model_selection import train_test_split
# # from sklearn.metrics import classification_report

# # to make the results are reproducible
# np.random.seed(10)
# torch.manual_seed(10)
# torch.cuda.manual_seed(10)

# # from . import SkinModel
# # export SKIN_MODEL_LOCATION = classifier_epoch_dict.pth


# 플라스크 rest-api 생성

import glob
import json
import torch
from cv2 import matchShapes
from models.classificationA import validate
from flask_cors import CORS, cross_origin
from flask import Flask, render_template, request, redirect
from PIL import Image
import io
import shutil
import os
import sys
sys.path.append("../tuna-ai-app")
from ipAdress import ipAdress

app = Flask(__name__, static_folder='./postman')
CORS(app)

ipAdress = ipAdress
port = 5002

def read_file():
    if "file" not in request.files:
        return redirect(request.url)
    file = request.files["file"]
    if not file:
        return
    # app에서 넘겨준 form의 파일명
    file_name = request.form["fileName"]
    # 이미지 저장 폴더 생성 및 파일 저장
    save_path = './postman/' + 'original/' + file_name
    path_original = save_path
    save_file = save_path + "/" + file_name + ".jpg"
    return file, file_name, save_path, path_original, save_file


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == "POST":
        file, file_name, save_path, path_original, save_file = read_file()

        if "file" not in request.files:
            return redirect(request.url)
        file = request.files["file"]
        if not file:
            return
        # app에서 넘겨준 form의 파일명
        file_name = request.form["fileName"]

        # 이미지 파일 읽기
        img_bytes = file.read()
        img = Image.open(io.BytesIO(img_bytes))

        # if os.path.isdir(path_original):
        #     shutil.rmtree(path_original)  # 있으면 지우기

        save_path = './postman/' + 'original/' + file_name
        if os.path.isdir(save_path):
            shutil.rmtree(save_path)

        # os.makedirs(save_path)
        os.makedirs(save_path)
        save_file = save_path + "/" + file_name + ".jpg"
        img.save(save_file)

        with torch.no_grad():
            img_saved, diagnosis = validate(save_path)
            if img_saved != None:
                message = {
                    "diagnosis": diagnosis,
                    "img_url": ipAdress + f"{port}" + img_saved.strip("."),
                    # "detection" : detection,
                }
                print(img_saved)
            elif img_saved == None:
                message = {
                    "diagnosis": diagnosis,
                    "original_image": ipAdress + f"{port}" + save_file.strip("."),
                    # "detection" : detection,
                }
            return message

        # prediction = model(img)
        # predicted_class = SkinClasses[torch.argmax(prediction)]
        # return jsonify({"image": img_url, "prediction": predicted_class})

        # # 이미지 저장 폴더 생성 및 파일 저장
        # save_path = './images/' + file_name
        # if os.path.isdir(save_path):
        #     shutil.rmtree(save_path)

        # os.makedirs(save_path)
        # save_file = "images/" + file_name + "/" + file_name + ".jpg"
        # img.save(save_file)


if __name__ == '__main__':
    # SKIN_PORT = 5002

    # app.run(host="0.0.0.0", port=os.environ["SKIN_PORT"])
    app.run(host="0.0.0.0", port=5002)

# if __name__ == '__main__':
    # parser = argparse.ArgumentParser(
    #     description="Flask app exposing yolov5 + x-ray models")
    # parser.add_argument("--port", default=5002, type=int, help="port number")
    # args = parser.parse_args()
    # print(args)
    # debug=True causes Restarting with stat
    # app.run(host="0.0.0.0", port=args.port)
