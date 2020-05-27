import csv
import random


def get_monster(level):
    f = open("monsters.csv", "r")
    reader = csv.reader(f)
    monsterarray = []
    monster ={}
    for row in reader:
        monster[row[0]] = {"emoji":row[1], "level": row[2], "itemdrop": row[3], "desc": row[4], "chance": row[5],
                           "coins": row[6], "att": row[7], "hp": row[8], "xp": row[9], "quantity": row[10]}
        if int(monster[row[0]]["level"]) <= int(level):
            monsterarray.append(row[0])
    number = random.randint(0, len(monsterarray)-1)
    chosen = monsterarray[number]
    print(chosen, monsterarray)
    return chosen


def get_drops(name):
    f = open("monsters.csv", "r")
    reader = csv.reader(f)
    monster = {}
    for row in reader:
        monster[row[0]] = {"emoji":row[1], "level": row[2], "itemdrop": row[3], "desc": row[4], "chance": row[5],
                           "coins": row[6], "att": row[7], "hp": row[8], "xp": row[9],  "quantity": row[10]}
    if random.randint(1, int(monster[name]["chance"])) == 1:
        quantity = random.randint(1, int(monster[name]["quantity"]))
        drops = [quantity, monster[name]["itemdrop"]]
        return drops
    else:
        return "Hmm.. nothing here"


def fight(chosen, att, defense, hp, max_hp):
    f = open("monsters.csv", "r")
    reader = csv.reader(f)
    monster = {}
    for row in reader:
        monster[row[0]] = {"emoji":row[1], "level": row[2], "itemdrop": row[3], "desc": row[4], "chance": row[5],
                           "coins": row[6], "att": row[7], "hp": row[8], "xp": row[9],  "quantity": row[10]}
    m_att = int(monster[chosen]["att"])
    m_att = random.randint(round(m_att*0.8),round(m_att*1.1))
    m_hp = int(monster[chosen]["hp"])
    m_hp = random.randint(round(m_hp*0.8),round(m_hp*1.1))
    m_coins = int(monster[chosen]["coins"])
    xp =  int(monster[chosen]["xp"])
    xp = random.randint(round(xp*0.6),round(xp*1.1))
    att = int(att)
    hp = int(hp)
    defense = int(defense)
    counter_dealt = 0
    counter_taken = 0
    emoji = monster[chosen]["emoji"]
    while m_hp > 0 and int(hp) > 0:
        m_hp -= att
        counter_taken += att
        if (m_att - int(defense)) > 0:
            hp -= (m_att - int(defense))
            counter_dealt += (m_att - int(defense))
        print(m_att, m_hp)
        print(att, hp)

    if m_hp <= 0:
        string = "Oh No! You loss **" + str(counter_taken) + "** hp. You attacked with **" + str(counter_dealt) +\
                 "** dmg. \n:heart:  " + str(hp) + "/" + str(max_hp) + "\nCongrats! You Killed **" +\
                 chosen + monster[chosen]["emoji"] + "**"
        coins = random.randint(round(m_coins*0.8), round(m_coins*1.4))
        print(string, coins, xp)
        return [string, coins, xp, True, hp]
    if hp <= 0:
        string = "Oh No! You loss " + str(counter_taken) + " hp. You lost to " + chosen + ". Exp Reset :( "
        print(string)
        return [string, 0, 0, False]



