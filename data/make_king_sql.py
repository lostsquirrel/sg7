# -*- encoding:utf-8 -*-
__author__ = 'lisong'

import xlrd

data = xlrd.open_workbook('king.xls')
range_type = (u'近战', u'远程')
soldier_type = (u'步兵', u'骑兵')
armor_type = (u'轻甲', u'重甲')

def build_soldier():
    soldier = data.sheet_by_index(1)
    nrows = soldier.nrows
    ncols = soldier.ncols
    for row in range(1, nrows):
        raw_value = soldier.row(row)
        name = raw_value[0].value
        attr = raw_value[1]
        ax = attr.value.split(u"|")

        attack_range_name = unicode(ax[0].strip())
        # print attack_range_name
        attack_range = range_type.index(attack_range_name)
        solder_type_name = unicode(ax[1].strip())
        # print solder_type_name
        st = soldier_type.index(solder_type_name)
        armor_name = unicode(ax[2].strip())
        rt = armor_type.index(armor_name)
        snd = raw_value[2].value
        _snd = snd.split('\n')
        sk = _snd[0].split(u"：")[0]
        sb = _snd[1].split(u"：")[0]
        sp = _snd[2].split(u"：")[0]
        sg = _snd[3].split(u"：")[0]
        sql_format = """insert into king_soldier
        (soldier_name, attack_range, soldier_type,
        armor, skill_green_name, skill_blue_name,
         skill_purple_name, skill_gold_name)
         values
         ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');
         """
        print sql_format % (name, attack_range, st, rt, sk, sb, sp, sg)
    # print(nrows, ncols)
def build_soldier_skills():
    soldier = data.sheet_by_index(1)
    col_values = soldier.col_values(2)
    icons = soldier.col_values(3)

    for x in range(1, len(col_values)):
        snd = col_values[x]
        _snd = snd.split('\n')

        # print(_snd)
        icon = icons[x]
        _icon = icon.split('\n')
        for y in range(4):
            nd = _snd[y]
            _nd = nd.split(u"：")
            sql_format = "insert into king_soldier_skills (skill_name, skill_desc, icon) values ('%s', '%s', '%s');"
            # print(_nd)
            # print(_icon)
            # print(y)
            print sql_format % (_nd[0].strip(), _nd[1].strip(), _icon[y].strip())

if __name__ == '__main__':
    build_soldier()