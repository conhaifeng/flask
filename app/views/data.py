#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/6 16:14
# @Author  : haifeng.hu

import logging

from flask.blueprints import Blueprint

from app import db, app
from app.models import *
from app.utils.globle import *

init_service = Blueprint("init", __name__)

logger = logging.getLogger("sample1")

@init_service.route("/init", methods=["get"])
def init_db():
    db.create_tables([Role, User, Post, Point, RoleUser])
    init_data()
    logger.info("Init data successful.")
    return JsonResult()

@init_service.route("/drop", methods=["get"])
def drop_db():
    db.drop_tables([Role, User, Post, Point, RoleUser])
    logger.info("Drop table successful.")
    return JsonResult()

def init_data():
    visitor = {"role_name":"visitor", "privilege":"visit"}
    user = {"role_name": "user", "privilege": "visit,add,delete,update"}
    admin = {"role_name": "admin", "privilege": "all"}

    Role.insert_many([visitor, user, admin]).execute()
