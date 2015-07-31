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
        sql = '''SELECT count(id)
        FROM cities
        '''

        return sql
cityDAO = CityDAO()
