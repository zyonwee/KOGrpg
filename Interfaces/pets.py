import db
import KoGDAO.allPetsDAO as ap
import KoGDAO.myPetsDAO as mp
import KoGDAO.userDAO as u

def increase_pet(i, n):
    cnx = db.cnx()
    if i in mp.get_myPets(n).keys():
        return False
    else:
        attr = ap.get_attr(i)
        stg = ap.get_stage(i)
        link = ap.get_img(i)
        cursor = cnx.cursor()
        hp = mp.max_hp(i, 1)
        query = f"INSERT INTO `kogrpg`.`mypets` (`name`, `pets`, `HP` , `Attribute`, `Stage`, `Image link`) " \
                f"VALUES ('{n}','{i}', '{hp}','{attr}', '{stg}', '{link}');"
        print(query)
        cursor.execute(query)
        cnx.commit()
        cursor.close()
        cnx.close()
        return True


def setMain(p, n):
    stack = []
    for i in mp.get_myPets(n).keys():
        stack.append(i.lower())
    if p in stack:
        cnx = db.cnx()
        cursor = cnx.cursor()
        query = f"UPDATE `kogrpg`.`mypets` SET `Equip Slots` = 'NONE' WHERE (`name` = '{n}');"
        cursor.execute(query)
        cnx.commit()
        cursor.close()

        cursor = cnx.cursor()
        query = f"UPDATE `kogrpg`.`mypets` SET `Equip Slots` = 'Main Pet' WHERE (`pets` = '{p}' AND `Name` = '{n}');"
        cursor.execute(query)
        cnx.commit()
        cursor.close()
        cnx.close()
        return True
    else:
        return False
        # print(names)
# print(setMain("puni", "OneForFourKay#5753"))

def getMain(n):
    try:
        cnx = db.cnx()
        cursor = cnx.cursor()
        link = []
        query = f"SELECT `Image link` FROM mypets WHERE (`Equip Slots` = 'Main Pet' and `name` = '{n}');"
        cursor.execute(query)
        for i in cursor:
            link.append(i)
        cnx.commit()
        cursor.close()
        return link[0][0]
    except:
        return ""


def getMain_Name(n):
    try:
        cnx = db.cnx()
        cursor = cnx.cursor()
        link = []
        query = f"SELECT `pets` FROM mypets WHERE (`Equip Slots` = 'Main Pet' and `name` = '{n}');"
        cursor.execute(query)
        for i in cursor:
            link.append(i)
        cnx.commit()
        cursor.close()
        return link[0][0]
    except:
        return ""


def check_level(p, n):
    xp = int(mp.get_curr_xp(p, n))
    lvl = int(mp.get_level(p, n))
    levelup = [False, lvl]
    lvlcount = 0
    while not levelup[0]:
        max_xp = int(mp.get_max_xp(p, n, lvl))
        if xp > max_xp:
            lvl += 1
            xp -= max_xp
            lvlcount += 1
        else:
            levelup = [True, lvlcount]
    if levelup[0]:
        cnx = db.cnx()
        cursor = cnx.cursor()
        new_hp = mp.max_hp(p, lvl)
        query = f"UPDATE `kogrpg`.`mypets` SET `xp` = '{xp}', `level` = '{lvl}', `hp` = '{new_hp}' WHERE (`pets` = '{p}');"
        cursor.execute(query)
        cnx.commit()
        cursor.close()
        cnx.close()
        return [True, lvlcount]
    return [False, 0]


def set_xp(new_xp, name):
    cnx = db.cnx()
    cursor = cnx.cursor()
    pet = getMain_Name(name)
    new_xp = int(new_xp)
    new_xp += int(mp.get_curr_xp(pet, name))
    print(new_xp)
    query = f"UPDATE `kogrpg`.`mypets` SET `xp` = '{new_xp}' WHERE (`pets` = '{pet}');"
    cursor.execute(query)
    cnx.commit()
    cursor.close()
    cnx.close()
    return True

