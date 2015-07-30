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
    def get_citys(self, limit, offset):
        sql = '''select city_id, city_name from cities order by city_id asc limit %s offset %s '''
        return sql

cityDAO = CityDAO()
