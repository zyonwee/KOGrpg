import discord
import stats as s
import items as item
import monsters as mon
import db

cnx = db.cnx()
client = discord.Client()

@client.event
async def on_message(message):
    message.content = message.content.lower()
    n = str(message.author).strip()
    if message.author == client.user:
        return

    # new gamer
    if message.content == "kog":

        try:
            array = s.get_allName()
            new = True
            for i in array:
                if i == str(message.author).strip():
                   new = False
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
        except Exception as e:
            print(e)

    # profile
    if message.content.startswith("kog p" or "kog profile"):
        embed = discord.Embed(title=str(message.author)[:-5] + "'s Profile",
                              description="Title : Noobie \n Level : " + s.get_level(n)
                              + "\nXp : " + s.get_curr_xp(n) + "/" + s.get_max_xp(n)
                              + "\n:heart: " + s.get_curr_hp(n) + "/" + s.get_max_hp(n))
        embed.add_field(name="Stats", value=":crossed_swords: **" + s.get_att(n) + "** \n\n:shield: **" +
                                            s.get_def(n) + "**")
        embed.add_field(name="Equipment", value="[NONE] \n\n\n\n :moneybag: **" + s.get_coins(n) + "** :comet: **" +
                                                s.get_gem(n) + "**", )
        embed.add_field(name="Pet", value="[NONE]")
        await message.channel.send(content=None, embed=embed)

    if message.content.startswith("kog shop"):
        embed = discord.Embed(title="Welcome to Basic Shop", description="A shop for all your BARE NECESSITIES")
        for i in item.get_all_shop():
            emoji = item.get_item_emoji(i)
            desc = item.get_desc(i)
            price = item.get_price(i)
            embed.add_field(name=str(i), value=f"{emoji}{desc}\n:moneybag: {price}\n")
        await message.channel.send(content=None, embed=embed)

    if message.content.startswith("kog help" or "kog ?"):
        embed = discord.Embed(title="Welcome to KoGrpg Help", description="Listed are some basic Commands")
        embed.add_field(name="Interfacing Commands", value="`kog` `kog profile` `kog shop`")
        embed.add_field(name="Action Commands", value="`kog hunt` `kog heal`")

        await message.channel.send(content=None, embed=embed)

    if message.content.startswith("kog hunt"):
        result = mon.fight(mon.chosen(s.get_level(n)), s.get_att(n), s.get_def(n), s.get_curr_hp(n), s.get_max_hp(n))
        if result[3]:
            s.set_hp(n, result[4])
            s.set_xp(n, result[2])
            s.set_coins(n, result[1])
            s.check_level(n)
            drops = mon.get_drops(result[5])
            if drops[1] == "Hmm.. nothing here":
                await message.channel.send(content=result[0] + "\n" + drops[1] + ". Earned **" + str(result[2]) + "xp**")
            else:
                await message.channel.send(content=result[0] + "\nYou've Obtained **" + drops[0] + " " + drops[1] + "**" + " and Earned **" + str(result[2]) + "xp**")
        else:
            s.you_died(n)
            s.heal(n)
            await message.channel.send(content=result[0])

    if message.content.startswith("kog heal"):
        s.heal(n)
        await message.channel.send(content="Your health is restored to full, 1 <:lifepotion:715245405918593207> consumed.")


# client.loop.create_task(update_stats())
client.run('NzE0ODM0NTc2ODk5NTcxNzkz.Xs0o0Q.vKw8tmtsg45zX9Y9vJQW47B5wak')
