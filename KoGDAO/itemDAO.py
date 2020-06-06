import db


def get_stats(name):  # get stats of item
    cnx = db.cnx()
    cursor = cnx.cursor()
    query = (f"SELECT * FROM items WHERE name = '{name}'")
    stats = []
    cursor.execute(query)
    for i in cursor:
        stats.append(i)
        # print(i)
    # print(stats)
    cursor.close()
    cnx.close()
    return stats[0]
# print(get_stats())


def get_all_name_below_price(p, tier):  # get stats of item
    cnx = db.cnx()
    cursor = cnx.cursor()
    query = (f"SELECT * FROM items WHERE price < '{p}' and tier <= '{tier}'")
    stats = []
    cursor.execute(query)
    for i in cursor:
        stats.append(i[1])
        # print(i)
    # print(stats)
    cursor.close()
    cnx.close()
    return stats
# print(get_all_name_below_price(10000))


def get_item_emoji(n):
    emoji = get_stats(n)[2]
    return str(emoji)


def get_type(n):
    typed = get_stats(n)[3]
    return str(typed)


def get_desc(n):
    desc = get_stats(n)[4]
    return str(desc)


def get_price(n):
    price = get_stats(n)[5]
    return str(price)


def get_shop(n):
    shop = get_stats(n)[6]
    return str(shop)


def get_boosts(n):
    boosts = get_stats(n)[7]
    return str(boosts)

def get_tier(n):
    boosts = get_stats(n)[8]
    return str(boosts)
