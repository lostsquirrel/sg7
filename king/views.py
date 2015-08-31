# -*- coding:utf-8 -*-

from simpletor import application
from king import services
import settings

range_type = (u'近战', u'远程')
soldier_type = (u'步兵', u'骑兵')
armor_type = (u'轻甲', u'重甲')

@application.RequestMapping("/king(.*)")
class IndexHandler(application.RequestHandler):
    def get(self, path):
        self.render("king/index.html")

# @application.RequestMapping("/king/(.*)")
# class KingHandler(application.RequestHandler):
#     def get(self, path):
#         if 'api' in path:
#             self.redirect('/king')
#
#         self.

@application.RequestMapping("/api/king/soldiers")
class SoldierHandler(application.RequestHandler):
    def get(self):
        page = self.get_argument(name="page", default="1")
        size = self.get_argument(name="size", default="10")
        soldiers = services.get_soldiers()
        self.render_json(soldiers)

@application.RequestMapping("/api/king/generals")
class GeneralHandler(application.RequestHandler):
    def get(self):
        page = self.get_argument(name="page", default="1")
        size = self.get_argument(name="size", default="10")
        gs = services.get_generals()
        self.render_json(gs)



