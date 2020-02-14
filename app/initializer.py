#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/14 18:00
# @Author  : haifeng.hu

import logging

from app.models import *
from app.extensions import db

logger = logging.getLogger("sample1")

def init_db():

    if not db.table_exists("user"):
        logger.info("Create tables.")
        db.create_tables([Role, User, Post, Point, RoleUser])
        logger.info("Insert roles info.")
        _init_data()
        logger.info("Init tables successful.")

    if not User.get_or_none(User.username == "admin"):
        _init_user()
        logger.info("Init user successful.")

def _init_data():
    visitor = {"role_name":"visitor", "privilege":"visit"}
    user = {"role_name": "user", "privilege": "visit,add,delete,update"}
    admin = {"role_name": "admin", "privilege": "all"}

    Role.insert_many([visitor, user, admin]).execute()

def _init_user():
    user_id = User.insert(username="admin", password="123456", phone="18766666004").execute()
    role = Role.get(Role.role_name == "admin")
    RoleUser.insert(role_id=role.id, user_id=user_id).execute()