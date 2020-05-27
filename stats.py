import db

def get_allName():
    names = []
    cnx = db.cnx()
    cursor = cnx.cursor()

    query = ("SELECT name FROM stats")

    cursor.execute(query)

    for i in cursor:
        names.append(i[0])
        # print(i[0])

    cursor.close()
    cnx.close()
    # print(names)
    return names


def get_stats(name):
    cnx = db.cnx()
    cursor = cnx.cursor()
    query = (f"SELECT * FROM stats WHERE name = '{name}'")
    stats = []
    cursor.execute(query)
    for i in cursor:
        stats.append(i)
    cursor.close()
    cnx.close()
    return stats[0]


def get_att(n):
    att = get_stats(n)[1]
    return str(att)


def get_def(n):
    defense = get_stats(n)[2]
    return str(defense)


def get_curr_hp(n):
    curr_hp = get_stats(n)[3]
    return str(curr_hp)


def get_max_hp(n):
    max_hp = get_stats(n)[4]
    return str(max_hp)


def get_coins(n):
    coins = get_stats(n)[5]
    return str(coins)


def get_gem(n):
    gem = get_stats(n)[6]
    return str(gem)


def get_curr_xp(n):
    curr_xp = get_stats(n)[7]
    return str(curr_xp)


def get_max_xp(n):
    max_xp = get_stats(n)[8]
    return str(max_xp)


def get_level(n):
    level = get_stats(n)[9]
    return str(level)


def set_hp(name, new_hp):
    cnx = db.cnx()
    cursor = cnx.cursor()
    query = f"UPDATE `kogrpg`.`stats` SET `curr_hp` = '{new_hp}' WHERE (`name` = '{name}');"
    cursor.execute(query)
    cnx.commit()
    cursor.close()
    cnx.close()
    return True


def set_xp(name, new_xp):
    cnx = db.cnx()
    cursor = cnx.cursor()
    new_xp += int(get_curr_xp(name))
    query = f"UPDATE `kogrpg`.`stats` SET `curr_xp` = '{new_xp}' WHERE (`name` = '{name}');"
    cursor.execute(query)
    cnx.commit()
    cursor.close()
    cnx.close()
    return True


def set_coins(name, coins):
    cnx = db.cnx()
    cursor = cnx.cursor()
    coins += int(get_coins(name))
    query = f"UPDATE `kogrpg`.`stats` SET `coins` = '{coins}' WHERE (`name` = '{name}');"
    cursor.execute(query)
    cnx.commit()
    cursor.close()
    cnx.close()
    return True


def you_died(name):
    cnx = db.cnx()
    cursor = cnx.cursor()
    lvl = int(get_level(name))-1
    if lvl <= 1:
        query = f"UPDATE `kogrpg`.`stats` SET `curr_hp` = '{get_max_hp(name)}', `curr_xp` = '0', `level` = '1' WHERE (`name` = '{name}');"
    else:
        query = f"UPDATE `kogrpg`.`stats` SET `curr_hp` = '{get_max_hp(name)}', `curr_xp` = '0', `level` = '{lvl}' WHERE (`name` = '{name}');"
    cursor.execute(query)
    cnx.commit()
    cursor.close()
    cnx.close()
    return True

