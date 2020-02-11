#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 20:18
# @Author  : haifeng.hu

import argparse

from app import app

if __name__ == "__main__":

    parse = argparse.ArgumentParser()
    parse.add_argument("-p", dest='port', default=8083)
    args = parse.parse_args()
    # app = create_app()
    app.run(host="127.0.0.1",port=args.port, debug=True)