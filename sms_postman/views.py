import json

import requests
# from flask_wtf.csrf import generate_csrf

from flask import (Flask, render_template, request, jsonify, flash)
from .apps import (app_sms, csrf)
from dotenv_ import (API_KEY, API_URL, PHONE_SEND)
from flask_wtf.csrf import CSRFError

from .forms.form_message import GetFormSmsMessage


@app_sms.errorhandler(CSRFError)
def handle_csrf_error(e):
    return render_template('csrf_error.html', reason=e.description), 400

@app_sms.route('/', methods=['GET', 'POST'])
@csrf.exempt
def index():
    form = GetFormSmsMessage()
    # csrf_token = csrf # generate_csrf()
    if request.method == 'POST' and form.validate_on_submit():
        # EXOLVE_API_KEY = generate_csrf()
        number = request.form.get('number')
        text = request.form.get('text')
        # api_key = request.form.get('api_key') or os.getenv('EXOLVE_API_KEY')  # Получение ключа из окружения или формы
        # api_key = EXOLVE_API_KEY

        if not number or not text:
            flash('Пожалуйста, заполните все поля.')
            return render_template('index.html')

        response = send_sms("", number, text)
        if response.status_code == 200:
            flash('SMS успешно отправлено!')
        else:
            flash(f'Ошибка при отправке SMS: {response.json().get("message", "Неизвестная ошибка")}')
    
    return render_template('index.html', form=form )

def send_sms(api_key, number, text):
    headers = {'Authorization': f'Bearer {api_key}'}
    data = {
        "number": PHONE_SEND,  # Замените на ваш номер отправителя
        "destination": number,
        "text": text
    }
    return requests.post(API_URL, json=data, headers=headers)


# # def sms_routing():
# @app_sms.route('/', methods=["GET"])
# def index():
#     return render_template('index.html')
#
# @app_sms.route("/csrf_token", methods=["GET"])
# def get_csrf_token():
#     pass
#     """
#     This CSRF-key returning by 'GET' request/
#     :return: JSON '{"csrf_token": < csrf_key >}'
#     """
#     csrf_ = generate_csrf()
#
#     return jsonify({"csrf_token": csrf_}), 200
#
# @app_sms.route("/send_sms", methods=["POST"])
# @csrf.exempt
# def send_sms():
#     number = request.form['number']
#     text = request.form['text']
#     api_key = request.form.get('api_key') or os.getenv(
#         'EXOLVE_API_KEY'
#         )  # Получение ключа из окружения или формы
#     sms_data = {
#         "number": "ваш_номер_отправителя",  # Замените на номер отправителя
#         "destination": number,
#         "text": text
#     }
#
#     headers = {'Authorization': f'Bearer {API_KEY}'}
#
#     response = requests.post(url=API_URL, json=sms_data, headers=headers)
#
#     if response.status_code == 200:
#         return jsonify(
#             {"status": "success", "message": "SMS отправлено успешно!"}
#         ), 200
#     else:
#         return jsonify(
#             {"status": "error", "message": "Ошибка при отправке SMS."}
#         ), response.status_code
#     # return app_sms