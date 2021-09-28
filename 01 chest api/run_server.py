import argparse
import time
from pathlib import Path

import cv2
import torch
import torch.backends.cudnn as cudnn
from numpy import random

from models.experimental import attempt_load
from utils.datasets import LoadStreams, LoadImages
from utils.general import check_img_size, non_max_suppression, apply_classifier, scale_coords, xyxy2xywh, \
    strip_optimizer, set_logging, increment_path
from utils.plots import plot_one_box
from utils.torch_utils import select_device, load_classifier, time_synchronized

# 플라스크 rest-api 생성
import io
import shutil
import os
from PIL import Image
from flask import Flask, render_template, request, redirect
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app)


@app.route("/predict", methods=["GET", "POST"])
# @app.route("/predict", methods=["POST"])
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

        # 이미지 저장 폴더 생성 및 파일 저장
        save_path = './images/' + file_name
        if os.path.isdir(save_path):
            shutil.rmtree(save_path)

        os.makedirs(save_path)
        save_file = "images/" + file_name + "/" + file_name + ".jpg"
        img.save(save_file)

        # 예측에 사용되는 추가 변수
        args.file_name = file_name
        args.source = 'images/' + file_name
        args.img_size = 640
        args.conf_thres = 0.15
        args.iou_thres = 0.5
        args.device = ''
        args.view_img = False
        args.save_txt = False
        args.save_conf = False
        args.classes = None
        args.agnostic_nms = False
        args.augment = False
        args.update = False

        args.project = 'static'
        # args.project = 'runs/detect'

        args.exist_ok = True
        args.name = 'exp'
        args.weights = 'runs/train/exp/weights/best.pt'

        # print("args.update : ", args.update)
        with torch.no_grad():
            if args.update:  # update all models (to fix SourceChangeWarning)
                for args.weights in ['yolov5s.pt', 'yolov5m.pt', 'yolov5l.pt', 'yolov5x.pt']:
                    message = detect()
                    strip_optimizer(args.weights)
            else:
                message = detect()
# -------------------------------
        # results = model(img, size=640)

        # # for debugging
        # # data = results.pandas().xyxy[0].to_json(orient="records")
        # # return data

        # results.render()  # updates results.imgs with boxes and labels

        # redirect("runs/detect/exp/image0.jpg")
        # return redirect("static/exp/image0.jpg")

    # return render_template("index.html")
    return message
    # return {'status': 'success'}


