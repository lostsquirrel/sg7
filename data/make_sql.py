# -*- encoding:utf-8 -*-
__author__ = 'lisong'

def general_reader(file_name):
    res = dict()
    char = ''
    with open(file_name) as items:
        for x in items.readlines():
            try:
                item = x.strip().split(' ')
                res[int(item[0])] = item
            except Exception, e:
                print e

    return res

def make_group_skills():
    id_name = general_reader("ArmyGroupSkill.txt")

    id_desc = general_reader("ArmyGroupSkillDescription.txt")

    for skill_id in id_name.keys():
        try:
            sql_format = 'INSERT INTO skills (name, description, skill_no, skill_type) VALUES (\'%s\', \'%s\', %s, 0);'
            sql = sql_format % (id_name[skill_id][1], id_desc[skill_id][1], skill_id)
            print sql
        except:
            pass

def make_army_skills():
    id_name = general_reader("ArmySkill.txt")

    id_desc = general_reader("ArmySkillDescription.txt")

    for skill_id in id_name.keys():
        try:
            sql_format = 'INSERT INTO skills (name, description, skill_no, skill_type) VALUES (\'%s\', \'%s\', %s, 1);'
            sql = sql_format % (id_name[skill_id][1], id_desc[skill_id][1], skill_id)
            print sql
        except:
            pass

def make_gen_skills():
    id_name = general_reader("GenSkill.txt")

    id_desc = general_reader("GenSkillDescription.txt")

    for skill_id in id_name.keys():
        try:
            sql_format = 'INSERT INTO skills (name, description, skill_no, skill_type) VALUES (\'%s\', \'%s\', %s, 2);'
            sql = sql_format % (id_name[skill_id][1], id_desc[skill_id][1], skill_id)
            print sql
        except:
            pass

def make_bf_magic():
    id_name = general_reader("BFMagic.txt")
    for magic_id in id_name.keys():
        try:
            sql_format = 'INSERT INTO magics (magic_id, magic_name, magic_type) VALUES (\'%s\', \'%s\', 0);'
            sql = sql_format % (magic_id, id_name[magic_id][1])
            print sql
        except:
            pass
def make_sf_magic():
    id_name = general_reader("SFMagic.txt")
    for magic_id in id_name.keys():
        try:
            sql_format = 'INSERT INTO magics (magic_id, magic_name, magic_type) VALUES (\'%s\', \'%s\', 1);'
            sql = sql_format % (magic_id, id_name[magic_id][1])
            print sql
        except:
            pass

def make_city():
    id_name = general_reader("City.txt")
    for magic_id in id_name.keys():
        try:
            sql_format = 'INSERT INTO cities (city_id, city_name) VALUES (\'%s\', \'%s\');'
            sql = sql_format % (magic_id, id_name[magic_id][1])
            print sql
        except:
            pass

def make_gen_skills():
    id_name = general_reader("Format.txt")

    id_desc = general_reader("FormatDescription.txt")

    for format_id in id_name.keys():
        try:
            sql_format = 'INSERT INTO formats (format_name, description, format_id) VALUES (\'%s\', \'%s\', \'%s\');'
            sql = sql_format % (id_name[format_id][1], id_desc[format_id][1], format_id)
            print sql
        except:
            pass

def make_gen():
    id_name = general_reader("General.txt")
    for gen_id in id_name.keys():
        try:
            sql_format = 'INSERT INTO generals (general_name, general_id) VALUES (\'%s\', \'%s\');'
            sql = sql_format % (id_name[gen_id][1], gen_id)
            print sql
        except:
            pass

def make_gen_lv():
    lv_exp = general_reader("GenLV.txt")
    for lv in lv_exp.keys():
        try:
            sql_format = 'INSERT INTO gen_lv (level, exp) VALUES (\'%s\', \'%s\');'
            sql = sql_format % (lv, lv_exp[lv][1])
            print sql
        except:
            pass

def make_race():
    lv_exp = general_reader("Race.txt")
    for lv in lv_exp.keys():
        try:
            sql_format = 'INSERT INTO races (race_id, race_name) VALUES (\'%s\', \'%s\');'
            sql = sql_format % (lv, lv_exp[lv][1])
            print sql
        except:
            pass

def make_super_atk_magic():
    id_name = general_reader("SuperAtk.txt")

    id_desc = general_reader("SuperAtkDescription.txt")
    count = 1
    for magic_id in id_name.keys():
        try:
            sql_format = '''INSERT INTO magics
            (magic_id, magic_name, description, magic_type)
            VALUES (\'%d\', \'%s\', \'%s\', 2);'''
            # print magic_id, id_name[magic_id][1], id_desc[count][1]
            sql = sql_format % (magic_id, id_name[magic_id][1], id_desc[count][1])
            print sql
            count += 1
        except Exception, e:
            print e

def make_super_atk_magic():
    id_name = general_reader("Soldier.txt")

    id_desc = general_reader("SoldierDescription.txt")
    count = 1
    for soldier_id in id_name.keys():
        try:
            sql_format = '''INSERT INTO soldiers
            (soldier_id, soldier_name, description, soldier_type)
            VALUES (\'%d\', \'%s\', \'%s\', \'%s\');'''
            # print magic_id, id_name[magic_id][1], id_desc[count][1]
            description = ''
            if id_desc.get(soldier_id) is not None:
                description = id_desc[soldier_id][1]
            sql = sql_format % (soldier_id, id_name[soldier_id][1],id_name[soldier_id][2], description)
            print sql
            count += 1
        except Exception, e:
            print e

def make_title():
    id_title = general_reader("Title.txt")
    for title_id in id_title.keys():
        try:
            sql_format = 'INSERT INTO titles (title_id, title_name) VALUES (\'%s\', \'%s\');'
            sql = sql_format % (title_id, id_title[title_id][1])
            print sql
        except:
            pass

def make_thing():
    id_title = general_reader("Thing.txt")
    for title_id in id_title.keys():
        try:
            sql_format = 'INSERT INTO items (item_id, item_name, item_type, item_lv) VALUES (\'%s\', \'%s\', \'%s\', \'%s\');'
            sql = sql_format % (title_id, id_title[title_id][1], id_title[title_id][2], id_title[title_id][3])
            print sql
        except:
            pass
if __name__ == '__main__':
    magic_types = (u'武将技', u'军师技', u'必杀技')
    # make_group_skills()
    # make_army_skills()
    # make_gen_skills()
    # make_bf_magic()
    # make_sf_magic()
    # make_city()
    # make_gen_skills()
    # make_gen()
    # make_gen_lv()
    # make_race()
    # make_super_atk_magic()
    # make_super_atk_magic()
    # make_title()
    # make_thing()