# 플라스크 rest-api 생성
from flask import Flask, request
from flask_cors import CORS
# 서버 띄우고 접속 허용
app = Flask(__name__)
# 보안관련
CORS(app)


@app.route("/predict", methods=["GET", "POST"])
# @app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        message = {
            "postman": "post요청을 불러왔습니다."
        }
        return message
    if request.method == "GET":
        message = {
            "postman": "get요청을 불러왔습니다."
        }
        return message


# @app.route("/predict2", methods=["GET", "POST"])
# def predict2():
#     if request.method == "POST":
#         message = {
#             "name": "post요청 2"
#         }
#         return message


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=50)  # debug=True causes Restarting with stat
