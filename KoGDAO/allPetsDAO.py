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

def get_allattr(n):
    names = []
    cnx = db.cnx()
    cursor = cnx.cursor()
    query = (f"SELECT * FROM pets WHERE Attribute = '{n}'")

    cursor.execute(query)
    for i in cursor:
        names.append(i[0])
        # print(i[0])

    cursor.close()
    cnx.close()
    # print(names)
    return names


def get_allattr_stage(a, s):
    names = {}
    cnx = db.cnx()
    cursor = cnx.cursor()
    query = (f"SELECT * FROM pets WHERE Attribute = '{a}' and stage = '{s}'")
    cursor.execute(query)
    for i in cursor:
        names[i[0]] = i[4]
        # print(i[0])
    cursor.close()
    cnx.close()
    # print(names)
    return names

# print(get_allattr_stage("dark", "Champion"))

def get_all_Evo(attr, s):
    names = []
    cnx = db.cnx()
    cursor = cnx.cursor()
    query = (f"SELECT * FROM pets WHERE (Stage = '{s}' AND Attribute = '{attr}')")

    cursor.execute(query)
    for i in cursor:
        names.append(i[0])
        # print(i[0])

    cursor.close()
    cnx.close()
    # print(names)
    return names

# print(get_all_Evo("Fire", "Rookie"))


def get_stage(n):
    stage = pet_info(n)[2]
    return str(stage)


def get_name(n):
    stage = pet_info(n)[0]
    return str(stage)

# print(get_name("poyo"))

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



