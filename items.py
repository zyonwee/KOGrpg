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

# print(get_stats("life potion")[1])


def get_item_emoji(n):
    emoji = get_stats(n)[1]
    return str(emoji)
    return emoji


def get_type(n):
    typed = get_stats(n)[2]
    return str(typed)
    return typed


def get_desc(n):
    desc = get_stats(n)[3]
    return str(desc)
    return desc


def get_price(n):
    price = get_stats(n)[4]
    return str(price)
    return price


def get_shop(n):
    shop = get_stats(n)[5]
    return str(shop)
    return shop


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
    query = (f"SELECT * FROM items WHERE shop = 'basic'")

    cursor.execute(query)
    for i in cursor:
        names.append(i[0])
        # print(i[0])

    cursor.close()
    cnx.close()
    # print(names)
    return names


def check_buy(i, n):
    print(get_price(i), s.get_coins(n))
    if get_price(i) < s.get_coins(n):
        return True
    return False


def buy(i, n):
    new_coin = int(s.get_coins(n)) - int(get_price(i))
    cnx = db.cnx()
    cursor = cnx.cursor()
    query = f"UPDATE `kogrpg`.`stats` SET `coins` = '{new_coin}' WHERE (`name` = '{n}');"
    cursor.execute(query)
    cnx.commit()
    cursor.close()

    if i in s.get_items(n).keys():
        numb = 1 + int(s.get_items(n)[i])
        cursor = cnx.cursor()
        query = f"UPDATE `kogrpg`.`inventory` SET `name` = '{n}', `item` = '{i}', `number` = '{numb}' WHERE (`item` = '{i}');"
        cursor.execute(query)
        cnx.commit()
        cursor.close()
        cnx.close()
    else:
        cursor = cnx.cursor()
        query = f"INSERT INTO `kogrpg`.`inventory` (`name`, `item`) VALUES ('{n}', '{i}');"
        cursor.execute(query)
        cnx.commit()
        cursor.close()
        cnx.close()


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

