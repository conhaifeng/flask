#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 19:44
# @Author  : haifeng.hu

from peewee import *
from app import db
from datetime import datetime

class BaseModel(Model):

    class Meta:
        database = ""

class Role(BaseModel):
    id = AutoField()
    role_name = CharField(40)
    privilege = CharField()

class User(BaseModel):
    id = AutoField()
    username = CharField(null=True)
    password = CharField()
    phone = CharField(max_length=11)
    role = ForeignKeyField(Role, field="id", backref="user")
    remark = CharField(null=True, max_length=100)
    created_time = DateTimeField(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

class Post(BaseModel):
    id = AutoField()
    user_id = ForeignKeyField(User, field="id", backref="post")
    title =CharField(max_length=80)
    content = CharField(max_length=512)
    remark = CharField(max_length=100, null=True)
    udpate_time = DateTimeField()
    created_time = DateTimeField(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

class Point(BaseModel):
    userid = ForeignKeyField(User, field="id", backref="point")
    point = IntegerField()
    update_time = DateTimeField()




