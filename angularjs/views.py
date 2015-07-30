# -*- coding:utf-8 -*-

__author__ = 'lisong'

from simpletor import application

@application.RequestMapping("/angular/hello")
class IndexHandler(application.RequestHandler):
    def get(self):
        self.render('angularjs/hello.html')