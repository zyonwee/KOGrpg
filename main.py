import discord
import asyncio
import time

messages = joined = 0

client = discord.Client()


# def read_token():
#     with open("./stats/stats.txt", "r") as f:
#         lines = f.readlines()
#         return lines[0].strip()
# token = read_token()




# @client.event
# async def on_member_join(member):
#     global joined
#     joined += 1
#     for channel in member.server.channels:
#         if str(channel) == "general":
#             await client.send_message(f"""Welcome to the server {member.mention}""")

# def noun_handling(noun):
#         name_bold = noun

@client.event
async def on_message(message):
    message.content = message.content.lower()
    if message.author == client.user:
        return

    if message.content == "kog":
        await message.channel.send("Shalom !! :dove: **" + str(message.author)[:-5] + "**")

    if message.content.startswith("kog p" or "kog profile"):
        embed = discord.Embed(title=str(message.author)[:-5] + "'s Profile", description="Title : Noobie")
        embed.add_field(name="Stats", value=":crossed_swords: **3** \n\n:shield: **2**")
        embed.add_field(name="Equipment", value="[NONE] \n\n\n\n :moneybag: **0**", )
        embed.add_field(name="Pet", value=":fish:")

        await message.channel.send(content=None, embed=embed)

# client.loop.create_task(update_stats())
client.run('NzE0ODM0NTc2ODk5NTcxNzkz.Xs0o0Q.vKw8tmtsg45zX9Y9vJQW47B5wak')
