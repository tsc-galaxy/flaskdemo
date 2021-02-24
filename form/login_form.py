# config=utf-8
from flask_wtf import FlaskForm as Form
from wtforms import StringField, PasswordField,SubmitField
from wtforms.validators import DataRequired


class LoginForm(Form):
    accountNumber = StringField(label='用户名', validators=[DataRequired('accountNumber is null')])
    password = PasswordField(label='密码', validators=[DataRequired('password is null')])
    submit = SubmitField(label='注册')