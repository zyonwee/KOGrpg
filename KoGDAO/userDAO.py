import db
import KoGDAO.itemDAO as itemDAO
import items as item
import Casino.Arithemetics as ari


def set_cooldown(n, cooldown):
    d = str(ari.get_date_time())
    cnx = db.cnx()
    cursor = cnx.cursor()
    query = f"UPDATE `kogrpg`.`cooldowns` SET `{cooldown}` = '{d}' WHERE (`name` = '{n}')"
    cursor.execute(query)
    cnx.commit()
    cursor.close()
    cnx.close()


def set_minusone_day(n, cooldown):
    d = str(ari.get_date_time_minus_1())
    cnx = db.cnx()
    cursor = cnx.cursor()
    query = f"UPDATE `kogrpg`.`cooldowns` SET `{cooldown}` = '{d}' WHERE (`name` = '{n}')"
    cursor.execute(query)
    cnx.commit()
    cursor.close()
    cnx.close()

def get_stats(name):
    # print(name)
    cnx = db.cnx()
    cursor = cnx.cursor()
    query = (f"SELECT * FROM stats WHERE (`name` = '{name}')")
    stats = []
    cursor.execute(query)
    for i in cursor:
        stats.append(i)
    cursor.close()
    cnx.close()
    return stats[0]


def get_cooldowns(name):
    cnx = db.cnx()
    cursor = cnx.cursor()
    query = (f"SELECT * FROM cooldowns WHERE name = '{name}'")
    stats = {}
    cursor.execute(query)
    for (name, daily, hunt) in cursor:
        stats["daily"] = daily
        stats["hunt"] = hunt
    cursor.close()
    cnx.close()
    return stats

# print(get_cooldowns("OneForFourKay#5753"))


def clear():
    cnx = db.cnx()
    cursor = cnx.cursor()
    query = f"DELETE FROM `kogrpg`.`inventory` WHERE (`number` = '0')"
    stats = []
    cursor.execute(query)
    cnx.commit()
    cursor.close()
    cnx.close()
# clear()

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

# print(get_items("OneForFourKay#5753")["rare staff"])


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
    # print(n)
    coins = get_stats(n)[5]
    return str(coins)


def get_gem(n):
    gem = get_stats(n)[6]
    return str(gem)


def get_curr_xp(n):
    curr_xp = get_stats(n)[7]
    return str(curr_xp)


