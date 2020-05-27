import csv


def get_item_emoji(name):
    f = open("items.csv", "r")
    reader = csv.reader(f)
    item = {}
    for row in reader:
        item[row[0]] = {"emoji": row[1], "type": row[2], "desc": row[3], "price":row[4], "shop":row[5]}
    emoji = item[name]["emoji"]
    return emoji

def get_type(name):
    f = open("items.csv", "r")
    reader = csv.reader(f)
    item = {}
    for row in reader:
        item[row[0]] = {"emoji": row[1], "type": row[2], "desc": row[3], "price":row[4], "shop":row[5]}
    type = str(item[name]["type"])
    return type


def get_desc(name):
    f = open("items.csv", "r")
    reader = csv.reader(f)
    item = {}
    for row in reader:
        item[row[0]] = {"emoji": row[1], "type": row[2], "desc": row[3], "price":row[4], "shop":row[5]}
    desc = str(item[name]["desc"])
    return desc


def get_price(name):
    f = open("items.csv", "r")
    reader = csv.reader(f)
    item = {}
    for row in reader:
        item[row[0]] = {"emoji": row[1], "type": row[2], "desc": row[3], "price":row[4], "shop":row[5]}
    price = str(item[name]["price"])
    return price


def get_shop(name):
    f = open("items.csv", "r")
    reader = csv.reader(f)
    item = {}
    for row in reader:
        item[row[0]] = {"emoji": row[1], "type": row[2], "desc": row[3], "price":row[4], "shop":row[5]}
    shop = str(item[name]["shop"])
    return shop


def get_all_shop():
    f = open("items.csv", "r")
    reader = csv.reader(f)
    item = {}
    item_array = []
    for row in reader:
        item[row[0]] = {"emoji": row[1], "type": row[2], "desc": row[3], "price":row[4], "shop":row[5]}
        if item[row[0]]["shop"] == "basic":
            item_array.append(row[0])
    shop = item_array
    # print(shop)
    return shop
# get_all_shop()

