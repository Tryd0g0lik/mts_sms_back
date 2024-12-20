"""Routers"""
import requests
from flask import (render_template, request, redirect, flash, url_for)
from .apps import (app_sms, csrf)
from dotenv_ import (API_KEY, PHONE_SEND, API_URL)
from flask_wtf.csrf import CSRFError

from sms_postman.files import receive_pathname_js_file
from sms_postman.forms.form_message import GetFormSmsMessage


@app_sms.errorhandler(CSRFError)
def handle_csrf_error(e):
    return render_template('csrf_error.html', reason=e.description), 400

@app_sms.route('/', methods=['GET', 'POST'])
@csrf.exempt
def index():
    form = GetFormSmsMessage()
    js_file_name = receive_pathname_js_file()

    def _validate_contains_only_letters_and_digits(text):
        """Checking symbols from message"""
        excluded_chars = " *?!'^+%&/()=}][{$#@!~`"  # Список недопустимых символов
        for char in text:
            if char in excluded_chars:
                flash(f"Символ '{char}' не разрешен.")
                return False
        return True
   

    if request.method == 'POST' and form.validate_on_submit():
        number = request.form.get('mobil_number')
        text = request.form.get('text_message')
        
        if not number or not text:
            flash('Пожалуйста, заполните все поля.')
            return render_template('index.html',
                                   js_file_name=js_file_name,
                                   form=form
                                   )
        if not _validate_contains_only_letters_and_digits(text):
            flash(f"Проверьте текст.")
            return render_template(
                'index.html',
                js_file_name=js_file_name,
                form=form
                )
        
        response = send_sms(API_KEY, number, text)
        if response.status_code == 200:
            flash('SMS успешно отправлено!')
            return redirect(url_for("index",
                                    js_file_name=js_file_name,
                                    form=form
                                    ))
        else:
            flash(f'Ошибка при отправке SMS: \
{response.json().get("message", "Неизвестная ошибка")}')
    
    return render_template('index.html',
                           js_file_name=js_file_name,
                           form=form )

def send_sms(api_key, number, text):
    """
    SMS sending to the (only) mobile telephone from Russia
    :param api_key: str. Look the '.env' file.
    :param number: str. Number ща recipient.
    :param text: str. Text of message. Min. 3 symbol. Max.35.
    :return: response received from a POST-request (sender of message).
    """
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
    # SEND
    response = requests.post(API_URL,
                         json=data,
                         headers=headers)
    if response.status_code != 200:
        print(f"Error: {response.status_code}, Response: {response.json()}")
    return response