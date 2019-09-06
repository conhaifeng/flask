#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/3 11:26
# @Author  : haifeng.hu

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Length, Regexp
from threading import Lock

class LoginForm(FlaskForm):
    phone = StringField("phone", [InputRequired(), Regexp("^1([38]\d|5[0-35-9]|7[3678])\d{8}$")])
    password = PasswordField("password", [InputRequired()])

class UserForm(FlaskForm):
    username = StringField("username", [InputRequired(), Length(5, 20)])
    password = PasswordField("password", [InputRequired()])
