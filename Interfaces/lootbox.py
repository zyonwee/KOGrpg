import db
import Casino.Arithemetics as ari
import KoGDAO.itemDAO as itemDao
import KoGDAO.userDAO as u


def open_common(n):
    item_n_number = {}
    string = ""
    all = itemDao.get_all_name_below_price(1000)
    for i in all:
        if ari.between_probs(0, 3) >= 50:
            item_n_number[i] = int(ari.between(1, 3))
        # if itemDao.get_type(i) != "att" and itemDao.get_type(i)!= "def":
        #     if item_n_number[i] != 0:
    for i in item_n_number.keys():

        print(i, n, item_n_number[i])
        string += u.increase_itembyNumber(i, n, item_n_number[i])
    u.decrease_item("lootbox", n, 1)
    if string == "":
        string += "Hey. You got nothing :("
    return string


def open_rare(n):
    item_n_number = {}
    string = ""
    all = itemDao.get_all_name_below_price(30000)
    for i in all:
        if ari.between_probs(0, 30) >= 2500:
            item_n_number[i] = int(ari.between(1, 2))
        # if itemDao.get_type(i) != "att" and itemDao.get_type(i)!= "def":
        #     if item_n_number[i] != 0:
    for i in item_n_number.keys():
        print(i, n, item_n_number[i])
        string += u.increase_itembyNumber(i, n, item_n_number[i])
    u.decrease_item("rare lootbox", n, 1)
    if string == "":
        string += "Hey. You got nothing :("
    return string
