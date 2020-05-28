import db
import stats as s
import pets as p
import random


def get_stats(name):  # get stats of item
    cnx = db.cnx()
    cursor = cnx.cursor()
    query = (f"SELECT * FROM items WHERE name = '{name}'")
    stats = []
    cursor.execute(query)
    for i in cursor:
        stats.append(i)
        # print(i)
    # print(stats)
    cursor.close()
    cnx.close()
    return stats[0]

print(get_stats("life potion"))


def get_item_emoji(n):
    emoji = get_stats(n)[2]
    return str(emoji)


def get_type(n):
    typed = get_stats(n)[3]
    return str(typed)


def get_desc(n):
    desc = get_stats(n)[4]
    return str(desc)


def get_price(n):
    price = get_stats(n)[5]
    return str(price)


def get_shop(n):
    shop = get_stats(n)[6]
    return str(shop)

def get_boosts(n):
    boosts = get_stats(n)[7]
    return str(boosts)


def get_all_eggshop():
    names = []
    cnx = db.cnx()
    cursor = cnx.cursor()
    query = (f"SELECT * FROM items WHERE shop = 'egg'")

    cursor.execute(query)
    for i in cursor:
        names.append(i[0])
        # print(i[0])

    cursor.close()
    cnx.close()
    # print(names)
    return names


def get_all_shop():
    names = []
    cnx = db.cnx()
    cursor = cnx.cursor()
    query = (f"SELECT * FROM items WHERE shop = 'basic' ORDER BY `id` ASC")

    cursor.execute(query)
    for i in cursor:
        names.append(i[1])
        # print(i[0])

    cursor.close()
    cnx.close()
    # print(names)
    return names




def buy(i, n):
    t = get_type(i)
    print(get_price(i), s.get_coins(n))
    cnx = db.cnx()
    if int(get_price(i)) < int(s.get_coins(n)):
        if t != ("att" or "def"):
            new_coin = int(s.get_coins(n)) - int(get_price(i))
            cursor = cnx.cursor()
            query = f"UPDATE `kogrpg`.`stats` SET `coins` = '{new_coin}' WHERE (`name` = '{n}');"
            cursor.execute(query)
            cnx.commit()
            cursor.close()
            t = get_type(i)
            if i in s.get_items(n).keys():
                numb = 1 + int(s.get_items(n)[i])
                cursor = cnx.cursor()
                query = f"UPDATE `kogrpg`.`inventory` SET `name` = '{n}', `item` = '{i}', `number` = '{numb}' WHERE (`item` = '{i}');"
                cursor.execute(query)
                cnx.commit()
                cursor.close()
                cnx.close()
                return "Yes"
            else:
                cursor = cnx.cursor()
                query = f"INSERT INTO `kogrpg`.`inventory` (`name`, `item`, `type`) VALUES ('{n}', '{i}', '{t}');"
                cursor.execute(query)
                cnx.commit()
                cursor.close()
                cnx.close()
                return "Yes"
        elif i not in s.get_items(n).keys():
            cursor = cnx.cursor()
            query = f"INSERT INTO `kogrpg`.`inventory` (`name`, `item`, `type`) VALUES ('{n}', '{i}', '{t}');"
            cursor.execute(query)
            cnx.commit()
            cursor.close()
            cnx.close()
            return "Yes"

        else:
            return "Repeat"

    else:
        return "Poor"


def decrease_item(i, n):
    user_items = s.get_items(n).keys()
    if i in user_items and s.get_items(n)[i] != 0:
        numb = int(s.get_items(n)[i]) - 1
        cnx = db.cnx()
        cursor = cnx.cursor()
        query = f"UPDATE `kogrpg`.`inventory` SET `name` = '{n}', `item` = '{i}', `number` = '{numb}' WHERE (`item` = '{i}');"
        cursor.execute(query)
        cnx.commit()
        cursor.close()
        return True
    else:
        return False


def increase_itembyNumber(i,n, numb):
    cnx = db.cnx()
    numb = int(numb)
    if i in s.get_items(n).keys():
        numb += int(s.get_items(n)[i])
        cursor = cnx.cursor()
        query = f"UPDATE `kogrpg`.`inventory` SET `name` = '{n}', `item` = '{i}', `number` = '{numb}' WHERE (`item` = '{i}');"
        cursor.execute(query)
        cnx.commit()
        cursor.close()
        cnx.close()
    else:
        cursor = cnx.cursor()
        query = f"INSERT INTO `kogrpg`.`inventory` (`name`, `item`, `number`) VALUES ('{n}', '{i}', '{numb}');"
        cursor.execute(query)
        cnx.commit()
        cursor.close()
        cnx.close()


def random_pet(i):
    if i == "egg common":
        pets = random.choice(p.get_allStage("Baby"))
        return pets
    if i == "egg uncommon":
        pets = random.choice(p.get_allStage("In-Training"))
        return pets


def equip(i, n):
    user_items = s.get_items(n).keys()
    typ = get_type(i)

    if typ == "att":
        if i in user_items and s.get_items(n)[i] != 0:

            cnx = db.cnx()

            cursor = cnx.cursor()
            query = f"UPDATE `kogrpg`.`inventory` SET `equip` = 'FALSE' WHERE (`type` = 'att');"
            cursor.execute(query)
            cnx.commit()
            cursor.close()

            cursor = cnx.cursor()
            query = f"UPDATE `kogrpg`.`inventory` SET `equip` = 'TRUE' WHERE (`item` = '{i}');"
            cursor.execute(query)
            cnx.commit()
            cursor.close()
            return True
        else:
            return False

    if typ == "def":
        if i in user_items and s.get_items(n)[i] != 0:
            cnx = db.cnx()

            cursor = cnx.cursor()
            query = f"UPDATE `kogrpg`.`inventory` SET `equip` = 'FALSE' WHERE (`type` = 'def');"
            cursor.execute(query)
            cnx.commit()
            cursor.close()

            cnx = db.cnx()
            cursor = cnx.cursor()
            query = f"UPDATE `kogrpg`.`inventory` SET `equip` = 'TRUE' WHERE (`item` = '{i}');"
            cursor.execute(query)
            cnx.commit()
            cursor.close()
            return True
        else:
            return False

def get_Equipped(n):
        cnx = db.cnx()
        cursor = cnx.cursor()
        estack = [0, 0]
        query = f"SELECT `item` FROM `kogrpg`.`inventory` WHERE (`type` = 'att' and `name` = '{n}' and `equip` = 'TRUE');"
        cursor.execute(query)
        for i in cursor:
            print(i)
            estack[0] = i[0]
        cursor.close()

        cnx = db.cnx()
        cursor = cnx.cursor()
        query = f"SELECT `item` FROM `kogrpg`.`inventory` WHERE (`type` = 'def' and `name` = '{n}' and `equip` = 'TRUE');"
        cursor.execute(query)

        for i in cursor:
            estack[1] = i[0]
        cursor.close()

        return estack

print(get_Equipped("OneForFourKay#5753"))
