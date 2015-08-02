# -*- coding:utf-8 -*-
'''
Created on 2015年5月14日

@author: zhuhua
'''
from simpletor import application
from demo import services

@application.RequestMapping("/")
class IndexHandler(application.RequestHandler):
    def get(self):
        self.render("index.html")

@application.RequestMapping("/cities")
class CityHandler(application.RequestHandler):
    def get(self):
        page = self.get_argument(name="page", default="1")
        size = self.get_argument(name="size", default="10")
        cities = services.get_cities(int(page), int(size))
        self.render_json(cities)

@application.RequestMapping("/items")
class CityHandler(application.RequestHandler):
    def get(self):
        page = self.get_argument(name="page", default="1")
        size = self.get_argument(name="size", default="10")
        cities = services.get_items(int(page), int(size))
        self.render_json(cities)