import db
import KoGDAO.itemDAO as itemDAO
import items as item


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
    query = (f"SELECT * FROM inventory WHERE name = '{name}' ORDER BY type asc")
    items = {}
    cursor.execute(query)
    for (id, user, item, quantity, equip, type) in cursor:
        items[item] = str(quantity)
    cursor.close()
    cnx.close()
    return items

# print(get_items("OneForFourKay#5753")["stick"])


def get_items_names(name):
    array = []
    for i in get_items(name):
        array.append(i.lower())
    return array

# print(get_items_names("OneForFourKay#5753"))

def get_att(n):
    name_weapon = get_Equipped(n)[0]
    att = get_stats(n)[1] + 1 + 2 * (int(get_level(n)) - 1)
    if name_weapon:
        boosts = int(itemDAO.get_boosts(name_weapon))
        att += boosts
    return str(att)


def get_def(n):
    name_shield = get_Equipped(n)[1]
    defense = get_stats(n)[2] + 1 + 2*(int(get_level(n)) - 1)
    if name_shield:
        boosts = int(itemDAO.get_boosts(name_shield))
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
    progress = str(round((int(get_curr_xp(n))/int(get_max_hp(n))*100),2))
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
    coins = int(get_coins(name)) + coins
    query = f"UPDATE `kogrpg`.`stats` SET `coins` = '{coins}' WHERE (`name` = '{name}');"
    cursor.execute(query)
    cnx.commit()
    cursor.close()
    cnx.close()
    return True


def buy(i, n, number):
    t = itemDAO.get_type(i)
    # print(get_items(n).keys(), "      !", t)
    cnx = db.cnx()
    if int(itemDAO.get_price(i))*number < int(get_coins(n)):
        if t != "att" and t != "def":
            print(i, "bought")
            new_coin = int(get_coins(n)) - int(itemDAO.get_price(i)) * number
            cursor = cnx.cursor()
            query = f"UPDATE `kogrpg`.`stats` SET `coins` = '{new_coin}' WHERE (`name` = '{n}');"
            cursor.execute(query)
            cnx.commit()
            cursor.close()
            if i in get_items(n).keys():
                numb = number + int(get_items(n)[i])
                cursor = cnx.cursor()
                query = f"UPDATE `kogrpg`.`inventory` SET `name` = '{n}', `item` = '{i}', `number` = '{numb}' WHERE (`item` = '{i.lower()}');"
                cursor.execute(query)
                cnx.commit()
                cursor.close()
                cnx.close()
                return "Yes"
            else:
                numb = number
                cursor = cnx.cursor()
                query = f"INSERT INTO `kogrpg`.`inventory` (`name`, `item`, `type`, `number`) VALUES ('{n}', '{i}', '{t}', '{numb}');"
                cursor.execute(query)
                cnx.commit()
                cursor.close()
                cnx.close()
                return "Yes"
        elif i not in get_items(n).keys():
            new_coin = int(get_coins(n)) - int(itemDAO.get_price(i))
            cursor = cnx.cursor()
            query = f"UPDATE `kogrpg`.`stats` SET `coins` = '{new_coin}' WHERE (`name` = '{n}');"
            cursor.execute(query)
            cnx.commit()
            cursor.close()

            cursor = cnx.cursor()
            query = f"INSERT INTO `kogrpg`.`inventory` (`name`, `item`, `type`) VALUES ('{n}', '{i}', '{t}');"
            cursor.execute(query)
            cnx.commit()
            cursor.close()
            cnx.close()
            return "Tools"

        else:
            return "Repeat"

    else:
        return "Poor"


def sell(i, n, number):
    cnx = db.cnx()
    # print(get_items_names(n))
    if i in get_items_names(n):
        if number <= int(get_items(n)[i]):
            profit = (int(number)*int(itemDAO.get_price(i)))*0.8
            set_coins(n, profit)
            numb = int(get_items(n)[i]) - number
            cursor = cnx.cursor()
            query = f"UPDATE `kogrpg`.`inventory` SET `name` = '{n}', `item` = '{i}', `number` = '{numb}' WHERE (`item` = '{i}');"
            cursor.execute(query)
            cnx.commit()
            cursor.close()
            cnx.close()
            return ["Yes", abs(int(profit))]
        else:
            return ["You dont have enough of this item.", ""]
    else:
        return ["You dont have this item.", ""]



def decrease_item(i, n, number):
    user_items = get_items(n).keys()
    if i in user_items and int(get_items(n)[i]) != 0:
        numb = int(get_items(n)[i]) - number
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
    # print("numb = ", numb)
    try:
        now = int(get_items(n)[i.lower()])
        t = itemDAO.get_type(i)
    # print("now=", now)
    except:
        needsCheck = True
        now = 1
    x = ""
    if itemDAO.get_type(i) != "att" and itemDAO.get_type(i) != "def":
        i = i.lower()
        if i in get_items(n).keys():
            i = i.lower()
            numb += int(get_items(n)[i])
            cursor = cnx.cursor()
            query = f"UPDATE `kogrpg`.`inventory` SET `name` = '{n}', `item` = '{i}', `number` = '{numb}' WHERE (`item` = '{i}');"
            cursor.execute(query)
            cnx.commit()
            cursor.close()
            cnx.close()
            if numb == 0:
                x += ""
            else:
                numb -= now
                if numb == 0:
                    numb = 1
                x += f"+ {numb} {itemDAO.get_item_emoji(i)}\n"
            return x
        else:
            i = i.lower()
            cursor = cnx.cursor()
            t = itemDAO.get_type(i)
            query = f"INSERT INTO `kogrpg`.`inventory` (`name`, `item`, `type`) VALUES ('{n}', '{i}', '{t}');"
            cursor.execute(query)
            cnx.commit()
            cursor.close()
            cnx.close()
            if numb == 0:
                x += ""
            else:
                numb -= now
                if numb == 0:
                    numb = 1
                x += f"+ {numb} {itemDAO.get_item_emoji(i)}\n"
            return x
    if i.lower() not in get_items(n).keys():
        # print(i, "not in >", get_items(n).keys())
        t = itemDAO.get_type(i)
        i = i.lower()
        cursor = cnx.cursor()
        query = f"INSERT INTO `kogrpg`.`inventory` (`name`, `item`, `type`) VALUES ('{n}', '{i}', '{t}');"
        cursor.execute(query)
        cnx.commit()
        cursor.close()
        cnx.close()
        if numb == 0:
            x += ""
        else:
            x += f"+ {1} {itemDAO.get_item_emoji(i)}\n"
        return x
    else:
        x += ""
        return x


def equip(i, n):
    user_items = get_items(n).keys()
    t = itemDAO.get_type(i)

    if t == "att":
        if i in user_items and int(get_items(n)[i]) != 0:
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

    if t == "def":
        if i in user_items and int(get_items(n)[i]) != 0:
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
        e_array = [0, 0]
        query = f"SELECT `item` FROM `kogrpg`.`inventory` WHERE (`type` = 'att' and `name` = '{n}' and `equip` = 'TRUE');"
        cursor.execute(query)
        for i in cursor:
            # print(i)
            e_array[0] = i[0]
        cursor.close()

        cnx = db.cnx()
        cursor = cnx.cursor()
        query = f"SELECT `item` FROM `kogrpg`.`inventory` WHERE (`type` = 'def' and `name` = '{n}' and `equip` = 'TRUE');"
        cursor.execute(query)

        for i in cursor:
            e_array[1] = i[0]
        cursor.close()

        return e_array
