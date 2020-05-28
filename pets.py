import db


def pet_info(name):
    cnx = db.cnx()
    cursor = cnx.cursor()
    query = (f"SELECT * FROM pets WHERE pets = '{name}'")
    stats = []
    cursor.execute(query)
    for i in cursor:
        stats.append(i)
    cursor.close()
    cnx.close()
    return stats[0]

# print(pet_info("kura"))



def get_allStage(n):
    names = []
    cnx = db.cnx()
    cursor = cnx.cursor()
    query = (f"SELECT * FROM pets WHERE Stage = '{n}'")

    cursor.execute(query)
    for i in cursor:
        names.append(i[0])
        # print(i[0])

    cursor.close()
    cnx.close()
    # print(names)
    return names


def get_stage(n):
    stage = pet_info(n)[2]
    return str(stage)


def get_attr(n):
    attr = pet_info(n)[4]
    return str(attr)


def get_hp(n):
    hp = pet_info(n)[7]
    return str(hp)


def get_att(n):
    att = pet_info(n)[9]
    return str(att)


def get_def(n):
    defense = pet_info(n)[10]
    return str(defense)


def get_img(n):
    img = pet_info(n)[13]
    return str(img)


def get_myPets(name):
    cnx = db.cnx()
    cursor = cnx.cursor()
    query = (f"SELECT * FROM mypets WHERE name = '{name}'")
    mypets = {}
    cursor.execute(query)
    for (Name, id, Stage, Type, Attribute, pets, Equip_Slots, HP, XP, Atk, Def, level, moves, Image_link) in cursor:
        mypets[pets] = {"level": level, "Image_link": Image_link, "pets": pets, "equip": Equip_Slots, "hp": HP,
                        "xp": XP, "att": Atk, "def": Def, "stage": Stage}
    cursor.close()
    cnx.close()
    return mypets


def max_hp(p, l):
    base_hp = int(get_hp(p))/50
    maxhp = base_hp * l
    return int(maxhp)





def increase_pet(i, n):
    cnx = db.cnx()
    if i in get_myPets(n).keys():
        return False
    else:
        attr = get_attr(i)
        stg = get_stage(i)
        link = get_img(i)
        cursor = cnx.cursor()
        hp = max_hp(i, 1)
        query = f"INSERT INTO `kogrpg`.`mypets` (`name`, `pets`, `HP` , `Attribute`, `Stage`, `Image link`) VALUES ('{n}','{i}', '{hp}','{attr}', '{stg}', '{link}');"
        print(query)
        cursor.execute(query)
        cnx.commit()
        cursor.close()
        cnx.close()
        setMain(i, n)
        return True


def setMain(p, n):
    stack = []
    for i in get_myPets(n).keys():
        stack.append(i.lower())
    if p in stack:
        cnx = db.cnx()
        cursor = cnx.cursor()
        query = f"UPDATE `kogrpg`.`mypets` SET `Equip Slots` = 'Side Pet' WHERE (`name` = '{n}');"
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
print(setMain("puni", "OneForFourKay#5753"))

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

