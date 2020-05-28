import random
import db


def get_monster(name):
    cnx = db.cnx()
    cursor = cnx.cursor()
    monster = []
    query = (f"SELECT * FROM monsters WHERE name = '{name}'")
    cursor.execute(query)
    for i in cursor:
        monster.append(i)
        # print(i[0])

    cursor.close()
    cnx.close()
    return monster[0]


def get_emoji(n):
    emoji = get_monster(n)[1]
    return str(emoji)


def get_level(n):
    level = get_monster(n)[2]
    return str(level)


def get_itemdrop(n):
    itemdrop = get_monster(n)[3]
    return str(itemdrop)


def get_desc(n):
    desc = get_monster(n)[4]
    return str(desc)


def get_chance(n):
    chance = get_monster(n)[5]
    return str(chance)
    

def get_coins(n):
    coins = get_monster(n)[6]
    return str(coins)


def get_att(n):
    att = get_monster(n)[7]
    return str(att)


def get_hp(n):
    hp = get_monster(n)[8]
    return str(hp)


def get_xp(n):
    xp = get_monster(n)[9]
    return str(xp)


def get_quantity(n):
    quantity = get_monster(n)[10]
    return str(quantity)


def chosen(level):
    cnx = db.cnx()
    cursor = cnx.cursor()
    monster = []
    query = (f"SELECT * FROM monsters WHERE level <= '{level}'")
    cursor.execute(query)
    for i in cursor:
        monster.append(i)
    cursor.close()
    cnx.close()
    number = random.randint(0, len(monster)-1)
    chosen = monster[number]
    return chosen[0]


def get_drops(name):
    if random.randint(1, int(get_chance(name))) == 1:
        quantity = random.randint(1, int(get_quantity(name)))
        drops = [str(quantity), str(get_itemdrop(name))]
        return drops
    else:
        return ["", "Hmm.. nothing here"]


def fight(chosen, att, defense, hp, max_hp, level):
    level = int(level)
    m_att = int(get_att(chosen)) + 2 * (level - 1)

    m_att = random.randint(round(m_att*0.5), round(m_att*1.5))

    m_hp = int(get_hp(chosen)) + 50 + 5 * (level - 1)
    m_hp_start = m_hp = random.randint(round(m_hp*0.5), round(m_hp*1.5))

    m_coins = int(get_coins(chosen))

    xp = int(get_xp(chosen))
    xp = random.randint(round(xp*0.5), round(xp*1.5))

    att = int(att)
    hp_start = hp = int(hp)
    defense = int(defense)
    counter_dealt = 0
    counter_taken = 0
    emoji = get_emoji(chosen)

    while m_hp > 0 and int(hp) > 0:
        m_hp -= att
        counter_taken += att
        if (m_att*2 - int(defense)) > 0:
            hp -= abs((m_att - int(defense)))
            counter_dealt += abs((m_att - int(defense)))
        print(m_hp, hp)
    if hp > 0:
        string = "Oh No! You loss **" + str(counter_dealt) + "** hp. You attacked with **" + str(m_hp_start) +\
                 "** dmg. \n:heart:  " + str(hp) + "/" + str(max_hp) + "\nCongrats! You Killed **" +\
                 chosen + emoji + "**"
        coins = random.randint(round(m_coins*0.8), round(m_coins*1.4))
        return [string, coins, xp, True, hp, chosen]

    if m_hp > 0:
        string = "Oh No! You loss " + str(hp_start) + " hp. You lost to **" + chosen +" "+ emoji + "**. Exp Reset :( "
        return [string, 0, 0, False, hp, chosen]







