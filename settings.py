# -*- coding:utf-8 -*-
'''
Created on 2013-3-26

@author: zhuhua
'''
import os


installed_apps = ['demo', 'angularjs']

template_dir = os.path.join(os.path.dirname(__file__), "templates")
static_dir = os.path.join(os.path.dirname(__file__), "static")

deploy_sae = False

port = 8888

db_host = '127.0.0.1'
db_name = 'sg7'
db_user = 'sg7'
db_password = '123456'
db_max_idle_time = 7 * 3600

if deploy_sae:
    import sae.const
    db_host = sae.const.MYSQL_HOST + ":" + sae.const.MYSQL_PORT
    db_name = sae.const.MYSQL_DB
    db_user = sae.const.MYSQL_USER
    db_password = sae.const.MYSQL_PASS
    db_max_idle_time = 5
