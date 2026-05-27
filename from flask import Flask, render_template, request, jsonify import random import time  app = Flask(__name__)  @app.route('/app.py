from flask import Flask, render_template, request, jsonify
import random
import time

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    # 模拟模型预测耗时
    time.sleep(1)

    # 随机生成 0-21 月生存时间
    survival_time = round(random.uniform(0, 21), 1)

    return jsonify({
        'predicted_survival_months': survival_time
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
