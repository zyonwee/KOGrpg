import csv

def get_allName():
    f = open("userInfo.csv", "r")
    reader = csv.reader(f)
    Users = {}
    users_array = []
    for row in reader:
        Users[row[0]] = {"att": row[1], "def": row[2], "curr_hp": row[3], "max_hp": row[4], "coins": row[5],
                         "gem": row[6], "curr_xp": row[7], "max_xp": row[8], "level": row[9]}
        users_array.append(row[0])
    print(users_array, Users)
    return users_array

def get_att(name):
    f = open("userInfo.csv", "r")
    reader = csv.reader(f)
    Users = {}
    users_array = []
    for row in reader:
        Users[row[0]] = {"att": row[1], "def": row[2], "curr_hp": row[3], "max_hp": row[4], "coins": row[5],
                         "gem": row[6], "curr_xp": row[7], "max_xp": row[8], "level": row[9]}
        users_array.append(row[0])
    att = str(Users[name]["att"])
    return att

def get_def(name):
    f = open("userInfo.csv", "r")
    reader = csv.reader(f)
    Users = {}
    users_array = []
    for row in reader:
        Users[row[0]] = {"att": row[1], "def": row[2], "curr_hp": row[3], "max_hp": row[4], "coins": row[5],
                         "gem": row[6], "curr_xp": row[7], "max_xp": row[8], "level": row[9]}
        users_array.append(row[2])
    defense = str(Users[name]["def"])
    return defense


def get_curr_hp(name):
    f = open("userInfo.csv", "r")
    reader = csv.reader(f)
    Users = {}
    users_array = []
    for row in reader:
        Users[row[0]] = {"att": row[1], "def": row[2], "curr_hp": row[3], "max_hp": row[4], "coins": row[5],
                         "gem": row[6], "curr_xp": row[7], "max_xp": row[8], "level": row[9]}
        users_array.append(row[3])
    curr_hp = str(Users[name]["curr_hp"])
    return curr_hp


def get_max_hp(name):
    f = open("userInfo.csv", "r")
    reader = csv.reader(f)
    Users = {}
    users_array = []
    for row in reader:
        Users[row[0]] = {"att": row[1], "def": row[2], "curr_hp": row[3], "max_hp": row[4], "coins": row[5],
                         "gem": row[6], "curr_xp": row[7], "max_xp": row[8], "level": row[9]}
        users_array.append(row[4])
    max_hp = str(Users[name]["max_hp"])
    return max_hp


def get_coins(name):
    f = open("userInfo.csv", "r")
    reader = csv.reader(f)
    Users = {}
    users_array = []
    for row in reader:
        Users[row[0]] = {"att": row[1], "def": row[2], "curr_hp": row[3], "max_hp": row[4], "coins": row[5],
                         "gem": row[6], "curr_xp": row[7], "max_xp": row[8], "level": row[9]}
        users_array.append(row[5])
    coins = str(Users[name]["coins"])
    return coins


def get_gem(name):
    f = open("userInfo.csv", "r")
    reader = csv.reader(f)
    Users = {}
    users_array = []
    for row in reader:
        Users[row[0]] = {"att": row[1], "def": row[2], "curr_hp": row[3], "max_hp": row[4], "coins": row[5],
                         "gem": row[6], "curr_xp": row[7], "max_xp": row[8], "level": row[9]}
        users_array.append(row[6])
    gem = str(Users[name]["gem"])
    return gem


def get_curr_xp(name):
    f = open("userInfo.csv", "r")
    reader = csv.reader(f)
    Users = {}
    users_array = []
    for row in reader:
        Users[row[0]] = {"att": row[1], "def": row[2], "curr_hp": row[3], "max_hp": row[4], "coins": row[5],
                         "gem": row[6], "curr_xp": row[7], "max_xp": row[8], "level": row[9]}
        users_array.append(row[7])
    curr_xp = str(Users[name]["curr_xp"])
    return curr_xp


def get_max_xp(name):
    f = open("userInfo.csv", "r")
    reader = csv.reader(f)
    Users = {}
    users_array = []
    for row in reader:
        Users[row[0]] = {"att": row[1], "def": row[2], "curr_hp": row[3], "max_hp": row[4], "coins": row[5],
                         "gem": row[6], "curr_xp": row[7], "max_xp": row[8], "level": row[9]}
        users_array.append(row[8])
    max_xp = str(Users[name]["max_xp"])
    return max_xp


def get_level(name):
    f = open("userInfo.csv", "r")
    reader = csv.reader(f)
    Users = {}
    users_array = []
    for row in reader:
        Users[row[0]] = {"att": row[1], "def": row[2], "curr_hp": row[3], "max_hp": row[4], "coins": row[5],
                         "gem": row[6], "curr_xp": row[7], "max_xp": row[8], "level": row[9]}
        users_array.append(row[9])
    print(Users[name]["level"])
    level = str(Users[name]["level"])
    return level

