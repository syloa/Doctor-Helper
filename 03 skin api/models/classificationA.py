# %matplotlib inline
# python libraties
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
from models.segA import seg

# sklearn libraries
# from sklearn.metrics import confusion_matrix
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import classification_report

# to make the results are reproducible
np.random.seed(10)
torch.manual_seed(10)
torch.cuda.manual_seed(10)


def set_para_req_grad(model, grad):
    if grad == True:
        for param in model.parameters():
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


labels = ['sd1', 'sd2', 'sd3', 'sd4', 'sd5', 'sd6', 'sd7']
num_classes = 7
model_name = 'densenet'
grad = False
# initialise model to run
model = initialise_model(model_name, num_classes, grad, use_pretrained=True)
device = torch.device("cpu")
model = model.to(device)
batch_size = 32
epochs = 10
lr = 1e-3
optimizer = optim.Adam(model.parameters(), lr=lr)
criterion = nn.CrossEntropyLoss().to(device)
input_size = 224
mean = (0.49139968, 0.48215827, 0.44653124)
std = (0.24703233, 0.24348505, 0.26158768)


# dataloader or dataset
class HAM10000(torch.utils.data.Dataset):
    def __init__(self, image_files, labels, transforms):
        self.image_files = image_files
        self.labels = labels
        self.transforms = transforms

    def __len__(self):
        return(len(self.image_files))

    def __getitem__(self, index):
        return self.transforms(Image.open(self.image_files[index])), self.labels[index]


PATH = "./models/classifier_epoch10_dict.pth"

model.load_state_dict(torch.load(PATH, map_location=device))
model.eval()


def validate(path):
    val_x = []
    val_y = []
    prediction = []

    transform = transforms.Compose([transforms.Resize((input_size, input_size)), transforms.ToTensor(),
                                    transforms.Normalize(mean, std)])

    ds = HAM10000(val_x, val_y, transform)

    dl = DataLoader(ds, batch_size=batch_size, shuffle=False, num_workers=0)

    for images in sorted(os.listdir(path), key=len):
        test_image = os.path.join(path, images)
        val_x.append(test_image)
        val_y.append(0)

    model.eval()

#     val_loss = AverageMeter()
#     val_acc = AverageMeter()

    with torch.no_grad():
        for i, data in enumerate(dl):
            images, labels = data
            n = images.size(0)
            images = Variable(images).to(device)
            labels = Variable(labels).to(device)

            output = model(images)
    #             pred = torch.argmax(output, dim=1)
            pred = torch.argmax(output)

            pred = pred.item()

            prediction.append(pred)
    #             val_acc.update(pred.eq(labels).sum().item()/n)
    #             val_loss.update(criterion(output, labels).item())

    if prediction[i] == 0:
        diagnosis = "sd1"
        img_saved = seg(path)
        return img_saved, diagnosis
    elif prediction[i] == 1:
        diagnosis = "sd2"
        img_saved = seg(path)
        return img_saved, diagnosis
    elif prediction[i] == 2:
        diagnosis = "sd2"
        img_saved = seg(path)
        return img_saved, diagnosis
    elif prediction[i] == 3:
        diagnosis = "sd3"
        img_saved = seg(path)
        return img_saved, diagnosis
    elif prediction[i] == 4:
        diagnosis = "sd4"
        img_saved = seg(path)
        return img_saved, diagnosis
    elif prediction[i] == 5:
        diagnosis = "sd5"
        img_saved = seg(path)
        return img_saved, diagnosis
    elif prediction[i] == 6:
        diagnosis = "sd6"
        img_saved = seg(path)

    return img_saved, diagnosis
    print('-----------------------------------------')
#         print(labels[prediction])
    # print(prediction)
    # print(labels[prediction])
#         print(f'[epoch {epoch}] [iter{i/len(val_dl)}] [val loss {val_loss.avg:.5f}] [val_acc {val_acc.avg:.5f}]')
    print('-----------------------------------------')

#         return val_loss.avg, val_acc.avg
