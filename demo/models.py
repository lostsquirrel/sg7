__author__ = 'lisong'

from simpletor import torndb

class City(torndb.Row):
    """

    """
    def __init__(self):
        self.id = None
        self.city_id = None
        self.city_name = None

class CityDAO:

    @torndb.select
    def get_cities(self, limit, offset):
        sql = '''SELECT city_id, city_name
        FROM cities
        ORDER BY city_id ASC
        LIMIT %s OFFSET %s '''
        return sql

    @torndb.get
    def count_cities(self):
        sql = '''SELECT count(id) as total
        FROM cities
        '''

        return sql


city_dao = CityDAO()


class ItemDAO:

    @torndb.select
    def get_items(self, limit, offset):
        sql = '''
        SELECT item_id, item_name, item_type, item_lv, description
        FROM items
        ORDER BY item_id asc
        LIMIT %s OFFSET %s
        '''

    @torndb.get
    def count_item(self):
        sql = '''
        SELECT COUNT(id) AS total
        FROM items
        '''

item_dao = ItemDAO()