from discord import *
import discord
import datetime
import asyncio
from random import *
client = discord.Client()
messages = 0
joined = 0
prefix = "?"
def readtoken():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()
token = readtoken()
"""
if discord.guild.name == "Bot test":
    prefix = "!"
else:
    prefix = "?"
"""
async def update_stats():
    await client.wait_until_ready()
    global messages, joined
    # while the bot is running
    while not client.is_closed():
        # do this
        try:
            # log to stats.txt
            with open("stats.txt", "a") as f:
                # log message
                f.write(f"Date/Time: {datetime.datetime.utcnow()}, Messages: {messages}, New members: {joined}\n")
            # resets variables
            messages = 0
            joined = 0
            # refresh time in seconds
            await asyncio.sleep(3600)
        # exception
        except Exception as e:
            # print exception
            print(e)


async def godUser(message):
    global prefix
    # check weather the message begins with !
    if message.content.startswith(prefix) is True:
        # ##############################ADD NEW COMMANDS HERE#################################
        if message.content.startswith(prefix + "prefix") is True and message.content.endswith(prefix + "prefix") is False:
            msg = message.content.replace(f"""{prefix}prefix """, "")
            msg = msg.replace(f"""{prefix}prefix""", "")
            if msg != "":
                prefix = msg
                """
                try:
                    # log to stats.txt
                    with open("stats.txt", "a") as f:
                        # log message
                        f.write(f"prefix changed to {prefix} on server: {guild.name}\n")
                # exception
                except Exception as e:
                    # print exception
                    print(e)
                """
                await message.channel.send(f"""Prefix changed to: {prefix}""")
            else:
                await message.channel.send("please put a prefix in!")
        elif message.content.startswith(prefix + "prefix") is True and message.content.endswith(prefix + "prefix") is True:
            await message.channel.send("please put a prefix in!")
        # check for !help
        if message.content.startswith(prefix + "help") is True and message.content.endswith(prefix + "help") is True:
            # sends help message
            embedh = discord.Embed(title="Help", Description="what kind of help do you need?", color=3456491)
            embedh.add_field(name=f"""{prefix}help cmd""", value="Display all the bot commands")
            embedh.add_field(name=f"""{prefix}help COMMAND-NAME""", value="help on a specific command")
            await message.channel.send(embed=embedh)
        elif message.content.startswith(prefix + "help") is True and message.content.endswith(prefix + "help") is False:
            if message.content.endswith("cmd") is True:
                embedc = discord.Embed(title="Commands", Description="Bot commands", color=3456491)
                embedc.add_field(name=f"""{prefix}hello""", value="Sends you a friendly greeting")
                embedc.add_field(name=f"""{prefix}members""", value="# of members in the server")
                embedc.add_field(name=f"""{prefix}prefix""", value="changes the prefix")
                embedc.add_field(name=f"""{prefix}roll""", value="roll a dice")
                await message.channel.send(embed=embedc)
            elif message.content.endswith("hello") is True:
                embedhe = discord.Embed(title=f"""{prefix}hello""", Description="Hello command", color=3456491)
                embedhe.add_field(name=f"""{prefix}hello""", value="will send you a hello message!")
                await message.channel.send(embed=embedhe)
            elif message.content.endswith("members") is True:
                embedme = discord.Embed(title=f"""{prefix}members""", Description="member count", color=3456491)
                embedme.add_field(name=f"""{prefix}members""",
                                  value="will return the current number of members in the server")
                await message.channel.send(embed=embedme)
            elif message.content.endswith("prefix") is True:
                embedp = discord.Embed(title=f"""{prefix}prefix""", Description="change the prefix", color=3456491)
                embedp.add_field(name=f"""{prefix}prefix NEW-PREFIX""", value="changes the prefix")
                await message.channel.send(embed=embedp)
            elif message.content.endswith("roll") is True:
                embedr = discord.Embed(title=f"""{prefix}roll""", Description="roll a dice", color=3456491)
                embedr.add_field(name=f"""{prefix}roll NUMBER / {prefix}roll d+NUMBER""",
                                 value="roll a dice with any amount of sides!")
                await message.channel.send(embed=embedr)
                # check for !hello
        if message.content.startswith(prefix + "hello") is True and message.content.endswith(prefix + "hello") is True:
            # reply hello
            await message.channel.send("hello, supreme leader")
        # check for !members
        if message.content.startswith(prefix + "members") is True and message.content.endswith(
                prefix + "members") is True:
            # reply with the # of members
            await message.channel.send(f"""the number of members, my lord: {id.member_count}""")
        if message.content.startswith(prefix + "roll") is True and message.content.endswith(prefix + "roll") is False:
            rll = message.content.replace(f"""{prefix}roll d""", "")
            rll = rll.replace(f"""{prefix}roll """, "")
            rll = rll.replace(f"""{prefix}roll""", "")
            num = "lel"
            try:
                num = abs(int(rll))
            except ValueError:
                pass
            if rll != "":
                # DICE STUFF HERE
                if isinstance(num, int):
                    print("numint")
                    rnum = randint(1, num)
                    if rnum == 1:
                        await message.channel.send(f"""A NATURAL ONE!""")
                    elif rnum == num:
                        await message.channel.send(f"""A NATURAL {rnum}!""")
                    else:
                        await message.channel.send(rnum)
                # else:

            else:
                await message.channel.send("what do you want me to roll?")
        elif message.content.startswith(prefix + "roll") is True and message.content.endswith(
                prefix + "prefix") is True:
            await message.channel.send("what do you want me to roll?")
        elif message.content.find(prefix+"annoy")!=-1:
            x=0
            while(x<20):
                await message.channel.send("Vasu is a god")
                x+=1

        # ##############################ADD NEW COMMANDS HERE#################################


