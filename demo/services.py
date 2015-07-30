# -*- encoding:utf-8 -*-
__author__ = 'lisong'

from demo.models import cityDAO

def get_cities(page, size):
    return cityDAO.get_citys(10, 0)