# Doctor-Helper

해당 프로젝트는 실용 중심의 인공지능 개발자 양성과정에서 진행한 최종 실무프로젝트입니다. AI를 통한 의료 영상 이미지의 진단을 통해 의사의 업무를 보조하는 모바일 웹 서비스입니다.


---

## 프로젝트 설명
1. 3개의 Flask API를 이용해 질병을 진단합니다. Frontend에서 전달된 요청에 따라 MongoDB에 저장되어있는 이미지를 통해 진단하고, 진단된 결과를 출력하고, DB에 저장합니다.
- 흉부 질병 진단
    - Yolo.v5s
- 피부암 진단
    - Densenet121
- 뇌종양 여부 진단
    - Monai
2. 부가기능
- 앱의 기본 색상을 변경할 수 있습니다.
- 북마크한 의료 영상 이미지를 북마크 페이지에서 볼 수 있습니다.
- 영어, 일본어, 에스페란토어를 지원합니다.

## 시연영상
https://youtu.be/ug6kUtfy7-o


## 프로젝트 구조
```bash
Client
Server
DB
```
1. Client: 프레임워크 Quasar를 프론트 화면 구성
2. Server: RestAPI로 구성된 백엔드
3. NoSQL DB에 JSON 형태의 데이터 저장

## Skillset

- Javascript
- Vue.js
- Quesar
- Node.js
- feathersJS

- Python3.8
- Flask

- MongoDB
- Postman
- Git


## Dataset
1. Chest X-ray <br>
a large collection of Chest x-ray iamges is from NIH Clinical Center
Download: https://nihcc.app.box.com/v/ChestXray-NIHCC
Paper: Xiaosong Wang, Yifan Peng, Le Lu, Zhiyong Lu, Mohammadhadi Bagheri, Ronald Summers, ChestX-ray8: Hospital-scale Chest X-ray Database and Benchmarks on Weakly-Supervised Classification and Localization of Common Thorax Diseases, IEEE CVPR, pp. 3462-3471, 2017
2. Brain CT <br>
https://www.kaggle.com/navoneel/brain-mri-images-for-brain-tumor-detection
https://www.kaggle.com/ahmedhamada0/brain-tumor-detection
3. Skin Cancer MNIST: HAM10000 <br>
https://www.kaggle.com/kmader/skin-cancer-mnist-ham10000
