"""
FOrm for the sms message.
"""
from flask_wtf import FlaskForm
from wtforms import (TelField, StringField, SubmitField, validators as val)


class GetFormSmsMessage(FlaskForm):
    """There is a flask-form for a SMS sending """
    mobil_number = TelField(
        "Номер телефона",
        default="99999999",
        validators=[
            val.InputRequired(),
            val.Length(
                min=8,
                message="Min количество символов мобильного номера 8 символов"
            )
        ]
    )
    
    text_message = StringField(
        "SMS",
        validators=[
            val.InputRequired(),
            val.Length(
                min=3,
                max=35,
                message="Min. (Количество символов) 3. \
Max. (Количество символов) 35"
            )
        ]
    )
    submit = SubmitField(
        "Отправить",
        render_kw={"class": "btn btn-secondary"}
    )