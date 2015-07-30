# -*- coding:utf-8 -*-
'''
Created on 2015年5月14日

@author: zhuhua
'''
from simpletor import application
from demo import services as city_service

@application.RequestMapping("/")
class IndexHandler(application.RequestHandler):
    def get(self):
        cities = city_service.get_cities(1, 10)
        self.render('index.html', cities = cities)