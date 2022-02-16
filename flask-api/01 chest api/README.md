# rest api 형식 실행
```sh
python webapp.py --port 5000
```

# cli 형식으로 실행
```sh
python detect.py --weights 'runs/train/exp/weights/best.pt' --img 640 --conf 0.15 --iou 0.5 --source images --exist-ok
```