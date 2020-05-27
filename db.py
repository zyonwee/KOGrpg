import mysql.connector


def cnx():
    cnx = mysql.connector.connect(user='kogrpg', password='rom122',
                                  host='127.0.0.1',
                                  database='kogrpg',auth_plugin='mysql_native_password')
    return cnx
# cursor = cnx.cursor()
#
# query = ("SELECT name FROM stats")
#
# cursor.execute(query)
#
# for i in cursor:
#   print(i)
#
# cursor.close()
# cnx.close()

