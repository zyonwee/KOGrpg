import db
import KoGDAO.allPetsDAO as ap


def get_myPets(name):
    query = f"SELECT * FROM mypets WHERE name = '{name}' ORDER BY `Equip Slots` ASC"
    mypets = {}
    cnx = db.cnx()
    cursor = cnx.cursor()
    cursor.execute(query)
    for (Name, id, Stage, Type, attr, pets, Equip_Slots, HP, XP, Atk, Def, level, moves, Image_link) in cursor:
        mypets[pets] = {"level": level, "Image_link": Image_link, "pets": pets, "equip": Equip_Slots, "hp": HP,
                        "xp": XP, "att": Atk, "def": Def, "stage": Stage, "attr": attr}
    cursor.close()
    cnx.close()
    return mypets


def get_curr_xp(p, n):
    pet = get_myPets(n)
    currxp = pet[p]["xp"]
    return str(currxp)


def get_level(p, n):
    pet = get_myPets(n)
    level = pet[p]["level"]
    return str(level)


def get_stage(p, n):
    pet = get_myPets(n)
    level = pet[p]["stage"]
    return str(level)


def get_progress_xp(p, n):
    pet = get_myPets(n)
    level = pet[p]["level"]
    progress = round(int(get_curr_xp(p,n))/int(get_max_xp(p, n, level))*100, 2)
    print(progress)
    return str(progress)


def get_max_xp(p, n, L):
    pet = get_myPets(n)
    realm = round(L // 10)
    if realm == 0:
        realm = 1
    max_xp = (10 * L * L - 10 * L) + realm * 10
    return str(max_xp)


def max_hp(p, l):
    base_hp = round(int(ap.get_hp(p))/50)
    maxhp = base_hp * l
    return str(maxhp)


def max_def(p, l):
    base_hp = round(int(ap.get_hp(p))/50)
    maxhp = base_hp * l
    return str(maxhp)


def max_att(p, l):
    base_hp = round(int(ap.get_hp(p))/50)
    maxhp = base_hp * l
    return str(maxhp)




def get_att_inc(petname, l, n):  # Actual
    pet = get_myPets(n)
    base_att = round(int(ap.get_att(petname))/50) * l + pet[petname]["att"]

    return str(base_att)


def get_def_inc(petname, l, n):  # Actual
    pet = get_myPets(n)
    base_def = round(int(ap.get_def(petname))/50) * l + pet[petname]["def"]
    return str(base_def)
