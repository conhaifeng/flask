#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 20:11
# @Author  : haifeng.hu

import logging

from flask import jsonify, current_app as app
from flask.blueprints import Blueprint
from flask_login import login_required
from app.forms import LoginForm
from app.utils.globle import Result

logger = logging.getLogger("sample1")
auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["post"])
def login():
    login_form = LoginForm()

    if not login_form.validate_on_submit():
        logger.info("Login failed. username={}, password={}".format(login_form.phone.data, login_form.password.data))
        return jsonify(Result(code="00001000", message="failed")._asdict())

    logger.info("Login success. username={}, password={}".format(login_form.phone.data, login_form.password.data))
    return jsonify(Result(code="000000", message="success")._asdict())


@auth.route("/logout", methods=["get"])
@login_required
def logout():
    pass


