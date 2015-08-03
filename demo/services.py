# -*- encoding:utf-8 -*-
__author__ = 'lisong'

from demo.models import city_dao
from demo.models import item_dao
from simpletor.utils import pagination

def get_cities(page, size):
    offset = (page - 1) * size;
    records = city_dao.get_cities(size, offset)
    total = city_dao.count_cities()

    cities = pagination(records, page, size, total)
    return cities

def get_items(page, size):
    offset = (page - 1) * size;
    records = item_dao.get_items(size, offset)
    total = item_dao.count_item()
    items = pagination(records, page, size, total)

    return items
