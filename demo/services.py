# -*- encoding:utf-8 -*-
__author__ = 'lisong'

from demo.models import cityDAO

def get_cities(page, size):
    offset = (page - 1) * size;
    return cityDAO.get_cities(size, offset), cityDAO.count_cities