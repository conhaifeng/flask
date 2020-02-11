#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/3 11:26
# @Author  : haifeng.hu

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Length, Regexp
from threading import Lock

class BaseForm(FlaskForm):

    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)

    @property
    def error(self):
        """
        Get signle error from errors dict.
        :return: single error.
        """
        if self.errors is None or len(self.errors) == 0:
            return (None, None)

        error_field, error_msg = self.errors.popitem()
        error_msg = error_msg[0]

        return (error_field, error_msg)

class LoginForm(BaseForm):
    # phone = StringField("phone", [InputRequired(), Regexp("^1([38]\d|5[0-35-9]|7[3678])\d{8}$")])
    username = StringField("username", [InputRequired()])
    password = PasswordField("password", [InputRequired()])

class UserForm(BaseForm):
    username = StringField("username", [InputRequired(), Length(5, 20)])
    phone = StringField("phone", [InputRequired(), Regexp("^1([38]\d|5[0-35-9]|7[3678])\d{8}$")])
    password = PasswordField("password", [InputRequired()])
