#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/1 10:57
# @Author  : haifeng.hu

from peewee import SqliteDatabase
from flask_login import LoginManager

db = SqliteDatabase("20190903", pragmas={
    "journal_mode":"wal",
    "cache_size": -1 * 64000,
    "ignore_check_constraints":0,
    "synchronous":0,
    "foreign_keys":1
})

login_manager = LoginManager()