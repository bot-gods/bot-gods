from discord import *
import discord
import datetime
import asyncio
from random import *
client = discord.Client()
messages = 0
joined = 0
oldUser = "user"
prefix = "?"
boolSW = False
green = 0
purple = 0
yellow = 0
red = 0
blue = 0
black = 0
Bgreen = False
Bpurple = False
Byellow = False
Bred = False
Bblue = False
Bblack = False
calc = False
roll = False
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
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='?help'))

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
    global oldUser
    global boolSW
    global green, purple, yellow, red, blue, black
    global Bgreen, Bpurple, Byellow, Bred, Bblue, Bblack
    global calc, roll
    # check weather the message begins with !
    if message.content.startswith(prefix) is True:
        # ##############################ADD NEW COMMANDS HERE#################################
        if message.content.startswith(prefix + "prefix") is True and message.content.endswith(
                prefix + "prefix") is False:
            msg = message.content.replace(f"""{prefix}prefix """, "")
            msg = msg.replace(f"""{prefix}prefix""", "")
            if msg != "":
                prefix = msg
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
            num = "str"

            try:
                num = abs(int(rll))
            except ValueError:
                pass
            if rll != "":
                # DICE STUFF HERE
                if isinstance(num, int):
                    rnum = randint(1, num)
                    if rnum == 1:
                        await message.channel.send(f"""A NATURAL ONE!""")
                    elif rnum == num:
                        await message.channel.send(f"""A NATURAL {rnum}!""")
                    else:
                        await message.channel.send(rnum)
                else:
                    if rll == "Genesys" or rll == "genesys" or rll == "SW":
                        oldUser = str(message.author)
                        boolSW = True
                        roll = True
                        await message.channel.send("Reply 'roll' to this message please. if you want to stop at any time type: 'cancel'")
            else:
                await message.channel.send("what do you want me to roll?")
        elif message.content.startswith(prefix + "roll") is True and message.content.endswith(prefix + "roll") is True:
            await message.channel.send("what do you want me to roll?")

        # ##############################ADD NEW COMMANDS HERE#################################


