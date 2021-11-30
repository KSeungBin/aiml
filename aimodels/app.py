# flask API 역할을 하는 파일
from flask import Flask, render_template, request
import pickle
import numpy as np

# Flask(__name__)를 호출하여 플라스크 앱 초기화
app = Flask(__name__)
# pickle 모델 로드
model = pickle.load(open('iris_model_lr.pkl', 'rb'))

# 플라스크 앱의 루트 디렉토리를 초기화하고 
# 그 안에이 루트 디렉토리에서 자신을 호출 할 함수를 정의
@app.route('/')
def index():
    return render_template('home.html')

# request.form ['']을 사용하여 프런트 엔드 HTML 페이지에서 
# 데이터를 가져오고 출력을 예측 한 다음 다시 보내는 홈 함수를 정의
@app.route('/predict', methods=['POST'])
def prediction():
    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    data4 = request.form['d']
    arr = np.array([[data1, data2, data3, data4]])  # 값을 예측할 때에는 2차원으로 넣어줘야 하므로 array 형태로 변환
    pred = model.predict(arr)
    return render_template('after.html', data=pred) # 모델의 예측값을 after.html로 rendering하고 -> 웹 브라우저에서 after.html이 실행됨


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="5000", debug=True) # root(127.0.0.1)에서 실행됨