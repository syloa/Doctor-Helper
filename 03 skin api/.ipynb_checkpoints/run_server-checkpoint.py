from flask_cors import CORS, cross_origin
from flask import Flask, render_template, request, redirect
from PIL import Image
import os
import shutil
import io
from numpy import random
import torch.backends.cudnn as cudnn
import torch
import cv2
from pathlib import Path
import time
import argparse
from flask import Flask, jsonify
from torchvision import models
from torch._C import device
import os
import cv2
import itertools
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import pandas as pd
from tqdm import tqdm
from glob import glob
from PIL import Image
# pytorch libraries
import torch
from torch import optim, nn
from torch.autograd import Variable
from torch.utils.data import DataLoader, Dataset
from torchvision import models, transforms
import argparse

# # sklearn libraries
# from sklearn.metrics import confusion_matrix
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import classification_report

# to make the results are reproducible
np.random.seed(10)
torch.manual_seed(10)
torch.cuda.manual_seed(10)

# from . import SkinModel
# export SKIN_MODEL_LOCATION = classifier_epoch_dict.pth


# 플라스크 rest-api 생성


app = Flask(__name__)
CORS(app)


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == "POST":
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

        prediction = model(img)
        predicted_class = SkinClasses[torch.argmax(prediction)]
        return jsonify({"image": img_url, "prediction": predicted_class})

        # 이미지 저장 폴더 생성 및 파일 저장
        save_path = './images/' + file_name
        if os.path.isdir(save_path):
            shutil.rmtree(save_path)

        os.makedirs(save_path)
        save_file = "images/" + file_name + "/" + file_name + ".jpg"
        img.save(save_file)


labels = ['비정형색소모반', '악성흑색종', '지루각화증', '기저세포암', '광선각화증', '혈관종', '피부섬유종']
diagnosis = ['비정형색소모반', '악성흑색종', '지루각화증', '기저세포암', '광선각화증', '혈관종',
             '피부섬유종']

data_dir = "../skinpractice/images/original"
all_image_path = glob(os.path.join(data_dir, '*', '*.jpg'))

mean = (0.49139968, 0.48215827, 0.44653124)
std = (0.24703233, 0.24348505, 0.26158768)

input_size = 224

val_transforms = transforms.Compose([transforms.Resize((input_size, input_size)),
                                     transforms.ToTensor(),
                                     transforms.Normalize(mean, std)])

transform = transforms.Compose([transforms.Resize((input_size, input_size)),
                                #                                      transforms.RandomHorizontalFlip(),
                                #                                      transforms.RandomVerticalFlip(),
                                #                                      transforms.RandomRotation(20),
                                #                                      transforms.ColorJitter(brightness=0.1, contrast=0.1, hue=0.1),
                                transforms.ToTensor(),
                                transforms.Normalize(mean, std)])


def set_para_req_grad(model, grad):
    if grad == True:
        for param in mode.parameters():
            param.requires_grad = False


def initialise_model(model_name, num_classes, grad, use_pretrained=True):
    '''
    grad = if the pretrained weights be updated
    use_pretrained = use pre trained weights or start from scratch
    '''
    model = None

    if model_name == 'densenet':
        model = models.densenet121(pretrained=use_pretrained)
        set_para_req_grad(model, grad)
        num_ftrs = model.classifier.in_features
        model.classifier = nn.Linear(num_ftrs, num_classes)
    return model


num_classes = 7
model_name = 'densenet'
grad = False
# initialise model to run
model = initialise_model(model_name, num_classes, grad, use_pretrained=True)
device = torch.device("cpu")
batch_size = 32
epochs = 10
lr = 1e-3
optimizer = optim.Adam(model.parameters(), lr=lr)
criterion = nn.CrossEntropyLoss().to(device)

PATH = "./classifier_epoch10_dict.pth"

model.load_state_dict(torch.load(PATH, map_location=device))

# 이미 학습된 가중치를 사용하기 위해 `pretrained` 에 `True` 값을 전달합니다:
# device = torch.device('cpu')
# PATH = "./runs/train/exp/weights/classifier_epoch10.pt"
# model = torch.load(PATH, map_location=device)
# model.to(device)
# 모델을 추론에만 사용할 것이므로, `eval` 모드로 변경합니다:
model.eval()


class Dataset(torch.utils.data.Dataset):
    def __init__(self, image_files, labels, transforms):
        self.image_files = image_files
        self.labels = labels
        self.transforms = transforms

    def __len__(self):
        return len(self.image_files)

    def __getitem__(self, index):
        #             X = Image.open(self.image_files[index]),
        #             y = torch.tensor(int(self.labels[index]))

        #             if self.transforms:
        #                 X = self.transforms(X)
        #             return X,y
        return self.transforms(self.image_files[index]), self.labels[index]


# 폴더를 여러 개 생성하기, 폴더 하나에 이미지 하나
def skin_pred(path):
    val_x = []
    val_y = []
    prediction = []
    for images in sorted(os.listdir(path), key=len):
        test_image = os.path.join(path, images)
        val_x.append(test_image)
        val_y.append(0)

    val_transforms = transforms.Compose([transforms.Resize((input_size, input_size)),
                                         transforms.ToTensor(),
                                         transforms.Normalize(mean, std)])

    val_ds = Dataset(val_x, val_y, val_transforms)

    return val_ds
    print(val_ds)
# #     val_ds = Dataset(df_val, transform=val_transform)

    val_loader = torch.utils.data.DataLoader(
        val_ds, batch_size=batch_size, shuffle=False, num_workers=0)

# #     img_original = Image.open('../skinpractice/images/original/1/1.jpg')
# #     img_done = transforms(img_original)
# #     img_done = img_done.unsqueeze(0)

    model.eval()
    with torch.no_grad():
        for test_data in val_loader:
            test_images, labels = (
                test_data[0].to(device),
                test_data[1].to(device),
                test_data[2].to(device),
                test_data[3].to(device),
                test_data[4].to(device),
                test_data[5].to(device),
                test_data[6].to(device),
            )
            pred = model(test_images).argmax(dim=1)
            pred = pred.item()
            prediction.append(pred)

    if prediction[0] == 0:
        diagnosis = "비정형색소모반입니다."
        img_saved = None
        return img_saved, diagnosis
    elif prediction[0] == 1:
        diagnosis = "악성흑색종입니다."
        img_saved = None
        return img_saved, diagnosis
    elif prediction[0] == 2:
        diagnosis = "지루각화증입니다."
        img_saved = None
        return img_saved, diagnosis
    elif prediction[0] == 3:
        diagnosis = "기저세포암입니다."
        img_saved = None
        return img_saved, diagnosis
    elif prediction[0] == 4:
        diagnosis = "광선각화증입니다."
        img_saved = None
        return img_saved, diagnosis
    elif prediction[0] == 5:
        diagnosis = "혈관종입니다."
        img_saved = None
        return img_saved, diagnosis
    elif prediction[0] == 1:
        diagnosis = "피부섬유종입니다."
        img_saved = None
        return img_saved, diagnosis


#     with torch.no_grad():
#         for i, data in enumerate(val_loader):
#             images, labels = data
#             n = images.size(0)
#             images = Variable(images).to(device)
#             labels = Variable(labels).to(device)

#             output = model(images)
#             pred = torch.argmax(output, dim=1)


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
