from flask_wtf import FlaskForm
from wtforms.fields import (
    StringField,
    PasswordField,
    SubmitField,
    BooleanField
)
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    employee_number = StringField('Employee Number', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
    
class OrderForm(FlaskForm):
    french_fries = BooleanField('French Fries')
    dr_pepper = BooleanField('Dr. Pepper')
    jambalaya = BooleanField('Jambalaya')