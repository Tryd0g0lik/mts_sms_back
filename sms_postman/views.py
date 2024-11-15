import requests
from flask import (Flask, render_template, request, jsonify)
from .apps import (app_sms, csrf)
from dotenv_ import (API_KEY, API_URL, PHONE_SEND)


# def sms_routing():
@app_sms.route('/', methods=["GET"])
def index():
    return render_template('index.html')


@app_sms.route("/send_sms", methods=["POST"])
@csrf.exempt
def send_sms():
    number = request.form['number']
    text = request.form['text']
    
    sms_data = {
        "number": "ваш_номер_отправителя",  # Замените на номер отправителя
        "destination": number,
        "text": text
    }
    
    headers = {'Authorization': f'Bearer {API_KEY}'}
    
    response = requests.post(url=API_URL, json=sms_data, headers=headers)
    
    if response.status_code == 200:
        return jsonify(
            {"status": "success", "message": "SMS отправлено успешно!"}
        ), 200
    else:
        return jsonify(
            {"status": "error", "message": "Ошибка при отправке SMS."}
        ), response.status_code
    # return app_sms