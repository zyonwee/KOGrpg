import db


def all_craftables_name():
    cnx = db.cnx()
    cursor = cnx.cursor()
    query = (f"SELECT * FROM craft ORDER BY `id` ASC")
    stats = []
    cursor.execute(query)
    for i in cursor:
        stats.append(i[1])
    cursor.close()
    cnx.close()
    return stats

# print(all_craftables_name())

def all_craftables_stats():
    cnx = db.cnx()
    cursor = cnx.cursor()
    query = (f"SELECT * FROM craft ORDER BY `id` ASC")
    stats = []
    cursor.execute(query)
    for i in cursor:
        stats.append(i)
    cursor.close()
    cnx.close()
    return stats


def single_craftables_stats(n):
    cnx = db.cnx()
    cursor = cnx.cursor()
    query = (f"SELECT * FROM craft WHERE name = '{n}'")
    stats = []
    cursor.execute(query)
    for i in cursor:
        stats.append(i)
    cursor.close()
    cnx.close()
    return stats[0]

print(single_craftables_stats("Baby Core"))

def get_material1(n):
    m1 = single_craftables_stats(n)[2]
    return m1

# print(get_material1("Baby Core"))

def get_material2(n):
    m1 = single_craftables_stats(n)[4]
    return m1


def get_quantity1(n):
    m1 = single_craftables_stats(n)[3]
    return m1


def get_quantity2(n):
    m1 = single_craftables_stats(n)[5]
    return m1
