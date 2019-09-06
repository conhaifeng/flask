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
db = SqliteDatabase("20190903", pragmas={
    "journal_mode":"wal",
    "cache_size": -1 * 64000,
    "ignore_check_constraints":0,
    "synchronous":0
})

app = Flask(__name__)
app.config.from_object("config")
logging.config.fileConfig(os.path.join(app.config.get("BASE_PATH"), "config", "log.conf"))

from app.views.data import init_service
from app.views.auth import auth_service
from app.views.user import user_service

app.register_blueprint(init_service, url_prefix="/db")
app.register_blueprint(auth_service)
app.register_blueprint(user_service, url_prefix="/user")

@app.before_request
def _db_create():
    db.connection()

@app.teardown_request
def _db_close(exec):
    if not db.is_closed():
        db.close()
