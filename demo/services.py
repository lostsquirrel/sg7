# -*- encoding:utf-8 -*-
__author__ = 'lisong'

from demo.models import city_dao
from demo.models import item_dao
from simpletor.utils import pagination

item_type = ('NPC剑', '大刀', '道具', '弓', '剑', '配方', '枪', '扇', '消耗品', '坐骑', '未开放')
item_prop_type = ('武力', '智力', '体力', '技力', '速度', '忠诚', '武将技', '军师技', '特性')

def get_cities(page, size):
    offset = (page - 1) * size;
    records = city_dao.get_cities(size, offset)
    total = city_dao.count_cities()

    cities = pagination(records, page, size, total)
    return cities

def get_items(page, size):
    offset = (page - 1) * size;
    records = item_dao.get_items(size, offset)
    for record in records:
        record['item_type'] = item_type[record['item_type']]
    total = item_dao.count_item()
    items = pagination(records, page, size, total)

    return items
