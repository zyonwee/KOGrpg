import db
import KoGDAO.allPetsDAO as ap
import Casino.Arithemetics as ari
import KoGDAO.myPetsDAO as mp
stages = ["Baby", "In-Training", "Rookie", "Champion", "Ultimate", "Mega", "Ultra"]


def all_moves_attr_tier(attr, stage):  # index [0] 100%, [1] 60 %, [2] 40%
    cnx = db.cnx()
    cursor = cnx.cursor()
    query = f"SELECT * FROM moves WHERE (Attribute = '{attr}' and stage = '{stage}')"
    moves = []
    cursor.execute(query)
    for i in cursor:
        moves.append(i)
    cursor.close()
    cnx.close()
    return moves

# print(all_moves_attr_tier("light",6))


def get_m1(i):
    attr = ap.get_attr(i)
    stage = ap.get_stage(i)
    stage = stages.index(stage)
    # print("Stage :", stage)
    m1 = all_moves_attr_tier(attr, stage)
    return m1[0][0]
# print(get_m1("magnaange"))


def get_m2(i):
    attr = ap.get_attr(i)
    stage = ap.get_stage(i)
    stage = stages.index(stage)
    # print("Stage :", stage)
    m1 = all_moves_attr_tier(attr, stage)
    return m1[1][0]


def get_m3(i):
    attr = ap.get_attr(i)
    stage = ap.get_stage(i)
    stage = stages.index(stage)
    # print("Stage :", stage)
    m1 = all_moves_attr_tier(attr, stage)
    return m1[2][0]


def get_attack(moves, petname, n, lvl, o_main, opp):
    cnx = db.cnx()
    cursor = cnx.cursor()
    query = f"SELECT tier FROM moves WHERE (move = '{moves}')"
    moves = []
    cursor.execute(query)
    for i in cursor:
        moves.append(i)
    cursor.close()
    moves = moves[0][0]
    moves = get_hit_miss(moves)
    print(moves)
    if moves[0] == "hit":
        attack_dealt = int(mp.get_att_inc(petname, lvl, n)) * moves[1]
        if attack_dealt == 0:
            attack_dealt = 1
        mp.set_health(opp, o_main, attack_dealt)
        return f"{n}'s {petname} hit his attack with {attack_dealt} dmg"
    if moves[0] == "miss":
        return f"{n}'s {petname}  missed his attack."


def get_hit_miss(tier):
    if tier == 1:
        return ["hit", 1]
    if tier == 2:
        if ari.between(0, 100) >= 40:
            return ["hit", 2]
        else:
            return ["miss", 2]
    if tier == 3:
        if ari.between(0, 100) >= 60:
            return ["hit", 4]
        else:
            return ["miss", 4]
