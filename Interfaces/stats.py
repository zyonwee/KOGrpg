import db
import KoGDAO.userDAO as u


def get_allName():
    names = []
    query = "SELECT name FROM stats"
    cnx = db.cnx()
    cursor = cnx.cursor()
    cursor.execute(query)
    for i in cursor:
        names.append(i[0])
        # print(i[0])
    cursor.close()
    cnx.close()
    # print(names)
    return names


def you_died(name):
    cnx = db.cnx()
    cursor = cnx.cursor()
    lvl = int(u.get_level(name)) - 1
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
    query = f"UPDATE `kogrpg`.`stats` SET `curr_hp` = '{u.get_max_hp(name)}' WHERE (`name` = '{name}');"
    cursor.execute(query)
    cnx.commit()
    cursor.close()
    cnx.close()
    return True


def check_level(n):
    xp = int(u.get_curr_xp(n))
    max_xp = int(u.get_max_xp(n))
    levelup = False
    while xp >= max_xp:
        lvl = int(u.get_level(n)) + 1
        xp -= max_xp
        levelup = True
        max_xp
    if levelup:
        cnx = db.cnx()
        cursor = cnx.cursor()
        new_hp = str(int(u.get_max_hp(n)) + 10)
        query = f"UPDATE `kogrpg`.`stats` SET `curr_xp` = '{xp}', `level` = '{lvl}', `curr_hp` = '{new_hp}' WHERE (`name` = '{n}');"
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