async def basicUser(message):
    global prefix
    global messages, joined
    if message.content.startswith(prefix) is True:
        # ##############################ADD NEW COMMANDS HERE#################################
        if message.content.startswith(prefix + "prefix") is True and message.content.endswith(
                prefix + "prefix") is False:
            msg = message.content.replace(f"""{prefix}prefix """, "")
            msg = msg.replace(f"""{prefix}prefix""", "")
            if msg != "":
                prefix = msg
                """
                try:
                    # log to stats.txt
                    with open("stats.txt", "a") as f:
                        # log message
                        f.write(f"prefix changed to {prefix} on server: {guild.name}\n")
                # exception
                except Exception as e:
                    # print exception
                    print(e)
                """
                await message.channel.send(f"""Prefix changed to: {prefix}""")
            else:
                await message.channel.send("please put a prefix in!")
        elif message.content.startswith(prefix + "prefix") is True and message.content.endswith(
                prefix + "prefix") is True:
            await message.channel.send("please put a prefix in!")
        # check for !help
        if message.content.startswith(prefix + "help") is True and message.content.endswith(
                prefix + "help") is True:
            # sends help message
            embedh = discord.Embed(title="Help", Description="what kind of help do you need?", color=3456491)
            embedh.add_field(name=f"""{prefix}help cmd""", value="Display all the bot commands")
            embedh.add_field(name=f"""{prefix}help COMMAND-NAME""", value="help on a specific command")
            await message.channel.send(embed=embedh)
        elif message.content.startswith(prefix + "help") is True and message.content.endswith(
                prefix + "help") is False:
            if message.content.endswith("cmd") is True:
                embedc = discord.Embed(title="Commands", Description="Bot commands", color=3456491)
                embedc.add_field(name=f"""{prefix}hello""", value="Sends you a friendly greeting")
                embedc.add_field(name=f"""{prefix}members""", value="# of members in the server")
                embedc.add_field(name=f"""{prefix}prefix""", value="changes the prefix")
                embedc.add_field(name=f"""{prefix}roll""", value="roll a dice")
                await message.channel.send(embed=embedc)
            elif message.content.endswith("hello") is True:
                embedhe = discord.Embed(title=f"""{prefix}hello""", Description="Hello command", color=3456491)
                embedhe.add_field(name=f"""{prefix}hello""", value="will send you a hello message!")
                await message.channel.send(embed=embedhe)
            elif message.content.endswith("members") is True:
                embedme = discord.Embed(title=f"""{prefix}members""", Description="member count", color=3456491)
                embedme.add_field(name=f"""{prefix}members""",
                                  value="will return the current number of members in the server")
                await message.channel.send(embed=embedme)
            elif message.content.endswith("prefix") is True:
                embedp = discord.Embed(title=f"""{prefix}prefix""", Description="change the prefix",
                                       color=3456491)
                embedp.add_field(name=f"""{prefix}prefix NEW-PREFIX""", value="changes the prefix")
                await message.channel.send(embed=embedp)
            elif message.content.endswith("roll") is True:
                embedr = discord.Embed(title=f"""{prefix}roll""", Description="roll a dice", color=3456491)
                embedr.add_field(name=f"""{prefix}roll NUMBER / {prefix}roll d+NUMBER""",
                                 value="roll a dice with any amount of sides!")
                await message.channel.send(embed=embedr)
        # check for !hello
        if message.content.startswith(prefix + "hello") is True and message.content.endswith(prefix + "hello") is True:
            # reply with hi
            await message.channel.send("Hi")
        # check for !members
        if message.content.startswith(prefix + "members") is True and message.content.endswith(
                prefix + "members") is True:
            # reply with the # of members
            await message.channel.send(f"""number of members: {id.member_count}""")
        if message.content.startswith(prefix + "roll") is True and message.content.endswith(prefix + "roll") is False:
            rll = message.content.replace(f"""{prefix}roll d""", "")
            rll = rll.replace(f"""{prefix}roll """, "")
            rll = rll.replace(f"""{prefix}roll""", "")
            num = "lel"
            try:
                num = abs(int(rll))
            except ValueError:
                pass
            if rll != "":
                # DICE STUFF HERE
                if isinstance(num, int):
                    print("numint")
                    rnum = randint(1, num)
                    if rnum == 1:
                        await message.channel.send(f"""A NATURAL ONE!""")
                    elif rnum == num:
                        await message.channel.send(f"""A NATURAL {rnum}!""")
                    else:
                        await message.channel.send(rnum)
                # else: put star wars dice function here

            else:
                await message.channel.send("what do you want me to roll?")
        elif message.content.startswith(prefix + "roll") is True and message.content.endswith(
                prefix + "prefix") is True:
            await message.channel.send("what do you want me to roll?")

        # ##############################ADD NEW COMMANDS HERE#################################

