from flask import Flask, render_template, request
import requests
import json
from roboflow import Roboflow

# สร้างแอปพลิเคชัน Flask และระบุ template_folder
app = Flask(__name__, template_folder='template')

# ... โค้ดอื่น ๆ ...

@app.route('/', methods=['GET', 'POST'])
def index():
    count_cabbage = 0

    if request.method == 'POST':
        if 'file' in request.files:
            uploaded_file = request.files['file']
            if uploaded_file.filename != '':
                api_key = "hGegkoy8IkVOXti6XHB1"
                url = "https://detect.roboflow.com/cabbage-low/1?api_key=hGegkoy8IkVOXti6XHB1"
                files = {'file': ('image.jpg', uploaded_file.read())}
                headers = {'Authorization': f'Bearer {api_key}'}
                response = requests.post(url, headers=headers, files=files)
                data = response.json()
                predictions = data['predictions']

                for prediction in predictions:
                    if prediction['class'] == 'Cabbage':
                        count_cabbage += 1

    return render_template('index.html', count_cabbage=count_cabbage)

# นิยามฟังก์ชัน calculate_price() และเส้นทางสำหรับการคำนวณและแสดงผลลัพธ์
# ...
# นิยามฟังก์ชันที่มีอยู่แล้วสำหรับคำนวณราคา
def calculate_price():
    price_per_kg = float(request.form['price_per_kg'])
    num_cabbages = int(request.form['num_cabbages'])
    weight_per_cabbage = float(request.form['weight_per_cabbage'])

    total_weight = num_cabbages * weight_per_cabbage
    total_price = total_weight * price_per_kg

    return f"น้ำหนักทั้งหมด: {total_weight} กิโลกรัม\nราคาทั้งหมด: {total_price} บาท"

# เส้นทางสำหรับการคำนวณและแสดงผลลัพธ์
@app.route('/calculate', methods=['POST'])
def calculate():
    result = calculate_price()
    return result

# เส้นทางสำหรับแสดงฟอร์ม
@app.route('/', methods=['GET'])
def form():
    return render_template('index.html')
# รันแอปพลิเคชัน Flask
if __name__ == '__main__':
    app.run(debug=True)