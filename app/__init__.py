#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/10 20:28
# @Author  : haifeng.hu

import logging.config
import os

from flask import Flask
from flask_cors import CORS

from app.extensions import login_manager, db
from app.models import User
from app.utils.globle import JsonResult, Status
from app.initializer import init_db

app = Flask(__name__)
app.config.from_object("config")
# app.config.from_json("conf.json")
CORS(app, max_age=3600, origins=app.config.get("CORS_ORIGIN"), supports_credentials=True)
logging.config.fileConfig(os.path.join(app.config.get("BASE_PATH"), "config", "log.conf"))

from app.views.data import init_service
from app.views.auth import auth_service
from app.views.user import user_service
# from app.views.alert import alert_service
from app.views.index import ok_service

app.register_blueprint(init_service, url_prefix="/db")
app.register_blueprint(auth_service)
app.register_blueprint(user_service, url_prefix="/users")
# app.register_blueprint(alert_service, url_prefix="/alert")
app.register_blueprint(ok_service)

login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id) :
    return User.get_or_none(User.id == user_id)

@login_manager.unauthorized_handler
def unauthrized_user():
    return JsonResult(Status.FAILED, "Unauthrized.")

@app.before_first_request
def _init_db():
    init_db()

@app.before_request
def _db_create():
    if db.is_closed():
        db.connect()

@app.teardown_request
def _db_close(exec):
    if not db.is_closed():
        db.close()


