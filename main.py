import asyncio
import discord
import db
import monsters as mon
from Interfaces import pets as p, stats as s, queries as q, recipes as r, lootbox as lb
import items as item
import KoGDAO.allPetsDAO as ap
import KoGDAO.myPetsDAO as mp
import KoGDAO.userDAO as u
import KoGDAO.itemDAO as itemDAO
import Casino.coinflip as cf
import Casino.Arithemetics as ari
cnx = db.cnx()
client = discord.Client()
fixed_queries = ["interface", "action", "pet", "pets", "casino", "shop"]
stages = ["Baby", "In-Training", "Rookie", "Champion", "Ultimate", "Mega", "Ultra"]

@client.event
async def on_message(message):
    message.content = message.content.lower()
    n = str(message.author).strip()
    if message.author == client.user:
        return
    # new gamer
    if message.content.startswith("kog"):
        new = s.check_player_new(n)
        if new:
            if message.content == "kog":
                if new:
                    cursor = cnx.cursor()
                    query = (f"INSERT INTO `kogrpg`.`stats` (`name`) VALUES ('{n}')")
                    cursor.execute(query)
                    cnx.commit()
                    cursor.close()
                    cnx.close()
                    await message.channel.send("Welcome New Player :baby: !! :dove: **" + str(message.author)[:-5].title() + "**" +
                                               "\n Do `kog p` or `kog profile` to see your profile! :D\n `kog help` for Basic Commnands")
                else:
                    await message.channel.send("Shalom !! :dove: **" + str(message.author)[:-5].title() + "**\n`kog help` for Basic Commnands")
            else:
                await message.channel.send("Shalom !! Type `kog` to create an account :dove:")

        else:
            if message.content == "kog":
                    await message.channel.send("Shalom !! :dove: **" + str(message.author)[:-5].title() + "**\n`kog help` for Basic Commnands")


            # profile
            if message.content == "kog p" or message.content == "kog profile":
                embed = discord.Embed(title=str(message.author)[:-5].title() + "'s Profile",
                                      description="Title : Noobie \nTrainer's Level : " + u.get_level(n) + " (" + u.get_progress(n) + "%)"
                                                  + "\nRealm : " + u.get_realm(n)
                                                  + "\nXp : " + u.get_curr_xp(n) + "/" + u.get_max_xp(n)
                                                  + "\n:heart: " + u.get_curr_hp(n) + "/" + u.get_max_hp(n))
                embed.add_field(name="Stats", value=":crossed_swords: **" + u.get_att(n) + "** \n\n:shield: **" +
                                                    u.get_def(n) + "**")

                equipment = u.get_Equipped(n)
                string = ""
                if equipment[0] or equipment[1]:
                    if equipment[0]:
                        att = itemDAO.get_boosts(equipment[0])
                        string += itemDAO.get_item_emoji(equipment[0]) + f" [ Effects **+ {att} ATT** ]\n\n"

                    if equipment[1]:
                        defense = itemDAO.get_boosts(equipment[1])
                        string += itemDAO.get_item_emoji(equipment[1]) + f" [ Effects **+ {defense} DEF** ]\n"
                    embed.add_field(name="Equipment", value=string)
                else:
                    embed.add_field(name="Equipment", value="[NONE]")
                pet = p.getMain_Name(n)
                if pet:
                    print(pet)
                    m_pet = mp.get_myPets(n)[pet]
                    lvl = m_pet["level"]
                    hp = m_pet["hp"]
                    stage = m_pet["stage"]
                    max_hp = mp.max_hp(pet, lvl)
                    embed.add_field(name="Main Pet", value=f"**{pet}** *[{stage}]*\n**Level: {lvl}**\n:heart: **{hp}/{max_hp}**")
                    embed.set_thumbnail(url=p.getMain(n))
                embed.add_field(name="Bank", value= f":moneybag: **" + u.get_coins(n) + "** :comet: **" + u.get_gem(n) + "**", inline=False)
                embed.color = discord.Color(0xfdfd96)
                embed.set_footer(text = "Try doing <kog inv> to see all items you have!")
                await message.channel.send(content=None, embed=embed)



            # shop
            if message.content == ("kog shop egg"):
                embed = discord.Embed(title="Welcome to Egg Shop", description="A shop for all your Pets Eggs `kog buy <name>`")
                for i in item.get_all_eggshop():
                    # print(i, item.get_all_eggshop())
                    emoji = itemDAO.get_item_emoji(i)
                    desc = itemDAO.get_desc(i)
                    price = itemDAO.get_price(i)
                    embed.add_field(name=str(i).title(), value=f"{emoji}{desc}\n\n:moneybag: {price}\n")
                embed.set_thumbnail(url=p.getMain(n))
                embed.color = discord.Color(0xd4af37)
                await message.channel.send(content=None, embed=embed)

            if message.content == ("kog shop pet"):
                embed = discord.Embed(title="Welcome to Egg Shop", description="A shop for all your Pets Eggs `kog buy <name>`")
                for i in item.get_all_petshop():
                    # print(i, item.get_all_eggshop())
                    emoji = itemDAO.get_item_emoji(i)
                    desc = itemDAO.get_desc(i)
                    price = itemDAO.get_price(i)
                    embed.add_field(name=str(i).title(), value=f"{emoji}{desc}\n\n:moneybag: {price}\n")
                embed.set_thumbnail(url=p.getMain(n))
                embed.color = discord.Color(0xd4af37)
                await message.channel.send(content=None, embed=embed)

            if message.content == "kog shop lootbox" or message.content == "kog shop lb":
                embed = discord.Embed(title="Welcome to LootBox Shop", description="Let the looting RAVE begin!")
                for i in item.get_all_lootshop():
                    emoji = itemDAO.get_item_emoji(i)
                    desc = itemDAO.get_desc(i)
                    price = itemDAO.get_price(i)
                    embed.add_field(name=str(i).title(), value=f"{emoji}{desc}\n\n:moneybag: {price}\n")
                embed.set_thumbnail(url=p.getMain(n))
                embed.color = discord.Color(0xd4af37)
                await message.channel.send(content=None, embed=embed)

            if message.content == ("kog shop"):
                embed = discord.Embed(title="Welcome to Basic Shop", description="A shop for all your Basic Eggs `kog buy <name>`")
                embed.add_field(name="Other Shops", value=f"`kog shop egg` `kog shop pet` `kog shop lb`", inline=False)
                for i in item.get_all_shop():
                    # print(item.get_all_shop(), i)
                    emoji = itemDAO.get_item_emoji(i)
                    desc = itemDAO.get_desc(i)
                    price = itemDAO.get_price(i)
                    embed.set_thumbnail(url=p.getMain(n))
                    embed.add_field(name=str(i).title(), value=f"{emoji} {desc}\n:moneybag: {price}", inline=False)

                embed.color = discord.Color(0xEDDDDD)
                embed.set_thumbnail(url=p.getMain(n))
                await message.channel.send(content=None, embed=embed)


            # help
            if message.content == "kog help" or message.content == "kog ?":
                embed = discord.Embed(title="Welcome to KoGrpg Help", description="Listed are some basic Commands \n`kog help <specifics>`")
                embed.add_field(name="Interfacing Commands", value="`kog help interface`", inline=False)
                embed.add_field(name="Action Commands", value="`kog help action`", inline=False)
                embed.add_field(name="Shop Commands", value="`kog help shop`", inline=False)
                embed.add_field(name="Pets Commands", value="`kog help pets`", inline=False)
                embed.add_field(name="Casino Commands", value="`kog help casino`", inline=False)
                embed.color = discord.Color(0xEDDDDD)
                embed.set_thumbnail(url=p.getMain(n))
                await message.channel.send(content=None, embed=embed)

            if message.content == "kog help interface":
                embed = discord.Embed(title="Welcome to KoGrpg Help Interface", description="Listed are some basic Commands \n`kog help <specifics>`")
                h = q.list_help("interface")
                embed.add_field(name="Interface Commands", value=h, inline=False)
                embed.color = discord.Color(0xEDDDDD)
                embed.set_thumbnail(url=p.getMain(n))
                await message.channel.send(content=None, embed=embed)

            if message.content == "kog help action" or message.content == "kog help actions":
                embed = discord.Embed(title="Welcome to KoGrpg Help Action", description="Listed are some basic Commands \n`kog help <specifics>`")
                h = q.list_help("action")
                embed.add_field(name="Action Commands", value=h, inline=False)
                embed.color = discord.Color(0xEDDDDD)
                embed.set_thumbnail(url=p.getMain(n))
                await message.channel.send(content=None, embed=embed)

            if message.content == "kog help shop":
                embed = discord.Embed(title="Welcome to KoGrpg Help Shop", description="Listed are some basic Commands \n`kog help <specifics>`")
                h = q.list_help("shop")
                embed.add_field(name="Shop Commands", value=h, inline=False)
                embed.color = discord.Color(0xEDDDDD)
                embed.set_thumbnail(url=p.getMain(n))
                await message.channel.send(content=None, embed=embed)

            if message.content == "kog help pets" or message.content == "kog help pet":
                embed = discord.Embed(title="Welcome to KoGrpg Help Pets", description="Listed are some basic Commands \n`kog help <specifics>`")
                h = q.list_help("pet")
                embed.add_field(name="Pets Commands", value=h, inline=False)
                embed.color = discord.Color(0xEDDDDD)
                embed.set_thumbnail(url=p.getMain(n))
                await message.channel.send(content=None, embed=embed)

            if message.content == "kog help casino":
                embed = discord.Embed(title="Welcome to KoGrpg Help", description="Listed are some basic Commands \n`kog help <specifics>`")
                h = q.list_help("casino")
                embed.add_field(name="Casino Commands", value=h, inline=False)
                embed.color = discord.Color(0xEDDDDD)
                embed.set_thumbnail(url=p.getMain(n))
                await message.channel.send(content=None, embed=embed)

            if message.content.startswith("kog help "):
                h = message.content[9:].lower()
                if h not in fixed_queries:
                    print(h)
                    h = q.list_help(h)
                    await message.channel.send(content=h)


            # hunt
            if message.content.startswith("kog hunt"):
                result = mon.fight(mon.chosen(u.get_level(n)), u.get_att(n), u.get_def(n), u.get_curr_hp(n), u.get_max_hp(n),
                                   u.get_level(n), n)

                if 7 == ari.between(0, 60):
                    u.increase_itembyNumber("lootbox", n, 1)
                    embed = discord.Embed(title="Congratulations!", description=f"You picked up a lootbox")
                    embed.set_thumbnail(url=p.getMain(n))
                    embed.color = discord.Color(0xFFB6C1)
                    embed.set_footer(text = "do <kog use lootbox> to use it!")
                    await message.channel.send(content=None, embed=embed)

                if 7 == ari.between(0, 500):
                    u.increase_itembyNumber("rare lootbox", n, 1)
                    embed = discord.Embed(title="Congratulations!", description=f"You picked up a rare lootbox")
                    embed.set_thumbnail(url=p.getMain(n))
                    embed.color = discord.Color(0xFFB6C1)
                    embed.set_footer(text = "do <kog use rare lootbox> to use it!")
                    await message.channel.send(content=None, embed=embed)

                if result[3]:
                    u.set_hp(n, result[4])
                    u.set_xp(n, result[2])
                    u.set_coins(n, result[1])
                    coins = str(result[1])
                    b = s.check_level(n)

                    drops = mon.get_drops(result[5])
                    print(drops, "These are the drops")
                    if drops[1] == "Hmm.. nothing here":
                        if b:
                            await message.channel.send(content=result[0] + "\n" + drops[1] + ". Earned **" +
                                                               str(result[2]) + "xp**, :moneybag:**" + coins +
                                                               "**\nCongatulations, you Leveled Up ! +2 :crossed_swords: +2 :shield:")
                        else:
                            await message.channel.send(
                                content=result[0] + "\n" + drops[1] + ". Earned **" + str(result[2]) + "xp**, :moneybag:**" + coins + "**")
                    else:
                        if b:
                            u.increase_itembyNumber(drops[1], n, drops[0])
                            await message.channel.send(content=result[0] + "\nYou've Obtained **" + drops[0] + " " + drops[1]
                                                        + "**" + " and Earned **" + str(result[2])
                                                        + "xp**, :moneybag:**" + coins
                                                        + "**\nCongatulations, you Leveled Up ! +2 :crossed_swords: +2 :shield:")
                        else:
                            u.increase_itembyNumber(drops[1], n, drops[0])
                            await message.channel.send(content=result[0] + "\nYou've Obtained **" + drops[0] + " " + drops[1]
                                                        + "**" + " and Earned **" + str(result[2]) + "xp**, :moneybag:**" + coins + "**")

                else:
                    s.you_died(n)
                    s.heal(n)
                    await message.channel.send(content=result[0])


            # heal
            if message.content.startswith("kog heal"):
                try:
                    item_desired = "life potion"
                    if itemDAO.get_type(item_desired) == "hp" and int(u.get_items(n)[item_desired]) != 0 :
                        s.heal(n)
                        u.decrease_item(item_desired, n, 1)
                        await message.channel.send(content="Your health is restored to full, 1 <:lifepotion:715245405918593207> consumed.")
                    else:
                        await message.channel.send(content="You go buy a potion la. You got none.")
                except:
                    await message.channel.send(content="Sure bo you got potion? Go `kog shop`")


            # buy
            if message.content.startswith("kog buy "):
                item_desired = message.content[8:].lower()
                number = 0
                count = 0
                tmp_n = ""
                tmp_s = ""
                try:
                    for i in item_desired:
                        if i.isnumeric():
                            tmp_n += str(i)
                            count += 1
                        else:
                            tmp_s += i
                    if int(tmp_n) > 0:
                        item_desired = str(tmp_s)[1:]
                        number = int(tmp_n)
                except:
                    number = 1
                print(str(number) +"\n"+ item_desired)
                try:
                    string = u.buy(item_desired, n, number)
                    if string == "Yes":
                        await message.channel.send(content=f"Successfully bought **{number} {item_desired}** {itemDAO.get_item_emoji(item_desired)}")
                    if string == "Tools":
                        await message.channel.send(content=f"Successfully bought **1 {item_desired}** {itemDAO.get_item_emoji(item_desired)}")
                    if string == "Repeat":
                        await message.channel.send(content=f"You Already have the equipment **{item_desired}** {itemDAO.get_item_emoji(item_desired)}")
                    if string == "Poor":
                        await message.channel.send(content="You too poor la. **LMAO**")
                    if string == "Mat":
                        await message.channel.send(content="You cant buy a monster's parts dummi !")
                    if string == "Special":
                        await message.channel.send(content="Dummy, you thought there was a bug didnt you? Welps you cant buy special items ! !")
                except:
                    await message.channel.send(content="Check your spelling MeEstER!")

            # sell
            if message.content.startswith("kog sell "):
                item_desired = message.content[9:].lower()
                number = 0
                count = 0
                tmp_n = ""
                tmp_s = ""
                try:
                    for i in item_desired:
                        if i.isnumeric():
                            tmp_n += str(i)
                            count += 1
                        else:
                            tmp_s += i
                    if int(tmp_n) > 0:
                        print(tmp_s)
                        item_desired = str(tmp_s)[1:]
                        number = int(tmp_n)
                except:
                    number = 1
                print(str(number) +"\n"+ item_desired)
                string = u.sell(item_desired, n, abs(number))
                if string[0] == "Yes":
                    await message.channel.send(content=f"Successfully Sold **{number} {item_desired}** {itemDAO.get_item_emoji(item_desired)}\n"
                                                       f"You made a profit of :moneybag: **{string[1]}**")
                else:
                    await message.channel.send(content=string[0])

            # Inventory
            if message.content.startswith("kog inv" or "kog inventory"):
                embed = discord.Embed(title=f"{n[:-5].title()}'s Inventory", description="`kog sell <number> <name>` to get 80% coins back"
                                                                             "\n`kog use <egg name>` to hatch your eggs!"
                                                                             "\n`kog equip <name>` to equip weaponry"
                                                                             "\n`kog help <name>` to see item descriptions")
                count = 0
                for i in u.get_items(n):
                    # print(i)
                    if int(u.get_items(n)[i]) > 0:
                        emoji = itemDAO.get_item_emoji(i)
                        number = int(u.get_items(n)[i])
                        embed.add_field(name=str(i).title(), value=f"{emoji} x{number}")
                        count += 1
                if count == 0:
                        embed.add_field(name="Items", value=f"Dude go buy yourself something man. `kog shop`")
                embed.color = discord.Color(0xEDDDDD)
                embed.set_thumbnail(url=p.getMain(n))
                await message.channel.send(content=None, embed=embed)


            # pet all
            if message.content == "kog pets" or message.content == "kog pet all":
                embed = discord.Embed(title=f"{n[:-5].title()}'s Pets'", description="Do `kog main <name>` to set a Main Pet !\nDo `kog pet <name>` for more info")
                pet_count = True
                mypets = mp.get_myPets(n)

                for i in mypets.keys():
                    if i:
                        number = mypets[i]["level"]
                        attr = mypets[i]["attr"]
                        name = mypets[i]["pets"]
                        main = mypets[i]["equip"]
                        hp = mypets[i]["hp"]
                        max_hp = mp.max_hp(name, number)
                        stage = mypets[i]["stage"]
                        progress = mp.get_progress_xp(i, n)
                        att = mp.get_att_inc(i, number, n)
                        defense = mp.get_def_inc(i, number, n)
                        # embed.set_image(url=emoji)
                        embed.add_field(name=name.title(), value=f"**Level:** {number} ({progress}%)| {stage} | "
                                                         f"**Attr:** {attr} | **Hp:** {hp}/{max_hp} | *{main}*\n"
                                                         f":crossed_swords: {att} :shield: {defense}", inline=False)
                        pet_count = False
                if pet_count:
                        embed.add_field(name="Items", value=f"You inhuamane beast. Go get a pet ! `kog shop egg`")

                embed.color = discord.Color(0xEDDDDD)
                embed.set_thumbnail(url=p.getMain(n))
                await message.channel.send(content=None, embed=embed)


            # Pet info
            if message.content.startswith("kog pet "):
                pet_info = message.content[8:].lower()
                mypets = mp.get_myPets(n)
                for i in mypets.keys():
                    if pet_info == i.lower():
                        number = mypets[i]["level"]
                        attr = mypets[i]["attr"]
                        name = mypets[i]["pets"]
                        xp = mypets[i]["xp"]
                        max_xp = mp.get_max_xp(i, n, number)
                        hp = mypets[i]["hp"]
                        max_hp = mp.max_hp(name, number)
                        att = mp.get_att_inc(i, number, n)
                        defense = mp.get_def_inc(i, number, n)
                        stage = mypets[i]["stage"]
                        progress = mp.get_progress_xp(i, n)
                        emoji = mypets[i]["Image_link"]
                        embed = discord.Embed(title=f"{i.title()}", description=f"Stats")
                        embed.set_image(url=emoji)
                        embed.add_field(name=f"{stage}", value=f"**Level:** {number} ({progress}%)\n**XP:** {xp}/{max_xp}\n"
                                        f"**Attr:** {attr}\n**Hp:** {hp}/{max_hp}\n:crossed_swords: {att} :shield: {defense}", inline=False)
                        await message.channel.send(content=None, embed=embed)

            # pet main info
            if message.content == "kog pet" or message.content == "kog info" :
                try:
                    mypets = mp.get_myPets(n)
                    i = p.getMain_Name(n)
                    number = mypets[i]["level"]
                    attr = mypets[i]["attr"]
                    name = mypets[i]["pets"]
                    main = mypets[i]["equip"]
                    xp = mypets[i]["xp"]
                    max_xp = mp.get_max_xp(i, n, number)
                    hp = mypets[i]["hp"]
                    max_hp = mp.max_hp(name, number)
                    stage = mypets[i]["stage"]
                    att = mp.get_att_inc(i, number, n)
                    defense = mp.get_def_inc(i, number, n)
                    progress = mp.get_progress_xp(i, n)
                    emoji = mypets[i]["Image_link"]
                    embed = discord.Embed(title=f"{i.title()}", description=f"Stats of {main}")
                    embed.set_image(url=emoji)
                    embed.add_field(name=f"{stage}", value=f"**Level:** {number} ({progress}%)\n**XP:** {xp}/{max_xp}\n"
                                     f"**Attr:** {attr}\n**Hp:** {hp}/{max_hp}\n:crossed_swords: {att} :shield: {defense}", inline=False)
                    embed.color = discord.Color(0xFF0000)
                    embed.set_footer(text="do <kog pets> to see all your pets. Remember to main them with `kog main <name>`")
                    await message.channel.send(content=None, embed=embed)
                except:
                    await message.channel.send(content="You have no pet. Go buy one in `kog shop egg` Dont for get to main them! `kog main <pet name>`")

            # Use
            if message.content.startswith("kog use "):
                try:
                    item_desired = message.content[8:].lower()
                    # print(item_desired, "    l   f")
                    # print(itemDAO.get_type(item_desired))
                    number = 0
                    count = 0
                    tmp_n = ""
                    tmp_s = ""
                    try:
                        for i in item_desired:
                            if i.isnumeric():
                                tmp_n += str(i)
                                count += 1
                            else:
                                tmp_s += i
                        if int(tmp_n) > 0:
                            item_desired = str(tmp_s)[1:]
                            number = int(tmp_n)
                    except:
                        number = 1
                    if itemDAO.get_type(item_desired) == "hp":
                        try:
                            if int(u.get_items(n)[item_desired]) != 0 :
                                s.heal(n)
                                u.decrease_item(item_desired, n, 1)
                                await message.channel.send(content="Your health is restored to full, 1 <:lifepotion:715245405918593207> consumed.")
                            else:
                                await message.channel.send(content="You go buy a potion la. You got none.")
                        except:
                            await message.channel.send(content="You go buy a potion la. You got none.")

                    if itemDAO.get_type(item_desired) == "mat":
                        await message.channel.send(content="Crafting Material. How to use? this not China, not everything can eat.")

                    if itemDAO.get_type(item_desired) == "pet":
                        if int(u.get_items(n)[item_desired]) != 0:
                            if number == 1:
                                u.decrease_item(item_desired, n, number)
                                pet = item.random_pet(item_desired)
                                x = p.increase_pet(pet, n)
                                emoji = mp.get_myPets(n)[pet]["Image_link"]
                                if x:
                                    p.setMain(item_desired, n)
                                    embed = discord.Embed(title=f"Hatch")
                                    embed.color = discord.Color(0xaec6cf)
                                    embed.set_thumbnail(url=emoji)
                                    embed.add_field(name="Congratulations! ", value="You Hatched a **" + pet + f"**\nDo `kog pet {pet}` to check it out :D ")

                                    await message.channel.send(content=None, embed=embed)
                                else:
                                    u.set_coins(n, 100)
                                    await message.channel.send(content="Aww man, you already had a " + pet)
                            else:
                                await message.channel.send(content="Your butt aint that big to hatch **that** many eggs.")
                        else:
                            await message.channel.send(content="You dont give birth to eggs, buy them in a shop ! `kog shop egg`")

                    if itemDAO.get_type(item_desired) == "att" or itemDAO.get_type(item_desired) == "def":
                        await message.channel.send(content="This is an equipment! Do `kog equip <name> instead`")

                    if itemDAO.get_type(item_desired) == "petxp":
                        if int(u.get_items(n)[item_desired]) != 0:
                            mainpet = p.getMain_Name(n)
                            if mainpet:
                                u.decrease_item(item_desired, n, number)
                                boost = int(itemDAO.get_boosts(item_desired)) * number
                                p.set_xp(boost, n)
                                b = p.check_level(mainpet, n)
                                print(b," !!!!!!!!!!!!!")
                                if b[0]:
                                    emoji = itemDAO.get_item_emoji(item_desired)
                                    embed = discord.Embed(title=f"You used {number} {item_desired} {emoji} on **{mainpet}**")
                                    embed.add_field(name=f"{mainpet} is feeling happy! ", value=f"{mainpet} increased {boost}XP and Leveled up **{b[1]} times** !!")
                                    embed.color = discord.Color(0xaec6cf)
                                    embed.set_thumbnail(url=p.getMain(n))
                                    await message.channel.send(content=None, embed=embed)
                                else:
                                    emoji = itemDAO.get_item_emoji(item_desired)
                                    embed = discord.Embed(title=f"You used {number} {item_desired} {emoji} on **{mainpet}**")
                                    embed.add_field(name=f"{mainpet} is feeling bored. You probably didnt feed him enough... ", value=f"{mainpet} "
                                                        f"increased {boost}XP")
                                    embed.color = discord.Color(0xaec6cf)
                                    embed.set_thumbnail(url=p.getMain(n))
                                    await message.channel.send(content=None, embed=embed)
                            else:
                                await message.channel.send(content="You need to set a main pet first! `kog main <name>`")

                    if itemDAO.get_type(item_desired).lower() == "lb":
                        if item_desired == "lootbox":
                            x = lb.open_common(n)
                            embed = discord.Embed(title=f"You used {1} {item_desired}")
                            embed.add_field(name=f"Wowzas!", value=x)
                            embed.color = discord.Color(0xaec6cf)
                            embed.set_thumbnail(url=p.getMain(n))
                            await message.channel.send(content=None, embed=embed)
                        if item_desired == "rare lootbox":
                            x = lb.open_rare(n)
                            embed = discord.Embed(title=f"You used {1} {item_desired}")
                            embed.add_field(name=f"Wowzas!", value=x)
                            embed.color = discord.Color(0xaec6cf)
                            embed.set_thumbnail(url=p.getMain(n))
                            await message.channel.send(content=None, embed=embed)
                except:
                    await message.channel.send(content="Check you spelling kindergartner! or maybe u dont have the item...")



            # Set Main Pet
            if message.content.startswith("kog main "):
                mainpet = message.content[9:].lower()
                x = p.setMain(mainpet, n)
                if x:
                    await message.channel.send(content="You have set **" + mainpet + "** as your main pet !")
                else:
                    await message.channel.send(content="You do not have this item. Maybe u never spell right.")


            # Equip Items
            if message.content.startswith("kog equip "):
                item_desired = message.content[10:].lower()
                try:
                    if itemDAO.get_type(item_desired) == "att" or itemDAO.get_type(item_desired) == "def":
                        x = u.equip(item_desired, n)
                        emoji = itemDAO.get_item_emoji(item_desired)
                        if x:
                            await message.channel.send(content="You have equipped **" + item_desired + " " + emoji + "**!")
                        else:
                            await message.channel.send(content="You do not have this item. Maybe u never spell right.")
                    else:
                        await message.channel.send(content="This item in unequipable!")
                except:
                    await message.channel.send(content="YoU ReaLLy CaNt sPeLL yOuR EQuiPmENts o.0")


            # Evolve Pet
            if message.content.startswith("kog evolve "):
                evo_desired = message.content[11:].lower()
                can_evo = p.can_evolve(evo_desired, n)
                now_stage = mp.get_stage_l(evo_desired, n)
                next_stage_index = stages.index(now_stage) + 1
                attr = ap.get_attr(evo_desired)
                print(can_evo)
                if can_evo == "yes":
                    mat = p.check_evo_mat(now_stage, n)
                    if mat[1]:
                        # u.decrease_item(mat[0].lower(), n, 1)
                        possible_evo = p.possible_evo(attr, stages[next_stage_index])
                        name_attr = p.get_name_attr(possible_evo)
                        await message.channel.send(content=name_attr)

                        def check(m):
                            chk = False
                            name = ""
                            for i in m.content:
                                name += i
                            name = name
                            for i in possible_evo:
                                # print(possible_evo)
                                if name == i:
                                    chk = True
                            return chk
                        try:
                            evo_tobe = await client.wait_for('message', timeout=30.0, check=check)

                        except asyncio.TimeoutError:
                            await message.channel.send('Evolution Failed !')

                        p.UpdateEvo(evo_desired, evo_tobe.content, n)

                        embed = discord.Embed(title="Hatched!", description=f"You hatched a {evo_tobe.content.capitalize()}")
                        embed.set_thumbnail(url=p.getMain(n))
                        embed.color = discord.Color(0xFFB6C1)
                        embed.set_footer(text = "do <kog pet> to see it !")
                        await message.channel.send(content=None, embed=embed)

                    else:
                        await message.channel.send(content=mat[0])
                elif can_evo == "Your pet is not high level enough!!":
                    await message.channel.send(content=can_evo)
                else:
                    await message.channel.send(content=can_evo)

            if message.content.startswith("kog evo "):
                evo_desired = message.content[8:].lower()
                can_evo = p.can_evolve(evo_desired, n)
                now_stage = mp.get_stage_l(evo_desired, n)
                next_stage_index = stages.index(now_stage) + 1
                attr = ap.get_attr(evo_desired)
                if can_evo == "yes":
                    mat = p.check_evo_mat(now_stage, n)
                    if mat[1]:
                        # u.decrease_item(mat[0].lower(), n, 1)
                        possible_evo = p.possible_evo(attr, stages[next_stage_index])
                        name_attr = p.get_name_attr(possible_evo)
                        await message.channel.send(content=name_attr)

                        def check(m):
                            chk = False
                            name = ""
                            for i in m.content:
                                name += i
                            name = name
                            for i in possible_evo:
                                # print(possible_evo)
                                if name == i:
                                    chk = True
                            return chk
                        try:
                            evo_tobe = await client.wait_for('message', timeout=30.0, check=check)

                        except asyncio.TimeoutError:
                            await message.channel.send('Evolution Failed !')

                        p.UpdateEvo(evo_desired, evo_tobe.content, n)

                        embed = discord.Embed(title="Hatched!", description=f"You hatched a {evo_tobe.content.capitalize()}")
                        embed.set_thumbnail(url=p.getMain(n))
                        embed.color = discord.Color(0xFFB6C1)
                        embed.set_footer(text = "do <kog pet> to see it !")
                        await message.channel.send(content=None, embed=embed)

                    else:
                        await message.channel.send(content=mat[0])
                elif can_evo == "Your pet is not high level enough!!":
                    await message.channel.send(content=can_evo)

                else:
                    await message.channel.send(content=can_evo)

            # Equip Items
            if message.content.startswith("kog cf "):
                embed = discord.Embed(title="Casino :diamonds:", description="Coin Flip")
                choice = message.content[7:8]
                after = message.content[8:]
                bet = ""
                for i in after:
                    if i.isnumeric():
                        bet += i
                bet = abs(int(bet))
                if bet < int(u.get_coins(n)):
                    if choice == "h":
                        choice = "heads"
                        inner_text = cf.Bet(n, choice, bet)
                    elif choice == "t":
                        choice = "tails"
                        inner_text = cf.Bet(n, choice, bet)
                    else:
                        inner_text = "Please input properly. `kog cf [h/t] [money]`"
                    embed.add_field(name="Gambling ? :smiling_imp:", value=inner_text)
                    embed.set_thumbnail(url=p.getMain(n))
                    embed.color = discord.Color(0xFFB6C1)
                    await message.channel.send(content=None, embed=embed)
                else:
                    await message.channel.send(content="Not enough money")
            # Recipes
            if message.content == "kog recipe" or message.content == "kog recipes":
                embed = discord.Embed(title="Recipes", description="Welcome to Recipes! \n`kog craft < name>`")
                dict = r.dictionary_of_all()
                for i in dict:
                    emoji = dict[i]["emoji"]
                    m1 = dict[i]["m1"]
                    m1e = dict[i]["m1e"]
                    m2 = dict[i]["m2"]
                    m2e = dict[i]["m2e"]
                    q1 = dict[i]["q1"]
                    q2 = dict[i]["q2"]
                    embed.add_field(name=f"{i}", value=f"**{emoji} = {q1} {m1}  {m1e}  +  {q2} {m2} {m2e} **", inline=False)
                embed.color = discord.Color(0xEDDDDD)
                embed.set_thumbnail(url=p.getMain(n))
                await message.channel.send(content=None, embed=embed)

            # craft
            if message.content.startswith("kog craft "):
                try:
                    item_desired = message.content[10:].title()
                    ck = r.check_ifCraft(item_desired, n)
                    if ck == "Yes":
                        ck = r.craft(item_desired, n)
                    embed = discord.Embed(title="Crafts", description="Welcome to Crafts! \nDo `kog recipe` to see Recipes")
                    embed.add_field(name=f"{item_desired}", value=f"{ck}", inline=False)
                    embed.color = discord.Color(0xEDDDDD)
                    embed.set_thumbnail(url=p.getMain(n))
                    await message.channel.send(content=None, embed=embed)
                except:

                    await message.channel.send(content="Check out `kog recipes`")


# embed.set_thumbnail(url="http://digidb.io/images/dot/dot629.png")


# client.loop.create_task(update_stats())
client.run('NzE0ODM0NTc2ODk5NTcxNzkz.Xs0o0Q.vKw8tmtsg45zX9Y9vJQW47B5wak')
