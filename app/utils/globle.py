#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/3 17:32
# @Author  : haifeng.hu

from collections import namedtuple
from flask import jsonify
from enum import Enum

Result = namedtuple("result", ["code", "message"])


class Status(Enum):
    SUCCESS = "0000"
    FAILED = "1000"
    VALIDATE_FAILED = "2000"
    EXISTED = "3000"


def JsonResult(code=Status.SUCCESS.value, message="success"):
    if type(code) == Status:
        code = code.value

    return jsonify(Result(code, message)._asdict())
