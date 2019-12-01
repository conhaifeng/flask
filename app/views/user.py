#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 20:10
# @Author  : haifeng.hu

import logging

from flask import current_app as app, request, session, jsonify
from flask.blueprints import Blueprint
from flask_login import login_required
from app.forms import UserForm
from app.models import User
from app.utils.globle import *

user_service = Blueprint("user", __name__)

logger = logging.getLogger("sample2")


@user_service.route("/register", methods=["post"])
def add_user():
    user = UserForm()

    if not user.validate_on_submit():
        error_msg = "{}:{}".format(*user.error)
        logger.debug(error_msg)
        return JsonResult(Status.VALIDATE_FAILED.value, error_msg)

    result = User.select().where(User.phone == user.phone.data)
    if User.select().where(User.phone == user.phone.data).exists():
        logger.info("Phone exsited. Add failed.")
        return JsonResult(Status.EXISTED.value, "User exsited.")

    result = User.insert(username=user.username.data, password=user.password.data, phone=user.phone.data).execute()
    logger.info("add user successful. DB result is {}".format(result))
    return JsonResult()


@user_service.route("/<userid>", methods=["put"])
@login_required
def update_user(userid):
    return "update_user."


@user_service.route("/<userid>", methods=["get"])
@login_required
def query_user(userid):
    return JsonResult()
