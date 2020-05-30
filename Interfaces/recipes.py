import KoGDAO.craftDAO as c
import KoGDAO.itemDAO as itemDAO
import KoGDAO.userDAO as u
import db


def dictionary_of_all():
    Array = {}
    for i in c.all_craftables_name():
        print(i)
        Array[i] = {"emoji": itemDAO.get_item_emoji(i), "m1": c.get_material1(i),
                    "m1e":itemDAO.get_item_emoji(c.get_material1(i)), "q1": c.get_quantity1(i),
                    "m2": c.get_material2(i), "m2e": itemDAO.get_item_emoji(c.get_material2(i)),
                    "q2": c.get_quantity2(i)}
    return Array

print(dictionary_of_all())


def check_ifCraft(i, n):
    m1 = dictionary_of_all()[i]["m1"].lower()
    m2 = dictionary_of_all()[i]["m2"].lower()
    q1 = dictionary_of_all()[i]["q1"]
    q2 = dictionary_of_all()[i]["q2"]
    # print(u.get_items(n)[m1], "   ", q1, u.get_items(n)[m2], "   ", q2)
    if i in dictionary_of_all().keys():
        if m1 in u.get_items_names(n) and m2 in u.get_items_names(n):
            if q1 <= int(u.get_items(n)[m1]) and q2 <= int(u.get_items(n)[m2]):
                return "Yes"
            else:
                return "You dont have enough materials!"
        else:
            return "Dont have items."
    else:
        return "Did you spell cor-rightly?"

# print(check_ifCraft("Baby Core","OneForFourKay#5753"))

def craft(i, n):
    # try:
        emoji = dictionary_of_all()[i]["emoji"]
        m1 = dictionary_of_all()[i]["m1"].lower()
        m2 = dictionary_of_all()[i]["m2"].lower()
        q1 = int(dictionary_of_all()[i]["q1"])
        q2 = int(dictionary_of_all()[i]["q2"])
        numb1 = int(u.get_items(n)[m1]) - q1
        numb2 = int(u.get_items(n)[m2]) - q2
        t = itemDAO.get_type(i)
        # item update
        if i.lower() in u.get_items_names(n):
            cnx = db.cnx()
            cursor = cnx.cursor()
            query = f"UPDATE `kogrpg`.`inventory` SET `number` = '{numb2}' WHERE (`item` = '{m2.lower()}');"
            cursor.execute(query)
            cnx.commit()
            cursor.close()
            cnx.close()
        else:
            cnx = db.cnx()
            cursor = cnx.cursor()
            query = f"INSERT INTO `kogrpg`.`inventory` (`name`, `item`, `type`) VALUES ('{n}', '{i.lower()}', '{t}');"
            cursor.execute(query)
            cnx.commit()
            cursor.close()
            cnx.close()
        # m1 update
        cnx = db.cnx()
        cursor = cnx.cursor()
        query = f"UPDATE `kogrpg`.`inventory` SET `number` = '{numb1}' WHERE (`item` = '{m1.lower()}');"
        # print(query)
        cursor.execute(query)
        cnx.commit()
        cursor.close()
        cnx.close()
        # m2 update
        cnx = db.cnx()
        cursor = cnx.cursor()
        query = f"UPDATE `kogrpg`.`inventory` SET `number` = '{numb2}' WHERE (`item` = '{m2.lower()}');"
        cursor.execute(query)
        cnx.commit()
        cursor.close()
        cnx.close()
        return f"Succesfully crafted **{i}**  {emoji}"

    # except:
    #     return f"Failed to crafted **{i}**"
