#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 20:18
# @Author  : haifeng.hu

from app import app

if __name__ == "__main__":

    # app = create_app()
    app.run(host="127.0.0.1",port=8083, debug=True)