def can_evolve(p, n):
    level = int(mp.get_level_l(p, n))
    stage = mp.get_stage_l(p, n)
    player_realm = int(u.get_realm(n))
    print(player_realm)
    print(level, stage)
    if stage == "Baby" and level >= 10:
        if player_realm >= 0:
            return "yes"
        else:
            return "You need to be Realm 0 at least"

    elif stage == "In-Training" and level >= 20:
        if player_realm >= 1:
            return "yes"
        else:
            return "You need to be Realm 1 at least"

    elif stage == "Rookie" and level >= 30:
        if player_realm >= 2:
            return "yes"
        else:
            return "You need to be Realm 2 at least"

    elif stage == "Champion" and level >= 40:
        if player_realm >= 3:
            return "yes"
        else:
            return "You need to be Realm 3 at least"

    elif stage == "Ultimate" and level >= 50:
        if player_realm >= 4:
            return "yes"
        else:
            return "You need to be Realm 4 at least"

    elif stage == "Mega" and level >= 60:
        if player_realm >= 5:
            return "yes"
        else:
            return "You need to be Realm 5 at least"

    elif stage == "Ultra" and level >= 70:
        if player_realm >= 6:
            return "yes"
        else:
            return "You need to be Realm 6 at least"

    else:
        return "Your pet is not high level enough!!"


def check_evo_mat(stage, n):
    all_items = u.get_items(n).keys()
    if stage == "Baby" and "Baby Core".lower() in all_items:
        return ["Baby Core", True]

    elif stage == "In-Training" and "In-Training Core".lower() in all_items:
        return ["In-Training Core", True]

    elif stage == "Rookie" and "Rookie Core".lower() in all_items:
        return ["Rookie Core", True]

    elif stage == "Champion" and "Champion Core".lower() in all_items:
        return ["Champion Core", True]

    elif stage == "Ultimate" and "Ultimate Core".lower() in all_items:
        return ["Ultimate Core", True]

    elif stage == "Mega" and "Mega Core".lower() in all_items:
        return ["Mega Core", True]

    elif stage == "Ultra" and "Ultra Core".lower() in all_items:
        return ["Ultra Core", True]

    else:
        return ["You dont have the Necessary Core. Do `kog shop pet` to buy them. Or Craft them!! (Temporarily Unavailable)", False]


def possible_evo(attr, stage):
    if attr == "Neutral":
        neutral = ap.get_all_Evo("Neutral", stage)
        fire = ap.get_all_Evo("Fire", stage)
        water = ap.get_all_Evo("Water", stage)
        earth = ap.get_all_Evo("Earth", stage)
        wind = ap.get_all_Evo("Wind", stage)
        electric = ap.get_all_Evo("Electric", stage)
        dark = ap.get_all_Evo("Dark", stage)
        plant = ap.get_all_Evo("Plant", stage)
        light = ap.get_all_Evo("Light", stage)
        list = neutral + fire + water + electric + dark + earth + wind + plant + light

    else:
        list = ap.get_all_Evo(attr, stage)

    return list
print(possible_evo("Light", "Ultimate"))

def get_name_attr(array):
    string = "**These are you possible Evolutions (Choose 1) :**\n"
    for i in array:
        print(i)
        attr = ap.get_attr(i)
        name = ap.get_name(i)
        string +=  f"`{name} | {attr}` "
    string += "\n**You have 30s**\n *ps. spell correctly or do `kog evolve <name>` again*"
    return string


def UpdateEvo(now, later, n):
    stage = ap.get_stage(later)
    attr = ap.get_attr(later)
    # hp = mp.max_hp_l(later, mp.get_level_l(now, n))
    # defense = mp.max_def_l(later, mp.get_level(now, n))
    # att = mp.max_att_l(later, mp.get_level(now, n))
    # `Atk` = '{att}', `Def` = '{defense}' ,`HP` = '{int(hp)}',
    print(stage, attr)

    link = ap.get_img(later)
    lvl = mp.get_level_l(now, n)
    cnx = db.cnx()
    cursor = cnx.cursor()
    query = f"UPDATE `kogrpg`.`mypets` SET `Equip Slots` = 'NONE' WHERE (`name` = '{n}');"
    cursor.execute(query)
    cnx.commit()
    cursor.close()

    cursor = cnx.cursor()
    query = f"UPDATE `kogrpg`.`mypets` SET `Stage` = '{stage}', `Attribute` = '{attr}', `pets` = '{later}', " \
            f"`Equip Slots` = 'Main Pet', `level` = '{lvl}', `Image link` = '{link}' WHERE (`pets` = '{now}');"
    cursor.execute(query)
    cnx.commit()
    cursor.close()
    cnx.close()
    return True
