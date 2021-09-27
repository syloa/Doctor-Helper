import os
import shutil
import tempfile
import matplotlib.pyplot as plt
import PIL
import torchvision.transforms as transforms
import cv2
import torch
import numpy as np
import zipfile
import glob
from sklearn.metrics import classification_report

from monai.apps import download_and_extract
from monai.config import print_config
from monai.data import decollate_batch
from monai.metrics import ROCAUCMetric
from monai.networks.nets import DenseNet121
from monai.transforms import (
    Activations,
    AddChannel,
    AsDiscrete,
    Compose,
    LoadImage,
    RandFlip,
    RandRotate,
    RandZoom,
    ScaleIntensity,
    EnsureType,
)
from monai.utils import set_determinism
from models.segmentation import seg

class_names = ['Affected', 'Healthy']
num_class = len(class_names)

# 모델 만든 후
device = torch.device("cpu")
model_classification = DenseNet121(spatial_dims=2, in_channels=1,
                                   out_channels=num_class).to(device)

loss_function = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model_classification.parameters(), 1e-5)
max_epochs = 10
val_interval = 1
auc_metric = ROCAUCMetric()

# 파라미터 불러오기
model_classification.load_state_dict(torch.load(
    "./models/best_metric_model3.pth", map_location=device))

# 데이터 불러오기 위한 Class


class Dataset(torch.utils.data.Dataset):
    def __init__(self, image_files, labels, transforms):
        self.image_files = image_files
        self.labels = labels
        self.transforms = transforms

    def __len__(self):
        return len(self.image_files)

    def __getitem__(self, index):
        return self.transforms(self.image_files[index]), self.labels[index]

# i는 ALL 폴더 내의 i번째 이미지를 의미
# 폴더를 여러 개 생성하기, 폴더 하나에 이미지 하나


def tumor_detect(path):
    val_x = []
    val_y = []
    prediction = []
    for images in sorted(os.listdir(path), key=len):
        test_image = os.path.join(path, images)
        val_x.append(test_image)
        val_y.append(0)

    val_transforms = Compose(
        [LoadImage(image_only=True), AddChannel(), ScaleIntensity(), EnsureType()])

    val_ds = Dataset(val_x, val_y, val_transforms)

    val_loader = torch.utils.data.DataLoader(
        val_ds, batch_size=1, num_workers=0)

    model_classification.eval()
    with torch.no_grad():
        for test_data in val_loader:
            test_images, test_labels = (
                test_data[0].to(device),
                test_data[1].to(device),
            )
            pred = model_classification(test_images).argmax(dim=1)
            pred = pred.item()
            prediction.append(pred)

    if prediction[0] == 0:
        diagnosis = "뇌종양입니다."
        img_saved = seg(path)
        return img_saved, diagnosis
    elif prediction[0] == 1:
        diagnosis = "이상 소견 없음"
        img_saved = None
        return img_saved, diagnosis