def get_max_xp(L):
    realm = round(L // 10)
    if realm == 0:
        realm = 1
    max_xp = (10 * L * L - 10 * L) + realm * 10
    return str(max_xp)


def get_progress(n):
    progress = str(round((int(get_curr_xp(n))/int(get_max_xp(int(get_level(n))))*100),2))
    return str(progress)


def get_level(n):
    level = get_stats(n)[9]
    return str(level)


def get_realm(n):
    realm = get_stats(n)[10]
    return str(realm)


def get_id(n):
    level = get_stats(n)[11]
    return str(level)


def get_fight_partner(n):
    fs = get_stats(n)[12]
    return str(fs)


def get_fight_status(n):
    fs = get_stats(n)[13]
    return str(fs)

# print(get_fight_status("OneForFourKay#5753"))


def get_turn_count(n):
    tc = get_stats(n)[14]
    return str(tc)


def get_fight_break(n):
    fb = get_stats(n)[15]
    return str(fb)


def get_name_by_id(id):
    print(id)
    cnx = db.cnx()
    cursor = cnx.cursor()
    query = f"SELECT * FROM stats WHERE id = '{id}'"
    id = []
    cursor.execute(query)
    for i in cursor:
        id.append(i)
    cursor.close()
    cnx.close()
    return id[0][0]


def set_hp(name, new_hp):
    cnx = db.cnx()
    cursor = cnx.cursor()
    query = f"UPDATE `kogrpg`.`stats` SET `curr_hp` = '{new_hp}' WHERE (`name` = '{name}');"
    cursor.execute(query)
    cnx.commit()
    cursor.close()
    cnx.close()
    return True


def set_fight_partner(name, string):
    cnx = db.cnx()
    cursor = cnx.cursor()
    query = f"UPDATE `kogrpg`.`stats` SET `fight_partner` = '{string}' WHERE (`name` = '{name}');"
    cursor.execute(query)
    cnx.commit()
    cursor.close()
    cnx.close()
    return True


def set_fight_status(name, string):
    cnx = db.cnx()
    cursor = cnx.cursor()
    query = f"UPDATE `kogrpg`.`stats` SET `fight_status` = '{string}' WHERE (`name` = '{name}');"
    cursor.execute(query)
    cnx.commit()
    cursor.close()
    cnx.close()
    return True


def set_fight_break(name, string):
    cnx = db.cnx()
    cursor = cnx.cursor()
    query = f"UPDATE `kogrpg`.`stats` SET `fight_break` = '{string}' WHERE (`name` = '{name}');"
    cursor.execute(query)
    cnx.commit()
    cursor.close()
    cnx.close()
    return True


def set_turncount_inc(name):
    string = int(get_turn_count(name))
    string += 1
    cnx = db.cnx()
    cursor = cnx.cursor()
    query = f"UPDATE `kogrpg`.`stats` SET `turn_count` = '{string}' WHERE (`name` = '{name}');"
    cursor.execute(query)
    cnx.commit()
    cursor.close()
    cnx.close()
    return True


def set_turncount_zero(name):
    cnx = db.cnx()
    cursor = cnx.cursor()
    query = f"UPDATE `kogrpg`.`stats` SET `turn_count` = '{0}' WHERE (`name` = '{name}');"
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
    # print(name)
    coins = int(get_coins(name)) + coins
    cnx = db.cnx()
    cursor = cnx.cursor()
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
    if itemDAO.get_shop(i) != "special":
        if int(itemDAO.get_price(i))*number < int(get_coins(n)):
            if t != "att" and t != "def":
                if t != "mat":
                    print(i, "bought")
                    new_coin = int(get_coins(n)) - int(itemDAO.get_price(i)) * number
                    cursor = cnx.cursor()
                    query = f"UPDATE `kogrpg`.`stats` SET `coins` = '{new_coin}' WHERE (`name` = '{n}');"
                    cursor.execute(query)
                    cnx.commit()
                    cursor.close()
                    increase_itembyNumber(i, n, number)
                    return "Yes"
                else:
                    return "Mat"

            elif i not in get_items(n).keys():
                new_coin = int(get_coins(n)) - int(itemDAO.get_price(i))
                cursor = cnx.cursor()
                query = f"UPDATE `kogrpg`.`stats` SET `coins` = '{new_coin}' WHERE (`name` = '{n}');"
                cursor.execute(query)
                cnx.commit()
                cursor.close()

                increase_itembyNumber(i, n, number)
                return "Tools"

            elif int(get_items(n)[i]) == 0:
                new_coin = int(get_coins(n)) - int(itemDAO.get_price(i))
                cursor = cnx.cursor()
                query = f"UPDATE `kogrpg`.`stats` SET `coins` = '{new_coin}' WHERE (`name` = '{n}');"
                cursor.execute(query)
                cnx.commit()
                cursor.close()

                increase_itembyNumber(i, n, number)
                return "Tools"

            else:
                return "Repeat"

        else:
            return "Poor"
    else:
        return "Special"


def sell(i, n, number):
    # print(get_items_names(n))
    if i in get_items_names(n):
        if number <= int(get_items(n)[i]):
            profit = (int(number)*int(itemDAO.get_price(i)))*0.8
            set_coins(n, profit)
            numb = int(get_items(n)[i]) - number
            cnx = db.cnx()
            cursor = cnx.cursor()
            query = f"UPDATE `kogrpg`.`inventory` SET `number` = '{numb}' WHERE (`item` = '{i}' and `name`='{n}');"
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
        query = f"UPDATE `kogrpg`.`inventory` SET `number` = '{numb}' WHERE (`item` = '{i}' and `name` = '{n}');"
        cursor.execute(query)
        cnx.commit()
        cursor.close()
        return True
    else:
        return False
# print(get_items("OneForFourKay#5753").keys())


def increase_itembyNumber(i, n, numb):
    numb = int(numb) # number to increase
    x = ""
    t = itemDAO.get_type(i)
    # print("numb = ", numb)
    try:
        current_item_count = int(get_items(n)[i])
    except KeyError:
        if i not in get_items_names(n):
            cnx = db.cnx()
            cursor = cnx.cursor()
            t = itemDAO.get_type(i)
            query = f"INSERT INTO `kogrpg`.`inventory` (`name`, `item`, `type`, `number`) VALUES ('{n}', '{i}', '{t}', '0');"
            cursor.execute(query)
            cnx.commit()
            cursor.close()
            cnx.close()
    current_item_count = int(get_items(n)[i])
    if t != "att" and t != "def":  # make sure item is not an equipment and in db
        # print("item is in keys going to update")
        i = i.lower()
        supposed_value = numb + current_item_count
        cnx = db.cnx()
        cursor = cnx.cursor()
        query = f"UPDATE `kogrpg`.`inventory` SET `number` = '{supposed_value}' WHERE (`item` = '{i}' and `name` = '{n}');"
        cursor.execute(query)
        cnx.commit()
        cursor.close()
        cnx.close()
        x += f"+ {numb} {itemDAO.get_item_emoji(i)} {i.title()}\n"
        return x
    if t == "att" and current_item_count == 0:  # make sure item is not an equipment and not in db
        # print("item is not in keys going to insert")
        i = i.lower()
        # print("item is in keys going to update")
        i = i.lower()
        cnx = db.cnx()
        cursor = cnx.cursor()
        query = f"UPDATE `kogrpg`.`inventory` SET `number` = '{1}' WHERE (`item` = '{i}' and `name` = '{n}');"
        cursor.execute(query)
        cnx.commit()
        cursor.close()
        cnx.close()
        x += f"+ {1} {itemDAO.get_item_emoji(i)} {i.title()}\n"
        return x
    if t == "def" and current_item_count == 0:  # make sure item is not an equipment and not in db
        # print("item is not in keys going to insert")
        i = i.lower()
        # print("item is in keys going to update")
        i = i.lower()
        cnx = db.cnx()
        cursor = cnx.cursor()
        query = f"UPDATE `kogrpg`.`inventory` SET `number` = '{1}' WHERE (`item` = '{i}' and `name` = '{n}');"
        cursor.execute(query)
        cnx.commit()
        cursor.close()
        cnx.close()
        x += f"+ {1} {itemDAO.get_item_emoji(i)} {i.title()}\n"
        return x
    else:
        return ""

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
            cnx = db.cnx()
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
        query = f"SELECT `item` FROM `kogrpg`.`inventory` WHERE (`type` = 'att' and `name` = '{n}' and `equip` = 'TRUE' and `number` = '1');"
        cursor.execute(query)
        for i in cursor:
            # print(i)
            e_array[0] = i[0]
        cursor.close()

        cnx = db.cnx()
        cursor = cnx.cursor()
        query = f"SELECT `item` FROM `kogrpg`.`inventory` WHERE (`type` = 'def' and `name` = '{n}' and `equip` = 'TRUE' and `number` = '1');"
        cursor.execute(query)

        for i in cursor:
            e_array[1] = i[0]
        cursor.close()

        return e_array


def pvp_pet_to_False(n, name_fight):
    set_fight_status(n, "False")
    set_fight_status(name_fight, "False")
    set_fight_partner(name_fight, "False")
    set_fight_partner(n, "False")
    set_turncount_zero(n)
    set_turncount_zero(name_fight)
    set_fight_break(name_fight, "A")
    set_fight_break(n, "A")

