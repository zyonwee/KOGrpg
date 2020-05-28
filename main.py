import discord
import items as item
import db
import monsters as mon
import pets as p
import queries as q
import stats as s

cnx = db.cnx()
client = discord.Client()


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
                    await message.channel.send("Welcome New Player :baby: !! :dove: **" + str(message.author)[:-5] + "**" +
                                               "\n Do `kog p` or `kog profile` to see your profile! :D")
                else:
                    await message.channel.send("Shalom !! :dove: **" + str(message.author)[:-5] + "**")
            else:
                await message.channel.send("Shalom !! Type `kog` to create an account :dove: ")

        else:
            if message.content == "kog":
                    await message.channel.send("Shalom !! :dove: **" + str(message.author)[:-5] + "**")

            # profile
            if message.content == "kog p" or message.content == "kog profile":
                embed = discord.Embed(title=str(message.author)[:-5] + "'s Profile",
                                      description="Title : Noobie \nTrainer's Level : " + s.get_level(n) + " (" + s.get_progress(n) + "%)"
                                                  + "\nRealm : " + s.get_realm(n)
                                                  + "\nXp : " + s.get_curr_xp(n) + "/" + s.get_max_xp(n)
                                                  + "\n:heart: " + s.get_curr_hp(n) + "/" + s.get_max_hp(n))
                embed.add_field(name="Stats", value=":crossed_swords: **" + s.get_att(n) + "** \n\n:shield: **" +
                                                    s.get_def(n) + "**")

                equipment = item.get_Equipped(n)
                string = ""
                if equipment[0]:
                    att = item.get_boosts(equipment[0])
                    string += item.get_item_emoji(equipment[0]) + f" [ Effects **+ {att} ATT** ]\n\n"

                if equipment[1]:
                    defense = item.get_boosts(equipment[1])
                    string += item.get_item_emoji(equipment[1]) + f" [ Effects **+ {defense} DEF** ]\n"

                embed.add_field(name="Equipment", value=string)
                pet = p.getMain_Name(n)
                if pet:
                    print(pet)
                    m_pet = p.get_myPets(n)[pet]
                    lvl = m_pet["level"]
                    hp = m_pet["hp"]
                    stage = m_pet["stage"]
                    max_hp = p.max_hp(pet, lvl)
                    embed.add_field(name="Main Pet", value=f"**{pet}** *[{stage}]*\n**Level: {lvl}**\n:heart: **{hp}/{max_hp}**")
                    embed.set_thumbnail(url=p.getMain(n))
                embed.add_field(name="Bank", value= f":moneybag: **" + s.get_coins(n) + "** :comet: **" + s.get_gem(n) + "**", inline=False)
                embed.color = discord.Color(0xfdfd96)
                await message.channel.send(content=None, embed=embed)

            if message.content == ("kog shop egg"):
                embed = discord.Embed(title="Welcome to Egg Shop", description="A shop for all your Pets Eggs `kog buy <name>`")
                for i in item.get_all_eggshop():
                    emoji = item.get_item_emoji(i)
                    desc = item.get_desc(i)
                    price = item.get_price(i)
                    embed.add_field(name=str(i), value=f"{emoji}{desc}\n\n:moneybag: {price}\n")
                embed.set_thumbnail(url=p.getMain(n))
                await message.channel.send(content=None, embed=embed)

            if message.content == ("kog shop"):
                embed = discord.Embed(title="Welcome to Basic Shop", description="A shop for all your Basic Eggs `kog buy <name>`")
                embed.add_field(name="Other Shops", value=f"`kog shop egg`", inline=False)
                for i in item.get_all_shop():
                    print(item.get_all_shop(), i)
                    emoji = item.get_item_emoji(i)
                    desc = item.get_desc(i)
                    price = item.get_price(i)
                    embed.set_thumbnail(url=p.getMain(n))
                    embed.add_field(name=str(i), value=f"{emoji} {desc}\n:moneybag: {price}", inline=False)

                embed.color = discord.Color(0xEDDDDD)
                embed.set_thumbnail(url=p.getMain(n))
                await message.channel.send(content=None, embed=embed)

            if message.content == "kog help" or message.content == "kog ?":
                embed = discord.Embed(title="Welcome to KoGrpg Help", description="Listed are some basic Commands")
                embed.add_field(name="Interfacing Commands", value="`kog` `kog profile` `kog shop`", inline=False)
                embed.add_field(name="Action Commands", value="`kog hunt` `kog heal`", inline=False)
                embed.add_field(name="Pets Commands", value="`kog pet` `kog main <name>`", inline=False)
                embed.color = discord.Color(0xEDDDDD)
                embed.set_thumbnail(url=p.getMain(n))
                await message.channel.send(content=None, embed=embed)

            if message.content.startswith("kog help "):
                h = message.content[9:].lower()
                h = q.list_help(h)
                await message.channel.send(content=h)

            if message.content.startswith("kog hunt"):
                result = mon.fight(mon.chosen(s.get_level(n)), s.get_att(n), s.get_def(n), s.get_curr_hp(n), s.get_max_hp(n),
                                   s.get_level(n))
                if result[3]:
                    s.set_hp(n, result[4])
                    s.set_xp(n, result[2])
                    s.set_coins(n, result[1])
                    coins = str(result[1])
                    b = s.check_level(n)

                    drops = mon.get_drops(result[5])
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
                            item.increase_itembyNumber(drops[1], n, drops[0])
                            await message.channel.send(content=result[0] + "\nYou've Obtained **" + drops[0] + " " + drops[1]
                                                        + "**" + " and Earned **" + str(result[2])
                                                        + "xp**, :moneybag:**" + coins
                                                        + "**\nCongatulations, you Leveled Up ! +2 :crossed_swords: +2 :shield:")
                        else:
                            item.increase_itembyNumber(drops[1], n, drops[0])
                            await message.channel.send(content=result[0] + "\nYou've Obtained **" + drops[0] + " " + drops[1]
                                                        + "**" + " and Earned **" + str(result[2]) + "xp**, :moneybag:**" + coins + "**")

                else:
                    s.you_died(n)
                    s.heal(n)
                    await message.channel.send(content=result[0])

            if message.content.startswith("kog heal"):
                item_desired = "life potion"
                if item.get_type(item_desired) == "hp" and s.get_items(n)[item_desired] != 0 :
                    s.heal(n)
                    item.decrease_item(item_desired, n)
                    await message.channel.send(content="Your health is restored to full, 1 <:lifepotion:715245405918593207> consumed.")
                else:
                    await message.channel.send(content="You go buy a potion la. You got none.")

            if message.content.startswith("kog buy "):
                item_desired = message.content[8:].lower()
                print(item_desired)
                string = item.buy(item_desired, n)
                if string == "Yes":
                    await message.channel.send(content=f"Successfully bought **{item_desired}** {item.get_item_emoji(item_desired)}")
                if string == "Repeat":
                    await message.channel.send(content=f"You Already have the equipment **{item_desired}** {item.get_item_emoji(item_desired)}")
                if string == "Poor":
                    await message.channel.send(content="You too poor la. **LMAO**")

            if message.content.startswith("kog inv" or "kog inventory"):
                embed = discord.Embed(title=f"{n}'s Inventory'")
                count = 0
                for i in s.get_items(n):
                    if s.get_items(n)[i] > 0:
                        emoji = item.get_item_emoji(i)
                        number = s.get_items(n)[i]
                        embed.add_field(name=str(i), value=f"{emoji} x{number}")
                        count += 1
                if count == 0:
                        embed.add_field(name="Items", value=f"Dude go buy yourself something man. `kog shop`")
                embed.color = discord.Color(0xEDDDDD)
                embed.set_thumbnail(url=p.getMain(n))
                await message.channel.send(content=None, embed=embed)

            if message.content == "kog pets" or message.content == "kog pet":
                embed = discord.Embed(title=f"{n}'s Pets'", description="Do `kog main <name>` to set a Main Pet !")
                pet_count = 0
                mypets = p.get_myPets(n)
                for i in mypets.keys():
                    if i:
                        number = mypets[i]["level"]
                        attr = mypets[i]["attr"]
                        name = mypets[i]["pets"]
                        main = mypets[i]["equip"]
                        hp = mypets[i]["hp"]
                        max_hp = p.max_hp(name, number)
                        stage = mypets[i]["stage"]
                        # embed.set_image(url=emoji)
                        embed.add_field(name=name, value=f"**Level:** {number} | **Stage:** {stage} | "
                                                         f"**Attribute:** {attr} | **Hp:** {hp}/{max_hp} | **{main}**", inline=False)
                        pet_count += 1
                if pet_count == 0:
                        embed.add_field(name="Items", value=f"You inhuamane beast. Go get a pet ! `kog shop egg`")

                embed.color = discord.Color(0xEDDDDD)
                embed.set_thumbnail(url=p.getMain(n))
                await message.channel.send(content=None, embed=embed)

            if message.content.startswith("kog use "):
                item_desired = message.content[8:].lower()
                if item.get_type(item_desired) == "hp":
                    if s.get_items(n)[item_desired] != 0 :
                        s.heal(n)
                        item.decrease_item(item_desired, n)
                        await message.channel.send(content="Your health is restored to full, 1 <:lifepotion:715245405918593207> consumed.")
                    else:
                        await message.channel.send(content="You go buy a potion la. You got none.")

                if item.get_type(item_desired) == "misc":
                    await message.channel.send(content="Crafting Material. How to use? this not China, not everything can eat.")

                if item.get_type(item_desired) == "pet":
                    if s.get_items(n)[item_desired] != 0 :
                        item.decrease_item(item_desired, n)
                        pet = item.random_pet(item_desired)
                        x = p.increase_pet(pet, n)
                        emoji = p.get_myPets(n)[pet]["Image_link"]
                        if x:
                            embed = discord.Embed(title=f"Hatch")
                            embed.color = discord.Color(0xaec6cf)
                            embed.set_thumbnail(url=emoji)
                            embed.add_field(name="Congratulations! ", value="You Hatched a **" + pet + "**\nDo `kog pet` to check it out :D ")

                            await message.channel.send(content=None, embed=embed)
                        else:
                            s.set_coins(n, 100)
                            await message.channel.send(content="Aww man, you already had a " + pet)
                    else:
                        await message.channel.send(content="You dont give birth to eggs, buy them in a shop ! `kog shop egg`")

            if message.content.startswith("kog main "):
                mainpet = message.content[9:].lower()
                x = p.setMain(mainpet, n)
                if x:
                    await message.channel.send(content="You have set **" + mainpet + "** as your main pet !")
                else:
                    await message.channel.send(content="You do not have this item. Maybe u never spell right.")

            if message.content.startswith("kog equip "):
                item_desired = message.content[10:].lower()
                x = item.equip(item_desired, n)
                emoji = item.get_item_emoji(item_desired)
                if x:
                    await message.channel.send(content="You have equipped **" + item_desired + " " + emoji + "**!")
                else:
                    await message.channel.send(content="You do not have this item. Maybe u never spell right.")

# embed.set_thumbnail(url="http://digidb.io/images/dot/dot629.png")


# client.loop.create_task(update_stats())
client.run('NzE0ODM0NTc2ODk5NTcxNzkz.Xs0o0Q.vKw8tmtsg45zX9Y9vJQW47B5wak')
