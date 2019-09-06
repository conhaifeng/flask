#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/10 20:28
# @Author  : haifeng.hu

import os
import logging
import logging.config

from peewee import SqliteDatabase
from flask import Flask

from logging.handlers import RotatingFileHandler
# db = SqliteDatabase("20190903")
db = ""

app = Flask(__name__)
app.config.from_object("config")
logging.config.fileConfig(os.path.join(app.config.get("BASE_PATH"), "config", "log.conf"))

from app.views.auth import auth
from app.views.user import user_service

app.register_blueprint(auth)
app.register_blueprint(user_service, url_prefix="/user")
