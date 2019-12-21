#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/18 19:21
# @Author  : haifeng.hu

from flask.blueprints import Blueprint

ok_service = Blueprint("ok", __name__)

@ok_service.route("/ok")
def ok():
    return "ok"

@ok_service.route("/ok5")
def ok():
    return "ok4"