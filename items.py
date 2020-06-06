import db
import random
from KoGDAO.allPetsDAO import get_allStage


def get_all_eggshop():
    names = []
    cnx = db.cnx()
    cursor = cnx.cursor()
    query = (f"SELECT * FROM items WHERE shop = 'egg'")
    cursor.execute(query)
    for i in cursor:
        names.append(i[1])
        # print(i[0])

    cursor.close()
    cnx.close()
    # print(names)
    return names

# print(get_all_eggshop())


def get_all_item_exist_name_lower():
    names = []
    cnx = db.cnx()
    cursor = cnx.cursor()
    query = (f"SELECT * FROM items")
    cursor.execute(query)
    for i in cursor:
        names.append(i[1].lower())
        # print(i[0])
    cursor.close()
    cnx.close()
    # print(names)
    return names


def get_all_monsters_exist_name_lower():
    names = []
    cnx = db.cnx()
    cursor = cnx.cursor()
    query = (f"SELECT * FROM monsters")
    cursor.execute(query)
    for i in cursor:
        names.append(i[0].lower())
        # print(i[0])
    cursor.close()
    cnx.close()
    # print(names)
    return names


def get_all_lootshop():
    names = []
    cnx = db.cnx()
    cursor = cnx.cursor()
    query = (f"SELECT * FROM items WHERE shop = 'lb' ORDER BY `id` ASC")
    cursor.execute(query)
    for i in cursor:
        names.append(i[1])
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

def get_all_petshop():
    names = []
    cnx = db.cnx()
    cursor = cnx.cursor()
    query = (f"SELECT * FROM items WHERE shop = 'pet' ORDER BY `id` ASC")
    cursor.execute(query)
    for i in cursor:
        names.append(i[1])
        # print(i[0])
    cursor.close()
    cnx.close()
    # print(names)
    return names


def random_pet(i):
    if i == "egg common":
        pets = random.choice(get_allStage("Baby"))
        return pets
    if i == "egg uncommon":
        pets = random.choice(get_allStage("In-Training"))
        return pets




# print(get_Equipped("OneForFourKay#5753"))
