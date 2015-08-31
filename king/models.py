__author__ = 'lisong'

from simpletor import torndb

class SolderSkills(torndb.Row):
    """

    """
    def __init__(self):
        self.id = None
        self.skill_name = None
        self.skill_desc = None
        self.icon = None
        self.formula = None
class Soldier(torndb.Row):
    """

    """
    def __init__(self):
        self.id = None
        self.soldier_name = None
        self.attack_range = None
        self.soldier_type = None
        self.armor = None
        self.skill_green = None
        self.kill_blue = None
        self.kill_purple = None
        self.kill_gold = None
        self.kill_green_name = None
        self.skill_blue_name = None
        self.skill_purple_name = None
        self.skill_gold_name = None
class SoldierDAO:

    @torndb.select
    def get_soldiers(self):
        sql = '''SELECT id, soldier_name, attack_range, soldier_type, armor
        FROM king_soldier
        '''
        return sql

    @torndb.get
    def get_soldier_skill(self, skill_id):
        sql = '''SELECT id, skill_name, skill_desc, icon, formula, max_level
        FROM king_soldier_skills
        WHERE id = %s
        '''
        return sql

    @torndb.select
    def get_soldier_skills(self, soldier_id):
        sql = '''SELECT sk.id, sk.skill_name, sk.skill_desc, sk.icon, sk.formula, sk.max_level
        FROM king_soldier_skills sk
        JOIN king_soldier_skill_conj co
        ON sk.id = co.skill_id
        WHERE co.soldier_id = %s
        ORDER BY co.skill_level ASC
        '''
        return sql

soldierDAO = SoldierDAO()

class GeneralDAO:

    @torndb.select
    def get_generals(self):
        sql = """SELECT * FROM `king_general"""
        return sql

generalDAO = GeneralDAO()