def detect(save_img=False):
    source, weights, view_img, save_txt, imgsz, file_name = args.source, args.weights, args.view_img, args.save_txt, args.img_size, args.file_name
    webcam = source.isnumeric() or source.endswith('.txt') or source.lower().startswith(
        ('rtsp://', 'rtmp://', 'http://'))

    # Directories
    save_dir = Path(increment_path(Path(args.project) /
                    args.name, exist_ok=args.exist_ok))  # increment run
    # save_dir = Path(increment_path(Path(args.project) , exist_ok=args.exist_ok))  # increment run
    (save_dir / 'labels' if save_txt else save_dir).mkdir(parents=True,
                                                          exist_ok=True)  # make dir

    # Initialize
    set_logging()
    device = select_device(args.device)
    half = device.type != 'cpu'  # half precision only supported on CUDA

    # Load model
    model = attempt_load(weights, map_location=device)  # load FP32 model
    imgsz = check_img_size(imgsz, s=model.stride.max())  # check img_size
    if half:
        model.half()  # to FP16

    # Second-stage classifier
    classify = False
    if classify:
        modelc = load_classifier(name='resnet101', n=2)  # initialize
        modelc.load_state_dict(torch.load(
            'weights/resnet101.pt', map_location=device)['model']).to(device).eval()

    # Set Dataloader
    vid_path, vid_writer = None, None
    if webcam:
        view_img = True
        cudnn.benchmark = True  # set True to speed up constant image size inference
        dataset = LoadStreams(source, img_size=imgsz)
    else:
        save_img = True
        dataset = LoadImages(source, img_size=imgsz)
        print("dataset : ", dataset)

    # Get names and colors
    names = model.module.names if hasattr(model, 'module') else model.names

    # print("names === ", names)

    colors = [[random.randint(0, 255) for _ in range(3)] for _ in names]

    # Run inference
    t0 = time.time()
    img = torch.zeros((1, 3, imgsz, imgsz), device=device)  # init img
    # run once
    _ = model(img.half() if half else img) if device.type != 'cpu' else None
    for path, img, im0s, vid_cap in dataset:
        img = torch.from_numpy(img).to(device)
        img = img.half() if half else img.float()  # uint8 to fp16/32
        img /= 255.0  # 0 - 255 to 0.0 - 1.0
        if img.ndimension() == 3:
            img = img.unsqueeze(0)

        # Inference
        t1 = time_synchronized()
        pred = model(img, augment=args.augment)[0]

        # Apply NMS
        pred = non_max_suppression(
            pred, args.conf_thres, args.iou_thres, classes=args.classes, agnostic=args.agnostic_nms)
        t2 = time_synchronized()

        # Apply Classifier
        if classify:
            pred = apply_classifier(pred, modelc, img, im0s)

        # Process detections
        for i, det in enumerate(pred):  # detections per image
            if webcam:  # batch_size >= 1
                p, s, im0, frame = path[i], '%g: ' % i, im0s[i].copy(
                ), dataset.count
            else:
                p, s, im0, frame = path, '', im0s, getattr(dataset, 'frame', 0)

            p = Path(p)  # to Path
            save_path = str(save_dir / p.name)  # img.jpg
            txt_path = str(save_dir / 'labels' / p.stem) + \
                ('' if dataset.mode == 'image' else f'_{frame}')  # img.txt
            s += '%gx%g ' % img.shape[2:]  # print string
            # normalization gain whwh
            gn = torch.tensor(im0.shape)[[1, 0, 1, 0]]
            if len(det):
                # Rescale boxes from img_size to im0 size
                det[:, :4] = scale_coords(
                    img.shape[2:], det[:, :4], im0.shape).round()

                # Print results
                for c in det[:, -1].unique():
                    n = (det[:, -1] == c).sum()  # detections per class
                    s += f'{n} {names[int(c)]}s, '  # add to string

                # Write results
                for *xyxy, conf, cls in reversed(det):
                    if save_txt:  # Write to file
                        xywh = (xyxy2xywh(torch.tensor(xyxy).view(1, 4)
                                          ) / gn).view(-1).tolist()  # normalized xywh
                        # label format
                        line = (
                            cls, *xywh, conf) if args.save_conf else (cls, *xywh)
                        with open(txt_path + '.txt', 'a') as f:
                            f.write(('%g ' * len(line)).rstrip() % line + '\n')

                    if save_img or view_img:  # Add bbox to image
                        # print("name : ==== ", names)
                        # print("int(cls) : ==== ", int(cls))
                        diagnosis = ['대동맥확장', '무기폐', '석회화', '심장비대', '폐경결', '간질성폐질환',
                                     '침윤', '폐불투명도', '결절/덩어리', '기타병변', '흉막삼출', '흉막비후', '기흉', '폐섬유증']
                        diagnosis_label = f'{diagnosis[int(cls)]} {conf:.2f}'
                        # label = f'{diagnosis[int(cls)]} {conf:.2f}'
                        label = f'{names[int(cls)]} {conf:.2f}'
                        # opa = conf
                        # diagnosis = names[int(cls)]
                        plot_one_box(xyxy, im0, label=label,
                                     color=colors[int(cls)], line_thickness=1)

            # Print time (inference + NMS)
            print(f'{s}Done. ({t2 - t1:.3f}s)')

            # Stream results
            if view_img:
                cv2.imshow(str(p), im0)
                if cv2.waitKey(1) == ord('q'):  # q to quit
                    raise StopIteration

            # Save results (image with detections)
            if save_img:
                if dataset.mode == 'image':
                    cv2.imwrite(save_path, im0)
                else:  # 'video'
                    if vid_path != save_path:  # new video
                        vid_path = save_path
                        if isinstance(vid_writer, cv2.VideoWriter):
                            vid_writer.release()  # release previous video writer

                        fourcc = 'mp4v'  # output video codec
                        fps = vid_cap.get(cv2.CAP_PROP_FPS)
                        w = int(vid_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                        h = int(vid_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                        vid_writer = cv2.VideoWriter(
                            save_path, cv2.VideoWriter_fourcc(*fourcc), fps, (w, h))
                    vid_writer.write(im0)

    if save_txt or save_img:
        s = f"\n{len(list(save_dir.glob('labels/*.txt')))} labels saved to {save_dir / 'labels'}" if save_txt else ''
        print(f"Results saved to {save_dir}{s}")

    print(f'Done. ({time.time() - t0:.3f}s)')
    # print("label : ", label)

    if label:
        diagnosis = {
            "name": diagnosis_label.split(' ')[0],
            "rate": diagnosis_label.split(' ')[1],
            'img_url': "http://localhost:5000/static/exp/"+file_name+".jpg"
        }
    else:
        diagnosis = {
            "name": "진단없음",
            "rate": "0"
        }

    return diagnosis


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Flask app exposing yolov5 + x-ray models")
    parser.add_argument("--port", default=5000, type=int, help="port number")
    args = parser.parse_args()
    print(args)
    # debug=True causes Restarting with stat
    app.run(host="0.0.0.0", port=args.port)
