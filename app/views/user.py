#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 20:10
# @Author  : haifeng.hu

import logging

from flask import current_app as app, request, session, jsonify
from flask.blueprints import Blueprint
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
        return JsonResult("2000", error_msg)

    users = User.select().where(User.phone==user.phone.data)

    if len(list(users)):
        logger.info("Phone exsited. Add failed.")
        return JsonResult("3000", "User exsited.")

    result = User.insert(username=user.username.data, password=user.password.data, phone=user.phone.data).execute()
    logger.info("add user successful. DB result is {}".format(result))
    return JsonResult()


@user_service.route("/<userid>", methods=["put"])
def update_user():
    pass

@user_service.route("/<userid>", methods=["get"])
def query_user():
    pass