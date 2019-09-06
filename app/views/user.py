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

    # if User.select().where(phone=user.phone.data):
    #     return
    #
    # result = User.insert(username=user.username.data, password=user.password.data).execute()
    logger.debug("add user successful. DB result is {}".format(0))
    return JsonResult()


@user_service.route("/<userid>", methods=["put"])
def update_user():
    pass

@user_service.route("/<userid>", methods=["get"])
def query_user():
    pass