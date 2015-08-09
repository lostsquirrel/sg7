# -*- coding:utf-8 -*-
'''
Created on 2015年5月14日

@author: zhuhua
'''
from simpletor import application
from demo import services
import settings

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
class ItemHandler(application.RequestHandler):
    def get(self):
        page = self.get_argument(name="page", default="1")
        size = self.get_argument(name="size", default="10")
        cities = services.get_items(int(page), int(size))
        self.render_json(cities)

@application.RequestMapping("/test")
class TestHandler(application.RequestHandler):
    def get(self):
        data = {
            'db_name': settings.db_name,
            'db_host': settings.db_host,
            'db_password': settings.db_password,
            'db_user': settings.db_user,
        }
        self.render_json(data)