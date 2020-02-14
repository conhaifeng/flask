#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/14 18:00
# @Author  : haifeng.hu

import logging

from app.models import *
from app.extensions import db
from app import app

logger = logging.getLogger("sample1")

@app.before_first_request
def init_db():

    if db.table_exists(User) and User.get_or_none(User.username == "admin"):
        return

    db.create_tables([Role, User, Post, Point, RoleUser])
    init_data()
    logger.info("Init data successful.")
    init_user()
    logger.info("Init user successful.")

def init_data():
    visitor = {"role_name":"visitor", "privilege":"visit"}
    user = {"role_name": "user", "privilege": "visit,add,delete,update"}
    admin = {"role_name": "admin", "privilege": "all"}

    Role.insert_many([visitor, user, admin]).execute()

def init_user():
    user_id = User.insert(username="admin", password="123456", phone="18766666004").execute()
    role = Role.get(Role.role_name == "admin")
    RoleUser.insert(role_id=role.id, user_id=user_id).execute()