#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 20:11
# @Author  : haifeng.hu

import logging

from flask import jsonify, current_app as app
from flask.blueprints import Blueprint
# from flask_login import login_required
from flask_login import login_required, login_user, logout_user
from app.forms import LoginForm
from app.utils.globle import *
from app.models import User

logger = logging.getLogger("sample1")
auth_service = Blueprint("auth", __name__)

@auth_service.route("/login", methods=["post"])
def login():
    login_form = LoginForm()

    if not login_form.validate_on_submit():
        error_msg = "Login failed. {}:{}".format(*login_form.error)
        logger.info(error_msg)
        return JsonResult(Status.FAILED.value, error_msg)

    user = User.get_or_none(User.username == login_form.username.data, User.password == login_form.password.data)
    if user is None:
        return JsonResult(Status.FAILED, "Login failed, username or password was error.")

    login_user(user)
    logger.info("Login success. username={}, password={}".format(login_form.username.data, login_form.password.data))
    return JsonResult()

@auth_service.route("/logout", methods=["get"])
@login_required
def logout():
    logout_user()
    return JsonResult()

def unauthrized():
    return JsonResult(Status.FAILED, "Unauthrized.")