@client.event
async def on_message(message):
    global messages
    global prefix
    messages += 1
    id = client.get_guild(693537413448073328)
    channels = ["cmd", "current-commands"]
    god_users = ["Fireye#8983","Vasu Kedia#6141"]
    basic_users = ["bumblebee#4138"]
    # place print(message.content) here to print out all messages

    # check if message writer is a valid user
    if str(message.author) in god_users:
        # check if the message is in the correct channel
        if str(message.channel) in channels:
            await godUser(message)
        # check if the message is not in the correct channel, but if it begins with !
        elif str(message.channel) not in channels and message.content.startswith(prefix) is True:
            # log attempted command
            print(f"""{message.author} said {message.content} in {message.channel}""")
    # check if writer is not a valid user
    elif str(message.author) not in god_users:
        # check if the message is in the correct channel
        if str(message.channel) in channels:
            await basicUser(message)
        # check if the message is not in the correct channel, but if it begins with !
        elif str(message.channel) not in channels and message.content.startswith(prefix) is True:
            # log attempted command
            print(f"""{message.author} tried to use '{message.content}' in {message.channel}""")

@client.event
async def on_member_join(member):
    global basic_users
    global joined
    joined += 1
    print(f"""{member} has joined the server! Put them into basic users.""")
    for channel in member.server.channels:
        if str(channel) == "general":
            await client.send_message(f"""Welcome to the server, {member.mention}! I am the almighty BotGod!""")


# constantly update stats
client.loop.create_task(update_stats())
# run token
client.run(token)