async def basicUser(message):
    global prefix
    global oldUser
    global boolSW
    global green, purple, yellow, red, blue, black
    global Bgreen, Bpurple, Byellow, Bred, Bblue, Bblack
    global calc, roll
    if message.content.startswith(prefix) is True:
        # ##############################ADD NEW COMMANDS HERE#################################
        if message.content.startswith(prefix + "prefix") is True and message.content.endswith(
                prefix + "prefix") is False:
            msg = message.content.replace(f"""{prefix}prefix """, "")
            msg = msg.replace(f"""{prefix}prefix""", "")
            if msg != "":
                prefix = msg
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
                embedme.add_field(name=f"""{prefix}members""", value="will return the current number of members in the server")
                await message.channel.send(embed=embedme)
            elif message.content.endswith("prefix") is True:
                embedp = discord.Embed(title=f"""{prefix}prefix""", Description="change the prefix",color=3456491)
                embedp.add_field(name=f"""{prefix}prefix NEW-PREFIX""", value="changes the prefix")
                await message.channel.send(embed=embedp)
            elif message.content.endswith("roll") is True:
                embedr = discord.Embed(title=f"""{prefix}roll""", Description="roll a dice", color=3456491)
                embedr.add_field(name=f"""{prefix}roll NUMBER / {prefix}roll d+NUMBER""", value="roll a dice with any amount of sides!")
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
                else:
                    if rll == "Genesys" or rll == "genesys" or rll == "SW":
                        oldUser = str(message.author)
                        boolSW = True
                        roll = True
                        await message.channel.send("Reply 'roll' to this message please. if you want to stop at any time type: 'cancel'")

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
    global oldUser
    global boolSW
    global green, purple, yellow, red, blue, black
    global Bgreen, Bpurple, Byellow, Bred, Bblue, Bblack
    global calc, roll
    messages += 1
    id = client.get_guild(693537413448073328)
    channels = ["cmd", "current-commands"]
    god_users = ["Fireye#8983", "Vasu Kedia#6141"]
    basic_users = ["bumblebee#4138"]
    # place print(message.content) here to print out all messages
    # if calc == True and boolSW == True and oldUser == str(message.author):

    if Bblack == True and boolSW == True and oldUser == str(message.author):
        success = 0
        failure = 0
        advantage = 0
        threat = 0
        triumph = 0
        despair = 0
        try:
            if int(message.content) <= 500:
                black = int(message.content)
                Bblack = False
                calc = True
            else:
                await message.channel.send("Please input a number less than 500")
        except ValueError:
            if message.content != "cancel":
                await message.channel.send("Whoops! Looks like you put in a word! Try again with a number.")
        except Exception as e:
            print(e)
            await message.channel.send("An error has occurred. Try again, or cancel")
        if calc == True:
            # await message.channel.send("green: " + str(green) + "\npurple: " + str(purple) + "\nyellow: " + str(yellow) + "\nred: " + str(red) + "\nblue: " + str(blue) + "\nblack " + str(black))
            if green != 0:
                for i in range(green):
                    i += 1
                    g = randint(1, 8)
                    if g == 1:
                        pass
                    elif g == 2:
                        success += 1
                    elif g == 3:
                        success += 1
                    elif g == 4:
                        success += 2
                    elif g == 5:
                        advantage += 1
                    elif g == 6:
                        advantage += 1
                    elif g == 7:
                        advantage += 1
                        success += 1
                    elif g == 8:
                        advantage += 2
            if purple != 0:
                for j in range(purple):
                    j += 1
                    p = randint(1, 8)
                    if p == 1:
                        pass
                    elif p == 2:
                        failure += 1
                    elif p == 3:
                        failure += 1
                    elif p == 4:
                        failure += 2
                    elif p == 5:
                        threat += 1
                    elif p == 6:
                        threat += 1
                    elif p == 7:
                        threat += 1
                        failure += 1
                    elif p == 8:
                        threat += 2
                        failure += 1
            if yellow != 0:
                for i in range(yellow):
                    i += 1
                    y = randint(1, 12)
                    if y == 1:
                        pass
                    elif y == 2:
                        success += 1
                    elif y == 3:
                        success += 1
                    elif y == 4:
                        success += 2
                    elif y == 5:
                        success += 2
                    elif y == 6:
                        advantage += 1
                    elif y == 7:
                        advantage += 1
                        success += 1
                    elif y == 8:
                        advantage += 1
                        success += 1
                    elif y == 9:
                        advantage += 1
                        success += 1
                    elif y == 10:
                        advantage += 2
                    elif y == 11:
                        advantage += 2
                    elif y == 12:
                        triumph += 1
                        success += 1
            if red != 0:
                for i in range(red):
                    i += 1
                    r = randint(1, 12)
                    if r == 1:
                        pass
                    elif r == 2:
                        failure += 1
                    elif r == 3:
                        failure += 1
                    elif r == 4:
                        failure += 2
                    elif r == 5:
                        failure += 2
                    elif r == 6:
                        threat += 1
                    elif r == 7:
                        threat += 1
                        failure += 1
                    elif r == 8:
                        threat += 1
                        failure += 1
                    elif r == 9:
                        threat += 1
                        failure += 1
                    elif r == 10:
                        threat += 2
                    elif r == 11:
                        threat += 2
                    elif r == 12:
                        despair += 1
            if blue != 0:
                for i in range(blue):
                    i += 1
                    b = randint(1, 6)
                    if b == 1:
                        pass
                    elif b == 2:
                        pass
                    elif b == 3:
                        success += 1
                    elif b == 4:
                        advantage += 1
                        success += 1
                    elif b == 5:
                        advantage += 2
                    elif b == 6:
                        advantage += 1
            if black != 0:
                for i in range(black):
                    i += 1
                    bl = randint(1, 6)
                    if bl == 1:
                        pass
                    elif bl == 2:
                        pass
                    elif bl == 3:
                        success += 1
                    elif bl == 4:
                        advantage += 1
                        success += 1
                    elif bl == 5:
                        advantage += 2
                    elif bl == 6:
                        advantage += 1
            # await message.channel.send(f"success: {success}\nadvantage: {advantage}\nfailure: {failure}\nthreat: {threat}\ntriumph: {triumph}\ndespair: {despair}")
            sf = success - failure
            at = advantage - threat
            if sf >= 0:
                await message.channel.send(f"success: {abs(sf)}")
            elif sf < 0:
                await message.channel.send(f"failure: {abs(sf)}")
            if at >= 0:
                await message.channel.send(f"advantage: {abs(at)}")
            elif at < 0:
                await message.channel.send(f"threat: {abs(at)}")
            await message.channel.send(f"triumph: {triumph}")
            await message.channel.send(f"despair: {despair}")
            boolSW = False
            calc = False
    if Bblue == True and boolSW == True and oldUser == str(message.author):
        try:
            if int(message.content) <= 500:
                blue = int(message.content)
                await message.channel.send("how many black dice?")
                Bblue = False
                Bblack = True
            else:
                await message.channel.send("Please input a number less than 500")
        except ValueError:
            if message.content != "cancel":
                await message.channel.send("Whoops! Looks like you put in a word! Try again with a number.")
        except Exception as e:
            print(e)
            await message.channel.send("An error has occurred. Try again, or cancel")
    if Bred == True and boolSW == True and oldUser == str(message.author):
        try:
            if int(message.content) <= 500:
                red = int(message.content)
                await message.channel.send("how many blue dice?")
                Bred = False
                Bblue = True
            else:
                await message.channel.send("Please input a number less than 500")
        except ValueError:
            if message.content != "cancel":
                await message.channel.send("Whoops! Looks like you put in a word! Try again with a number.")
        except Exception as e:
            print(e)
            await message.channel.send("An error has occurred. Try again, or cancel")
    if Byellow == True and boolSW == True and oldUser == str(message.author):
        try:
            if int(message.content) <= 500:
                yellow = int(message.content)
                await message.channel.send("how many red dice?")
                Byellow = False
                Bred = True
            else:
                await message.channel.send("Please input a number less than 500")
        except ValueError:
            if message.content != "cancel":
                await message.channel.send("Whoops! Looks like you put in a word! Try again with a number.")
        except Exception as e:
            print(e)
            await message.channel.send("An error has occurred. Try again, or cancel")
    if Bpurple == True and boolSW == True and oldUser == str(message.author):
        try:
            if int(message.content) <= 500:
                purple = int(message.content)
                await message.channel.send("how many yellow dice?")
                Bpurple = False
                Byellow = True
            else:
                await message.channel.send("Please input a number less than 500")
        except ValueError:
            if message.content != "cancel":
                await message.channel.send("Whoops! Looks like you put in a word! Try again with a number.")
        except Exception as e:
            print(e)
            await message.channel.send("An error has occurred. Try again, or cancel")
    if Bgreen == True and boolSW == True and oldUser == str(message.author):
        try:
            if int(message.content) <= 500:
                green = int(message.content)
                await message.channel.send("how many purple dice?")
                Bgreen = False
                Bpurple = True
            else:
                await message.channel.send("Please input a number less than 500")
        except ValueError:
            if message.content != "cancel":
                await message.channel.send("Whoops! Looks like you put in a word! Try again with a number.")
        except Exception as e:
            print(e)
            await message.channel.send("An error has occurred. Try again, or cancel")
    if boolSW == True and oldUser == str(message.author) and message.content == "roll":
        await message.channel.send("how many green dice?")
        Bgreen = True
        roll = False
    if boolSW == True and oldUser == str(message.author) and message.content == "cancel":
        boolSW = False
        await message.channel.send("process cancelled. :)")









    # check if message writer is a valid user
    if str(message.author) in god_users:
        # check if the message is in the correct channel
        # if str(message.channel) in channels:
        await godUser(message)
        # check if the message is not in the correct channel, but if it begins with !
        # elif str(message.channel) not in channels and message.content.startswith(prefix) is True:
            # log attempted command
        #     print(f"""{message.author} said {message.content} in {message.channel}""")
    # check if writer is not a valid user
    elif str(message.author) not in god_users:
        # check if the message is in the correct channel
        #if str(message.channel) in channels:
        await basicUser(message)
        # check if the message is not in the correct channel, but if it begins with !
        # elif str(message.channel) not in channels and message.content.startswith(prefix) is True:
            # log attempted command
        #     print(f"""{message.author} tried to use '{message.content}' in {message.channel}""")

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
