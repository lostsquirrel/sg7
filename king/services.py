# -*- encoding:utf-8 -*-
__author__ = 'lisong'

from king.models import soldierDAO
from king.models import generalDAO

range_type = (u'近战', u'远程')
soldier_type = (u'步兵', u'骑兵')
armor_type = (u'轻甲', u'重甲')

def get_soldiers():
    records = soldierDAO.get_soldiers()
    for s in records:
        s.skills = soldierDAO.get_soldier_skills(s.id)
        for sk in s.skills:
            sk.level_tag = '%s_%s' % (s.id, sk.id)

    return records

def get_generals():
    gs = generalDAO.get_generals()

    return gs

