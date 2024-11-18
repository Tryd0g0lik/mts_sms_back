"""
Form for the sms messages.
"""
from cfgv import ValidationError
from flask_wtf import FlaskForm
from wtforms import (TelField, StringField, SubmitField, validators as val)



class GetFormSmsMessage(FlaskForm):
    """There is a flask-form for a SMS sending """
    mobil_number = TelField(
        "Номер телефона",
        default="+79...",
        
        validators=[
            val.InputRequired(),
            val.Length(
                min=10,
                message="Min количество символов мобильного номера 10 символов"
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

