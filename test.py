import csv
f = open("stats/userInfo.csv", "r")

reader = csv.reader(f)
Users = {}
for row in reader:
    Users[row[0]] = {"att":row[1], "def":row[2], "curr_hp":row[3], "max_hp":row[4]}
    print(Users["twoForFourKay#5753"])

    print(row[0])
# f = open("stats/userInfo.csv", "r")
# count = 0
# rl = f.readlines()
# for line in rl:
#     count += 1
#     print("Line{} > {}".format(count, line.strip()))
#     print()


