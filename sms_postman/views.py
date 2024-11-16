import json

import requests
# from flask_wtf.csrf import generate_csrf

from flask import (Flask, render_template, request, jsonify, flash)
from .apps import (app_sms, csrf)
from dotenv_ import (API_KEY, PHONE_SEND)
from flask_wtf.csrf import CSRFError

from .files import receive_pathname_js_file
from .forms.form_message import GetFormSmsMessage


@app_sms.errorhandler(CSRFError)
def handle_csrf_error(e):
    return render_template('csrf_error.html', reason=e.description), 400

@app_sms.route('/', methods=['GET', 'POST'])
@csrf.exempt
def index():
    form = GetFormSmsMessage()
    # Below, receive the JS file name.
    js_file_name = receive_pathname_js_file
    # csrf_token = csrf # generate_csrf()


    if request.method == 'POST' and form.validate_on_submit():
        # EXOLVE_API_KEY = generate_csrf()
        number = request.form.get('mobil_number')
        text = request.form.get('text_message')
        # api_key = request.form.get('api_key') or os.getenv('EXOLVE_API_KEY')  # Получение ключа из окружения или формы
        # api_key = EXOLVE_API_KEY

        if not number or not text:
            flash('Пожалуйста, заполните все поля.')
            return render_template('index.html',
                                   )

        response = send_sms(API_KEY, number, text)
        if response.status_code == 200:
            flash('SMS успешно отправлено!')
            
        else:
            flash(f'Ошибка при отправке SMS: \
{response.json().get("message", "Неизвестная ошибка")}')
    
    return render_template('index.html',
                           js_file_name=js_file_name,
                           form=form )

def send_sms(api_key, number, text):
    headers = {'Authorization': f'Bearer {api_key}'}
    mobile_number = number.strip()
    # CLEAN
    if number[0] in "+":
        mobile_number = "".join(["7", (number.strip())[1:]])
    if int(number[0]) == 8:
        mobile_number = "".join(["7", (number.strip())[1:]])
    if int(mobile_number[0]) != 7:
        mobile_number = "7" + mobile_number
    # CHECK
    if not (mobile_number.startswith("79") and len(mobile_number) >= 11):
        raise ValueError(
            "Invalid phone number format. Must start with '79' \
            and contain at least 11 digits."
            )
    data = {
            "number": PHONE_SEND,
            "destination": mobile_number,
            "text": text
        }
    response =  requests.post("https://api.exolve.ru/messaging/v1/SendSMS",
                         json=data,
                         headers=headers)
    if response.status_code != 200:
        print(f"Error: {response.status_code}, Response: {response.json()}")
    return response