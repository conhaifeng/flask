#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 20:10
# @Author  : haifeng.hu

import logging

from flask import current_app as app, request, session, jsonify
from flask.blueprints import Blueprint
from app.forms import UserForm
from app.models import User
from app.utils.globle import Result

user_service = Blueprint("user", __name__)

logger = logging.getLogger("werkzeug")

@user_service.route("/register", methods=["post"])
def add_user():
    user = UserForm()

    if not user.validate_on_submit():
        logger.debug("username or password is illegal.")
        return jsonify(Result(code="2000", message="username or password illegal."))

    result = User.insert(username=user.username.data, password=user.password.data).execute()
    logger.debug("add user successful.")
    return jsonify(Result(code="0000", message="success"))


@user_service.route("/<userid>", methods=["put"])
def update_user():
    pass

@user_service.route("/<userid>", methods=["get"])
def query_user():
    pass