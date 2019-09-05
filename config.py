#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/3 10:57
# @Author  : haifeng.hu

import os

# WTF_CSRF_SECRET_KEY = False -- 如果有SECRET_KEY，则默认使用SECRET_KEY
SECRET_KEY = "1234567890abcd"
WTF_CSRF_ENABLED  = False
BASE_PATH = os.path.dirname(os.path.realpath(__file__))