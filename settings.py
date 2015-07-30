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

port = 8080

db_host = '127.0.0.1'
db_name = 'sg7'
db_user = 'sg7'
db_password = '123456'
