#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/3 17:32
# @Author  : haifeng.hu

from collections import namedtuple
from flask import jsonify

Result = namedtuple("result", ["code", "message"])

def JsonResult(code="0000", message="success"):
    return jsonify(Result(code, message)._asdict())