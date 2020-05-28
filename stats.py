import db
import pets as p
import items as item
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



def get_items(name):
    cnx = db.cnx()
    cursor = cnx.cursor()
    query = (f"SELECT * FROM inventory WHERE name = '{name}'")
    items = {}
    cursor.execute(query)
    for (id, user, item, quantity, equip, type) in cursor:
        items[item] = quantity
    cursor.close()
    cnx.close()
    return items
# print(get_items("OneForFourKay#5753").keys())


def get_att(n):
    name_weapon = item.get_Equipped(n)[0]
    att = get_stats(n)[1] + 1 + 2 * (int(get_level(n)) - 1)
    if name_weapon:
        boosts = int(item.get_boosts(name_weapon))
        att += boosts
    return str(att)


def get_def(n):
    name_shield = item.get_Equipped(n)[1]
    defense = get_stats(n)[2] + 1 + 2*(int(get_level(n)) - 1)
    if name_shield:
        boosts = int(item.get_boosts(name_shield))
        defense += boosts
        return str(defense)


def get_curr_hp(n):
    curr_hp = get_stats(n)[3]
    return str(curr_hp)

def get_max_hp(n):
    max_hp = get_stats(n)[4] + 100 + 10*(int(get_level(n)) - 1)
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
    realm = round(int(get_level(n)) // 10)
    L = int(get_level(n))
    if realm == 0:
        realm = 1
    max_xp = (50 * L * L - 50 * L) + realm * 10
    return str(max_xp)


def get_progress(n):
    progress = str(round((int(get_curr_xp(n))/int(get_max_hp(n))*100)  ,2))
    return str(progress)


def get_realm(n):
    realm = round(int(get_level(n)) // 10)
    return str(realm)


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
        query = f"UPDATE `kogrpg`.`stats` SET `curr_xp` = '0', `level` = '1' WHERE (`name` = '{name}');"
    else:
        query = f"UPDATE `kogrpg`.`stats` SET `curr_xp` = '0', `level` = '{lvl}' WHERE (`name` = '{name}');"
    cursor.execute(query)
    cnx.commit()
    cursor.close()
    cnx.close()
    return True


def heal(name):
    cnx = db.cnx()
    cursor = cnx.cursor()
    query = f"UPDATE `kogrpg`.`stats` SET `curr_hp` = '{get_max_hp(name)}' WHERE (`name` = '{name}');"
    cursor.execute(query)
    cnx.commit()
    cursor.close()
    cnx.close()
    return True


def check_level(n):
    xp = int(get_curr_xp(n))
    max_xp = int(get_max_xp(n))
    levelup = False
    while xp >= max_xp:
        lvl = int(get_level(n)) + 1
        xp -= max_xp
        levelup = True
        max_xp
    if levelup:
        cnx = db.cnx()
        cursor = cnx.cursor()
        query = f"UPDATE `kogrpg`.`stats` SET `curr_xp` = '{xp}', `level` = '{lvl}', `curr_hp` = '{get_max_hp(n)}' WHERE (`name` = '{n}');"
        cursor.execute(query)
        cnx.commit()
        cursor.close()
        cnx.close()
        return True
    return False


def check_player_new(n):
        array = get_allName()
        new = True
        for i in array:
            if i == str(n).strip():
                new = False
        return new



