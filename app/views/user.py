#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 20:10
# @Author  : haifeng.hu

import logging

from flask import current_app as app, request, session, jsonify
from flask.blueprints import Blueprint
from flask_login import login_required,current_user
from app.forms import UserForm
from app.models import User, RoleUser, Role
from app.utils.globle import *

user_service = Blueprint("user", __name__)

logger = logging.getLogger("sample2")


@user_service.route("/register", methods=["post"])
def add_user():
    user = UserForm()

    if not user.validate_on_submit():
        error_msg = "{}:{}".format(*user.error)
        logger.debug(error_msg)
        return JsonResult(Status.VALIDATE_FAILED.value, error_msg)

    result = User.select().where(User.phone == user.phone.data)
    if User.select().where(User.phone == user.phone.data).exists():
        logger.info("Phone exsited. Add failed.")
        return JsonResult(Status.EXISTED.value, "User exsited.")

    result = User.insert(username=user.username.data, password=user.password.data, phone=user.phone.data).execute()
    logger.info("add user successful. DB result is {}".format(result))
    return JsonResult()


@user_service.route("/<userid>", methods=["put"])
@login_required
def update_user(userid):
    return "update_user."


@user_service.route("/<userid>", methods=["get"])
@login_required
def query_user(userid):
    user = User.get_or_none(userid)
    if user :
        return JsonResult(data=user)

    return JsonResult(Status.FAILED, "No such user.")

@user_service.route("/", methods=['get'])
@login_required
def query_users():
    users = User.select(User, Role.role_name).join(RoleUser).join(Role).dicts()
    return JsonResult(data=list(users))

@user_service.route("/permission", methods=['get'])
@login_required
def query_perssion():
    roles = RoleUser.select(Role.role_name).join(Role).where(RoleUser.user_id == current_user.id).objects()
    result = {}
    for role in roles :
        result["role"] = role.role_name
        return JsonResult(data=result)

    return JsonResult(Status.FAILED, "Query role failed.")

@user_service.route("/password", methods=['post'])
@login_required
def change_passowrd():
    user = User.get_by_id(current_user.id)
    if user.password != request.json['oldPassword']:
        return JsonResult(Status.FAILED, "Old password not equal.")

    if request.json['newPassword'] != request.json['newPasswordAG']:
        return JsonResult(Status.FAILED, "New password not equal.")

    user.password = request.json["newPassword"]
    user.save()
    return JsonResult(Status.SUCCESS, "Success.")