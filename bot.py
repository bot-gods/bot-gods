from discord import *
from discord.ext import *
import discord
import datetime
import asyncio
import os
from random import *
client = discord.Client()
messages = 0
joined = 0
oldUser = "user"
prefix = "?"
boolSW = False
oldChannel = "channel"
green = 0
purple = 0
yellow = 0
red = 0
blue = 0
black = 0
fields = []
var = []
oldprefix = "yeet"
Bgreen = False
Bpurple = False
Byellow = False
Bred = False
Bblue = False
Bblack = False
calc = False
roll = False
prfx = "f"
oldUser2 = ""
oldchannel2 = ""
oldUser3 = ""
oldchannel3 = ""
oldUser4 = ""
oldchannel4 = ""
oldUser5 = ""
oldchannel5 = ""
Ndata = False
Ndata1 = False
Ndata2 = False
Ndata3 = False
Next = False
DData = False
DData1 = False
DData2 = False
confirmedUser = False
x = 0
CategoryName = ""
subsectionName = ""
subsectionValue = ""
filer = ""
subsectionscompleted = 0
Adata = False
Adata1 = False

dir = "C:/Users/EOLUser/PycharmProjects/bot-gods"
os.chdir(dir)
def readtoken():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


token = readtoken()
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
            await asyncio.sleep(86400)
        # exception
        except Exception as e:
            # print exception
            print(e)


async def godUser(message):
    global prefix
    global boolSW
    global oldprefix
    global green, purple, yellow, red, blue, black
    global Bgreen, Bpurple, Byellow, Bred, Bblue, Bblack
    global calc, roll
    global Ndata, Next, DData, DData2, Adata, Adata1
    global oldUser, oldUser2, oldUser3, oldUser4, oldUser5, oldChannel, oldchannel2, oldchannel3, oldchannel4, oldchannel5
    # check weather the message begins with !
    if message.content.startswith(prefix) is True:
        # ##############################ADD NEW COMMANDS HERE#################################
        if message.content.startswith(prefix + "prefix") is True and message.content.endswith(prefix + "prefix") is False:
            msg = message.content.replace(f"""{prefix}prefix """, "")
            msg = msg.replace(f"""{prefix}prefix""", "")
            if msg != "":
                oldprefix = prefix
                prefix = msg
                try:
                    with open('prefix.txt', 'r+') as f:
                        strp = f.read()
                        count = 0
                        new_file_content = ""
                        if strp.find(str(message.guild)) != -1:
                            CoList = strp.split("\n")
                            for i in CoList:
                                if i:
                                    count += 1
                                if i.find(str(message.guild)) != -1:
                                    stripped_line = i.strip()
                                    new_line = stripped_line.replace(oldprefix, prefix)

                            dir = "C:/Users/EOLUser/PycharmProjects/bot-gods"
                            os.chdir(dir)
                            f.write(new_line + "\n")
                        else:
                            f = open('prefix.txt', 'a')
                            f.write(f"{str(message.guild)} {prefix}\n")
                            f.close()
                    # exception
                except Exception as e:
                    # print exception
                    print(e)
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
                embedc.add_field(name=f"""{prefix}roll""", value="roll a die")
                embedc.add_field(name=f"""{prefix}clear""", value="delete a number of messages")
                embedc.add_field(name=f"""{prefix}data""", value="store and access important data")
                await message.channel.send(embed=embedc)
            elif message.content.endswith("hello") is True:
                embedhe = discord.Embed(title=f"""{prefix}hello""", Description="Hello command", color=3456491)
                embedhe.add_field(name=f"""{prefix}hello""", value="will send you a hello message!")
                await message.channel.send(embed=embedhe)
            elif message.content.endswith("members") is True:
                embedme = discord.Embed(title=f"""{prefix}members""", Description="member count", color=3456491)
                embedme.add_field(name=f"""{prefix}members""",value="will return the current number of members in the server")
                await message.channel.send(embed=embedme)
            elif message.content.endswith("prefix") is True:
                embedp = discord.Embed(title=f"""{prefix}prefix""", Description="change the prefix", color=3456491)
                embedp.add_field(name=f"""{prefix}prefix NEW-PREFIX""", value="changes the prefix")
                await message.channel.send(embed=embedp)
            elif message.content.endswith("roll") is True:
                embedr = discord.Embed(title=f"""{prefix}roll""", Description="roll a dice", color=3456491)
                embedr.add_field(name=f"""{prefix}roll NUMBER / {prefix}roll d+NUMBER""", value="roll a dice with any amount of sides!")
                embedr.add_field(name=f"""{prefix}roll SW / {prefix}roll Genesys""", value="roll genesys style dice.")
                await message.channel.send(embed=embedr)
            elif message.content.endswith("clear") is True:
                embedclr = discord.Embed(title=f"""{prefix}clear""", Description="delete a number of messages", color=3456491)
                embedclr.add_field(name=f"""{prefix}clear MESSAGES""", value="delete a number of messages")
                await message.channel.send(embed=embedclr)
            elif message.content.endswith("data") is True:
                embedclr = discord.Embed(title=f"""{prefix}data""", Description="store and access important data",color=3456491)
                embedclr.add_field(name=f"""{prefix}data add""", value="make a new category")
                embedclr.add_field(name=f"""{prefix}data delete""", value="remove a category")
                embedclr.add_field(name=f"""{prefix}data edit""", value="COMING SOON")
                embedclr.add_field(name=f"""{prefix}data access""", value="access all of the subsections in a category")
                await message.channel.send(embed=embedclr)
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
                rnum = randint(1, 20)
                if rnum == 1:
                    await message.channel.send(f"""A NATURAL ONE!""")
                elif rnum == 20:
                    await message.channel.send(f"""A NATURAL 20!""")
                else:
                    await message.channel.send(rnum)
        elif message.content.startswith(prefix + "roll") is True and message.content.endswith(prefix + "roll") is True:
            rnum = randint(1, 20)
            if rnum == 1:
                await message.channel.send(f"""A NATURAL ONE!""")
            elif rnum == 20:
                await message.channel.send(f"""A NATURAL 20!""")
            else:
                await message.channel.send(rnum)
        if message.content.find(prefix + "clear") != -1:
            amount = message.content.replace(prefix + "clear ", "")
            await message.channel.purge(limit=int(amount) + 1)
            await(await message.channel.send(f"{amount} messages cleared.")).delete(delay=4)
        if message.content.startswith(f"{prefix}reactionrole new"):
            print(str(message.guild))
        elif message.content.startswith(f"{prefix}reactionrole edit"):
            pass
        elif message.content.startswith(f"{prefix}reactionrole delete"):
            pass
        if message.content.startswith(f"{prefix}data add"):
            await message.channel.send("I will prompt you for different categories that you want me to store, then I will ask for values to put under them. Please refrain from writing : and ; as it will mess up your stat block")
            await asyncio.sleep(0.5)
            await message.channel.send("Reply to this message with the category name (Remember this). It is CAPS SENSTITVE. If you want to cancel the whole process, reply 'cancel' at any time")
            Ndata = True
            Next = True
            oldUser2 = message.author
            oldchannel2 = message.channel
        if message.content.startswith(f"{prefix}data delete"):
            await message.channel.send("Reply to this message with the name of the category that you want to delete. It is CAPS SENSTITVE. If you want to cancel the whole process, reply 'cancel' at any time")
            DData = True
            DData2 = True
            oldUser3 = message.author
            oldchannel3 = message.channel
        if message.content.startswith(f"{prefix}data access"):
            await message.channel.send("Reply to this message with the name of the category that you want to access. It is CAPS SENSTITVE. If you want to cancel the whole process, reply 'cancel' at any time")
            Adata = True
            Adata1 = True
            oldUser4 = message.author
            oldchannel4 = message.channel
        # ##############################ADD NEW COMMANDS HERE#################################




async def basicUser(message):
    global prefix
    global oldUser, oldUser2, oldUser3, oldUser4, oldUser5, oldChannel, oldchannel2, oldchannel3, oldchannel4, oldchannel5
    global boolSW
    global oldprefix
    global green, purple, yellow, red, blue, black
    global Bgreen, Bpurple, Byellow, Bred, Bblue, Bblack
    global calc, roll
    global Ndata, Next, DData, DData2, Adata, Adata1
    if message.content.startswith(prefix) is True:
        # ##############################ADD NEW COMMANDS HERE#################################
        if message.content.startswith(prefix + "prefix") is True and message.content.endswith(
                prefix + "prefix") is False:
            msg = message.content.replace(f"""{prefix}prefix """, "")
            msg = msg.replace(f"""{prefix}prefix""", "")
            if msg != "":
                oldprefix = prefix
                prefix = msg
                oldprefix = prefix
                prefix = msg
                try:
                    with open('prefix.txt', 'r+') as f:
                        strp = f.read()
                        count = 0
                        new_file_content = ""
                        if strp.find(str(message.guild)) != -1:
                            CoList = strp.split("\n")
                            for i in CoList:
                                if i:
                                    count += 1
                                if i.find(str(message.guild)) != -1:
                                    stripped_line = i.strip()
                                    new_line = stripped_line.replace(oldprefix, prefix)

                            dir = "C:/Users/EOLUser/PycharmProjects/bot-gods"
                            os.chdir(dir)
                            f.write(new_line + "\n")
                        else:
                            f = open('prefix.txt', 'a')
                            f.write(f"{str(message.guild)} {prefix}\n")
                            f.close()
                    # exception
                except Exception as e:
                    # print exception
                    print(e)
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
                embedc.add_field(name=f"""{prefix}roll""", value="roll a die")
                embedc.add_field(name=f"""{prefix}clear""", value="delete a number of messages")
                embedc.add_field(name=f"""{prefix}data""", value="store and access important data")
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
                embedr.add_field(name=f"""{prefix}roll SW / {prefix}roll Genesys""", value="roll genesys style dice.")
                await message.channel.send(embed=embedr)
            elif message.content.endswith("clear") is True:
                embedclr = discord.Embed(title=f"""{prefix}clear""", Description="delete a number of messages", color=3456491)
                embedclr.add_field(name=f"""{prefix}clear MESSAGES""", value="delete a number of messages")
                await message.channel.send(embed=embedclr)
            elif message.content.endswith("data") is True:
                embedclr = discord.Embed(title=f"""{prefix}data""", Description="store and access important data",color=3456491)
                embedclr.add_field(name=f"""{prefix}data add""", value="make a new category")
                embedclr.add_field(name=f"""{prefix}data delete""", value="remove a category")
                embedclr.add_field(name=f"""{prefix}data edit""", value="COMING SOON")
                embedclr.add_field(name=f"""{prefix}data access""", value="access all of the subsections in a category")
                await message.channel.send(embed=embedclr)
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
                        oldChannel = str(message.channel)
                        boolSW = True
                        roll = True
                        await message.channel.send("Reply 'roll' to this message please. if you want to stop at any time type: 'cancel'")

            else:
                rnum = randint(1, 20)
                if rnum == 1:
                    await message.channel.send(f"""A NATURAL ONE!""")
                elif rnum == 20:
                    await message.channel.send(f"""A NATURAL 20!""")
                else:
                    await message.channel.send(rnum)
        elif message.content.startswith(prefix + "roll") is True and message.content.endswith(prefix + "roll") is True:
            rnum = randint(1, 20)
            if rnum == 1:
                await message.channel.send(f"""A NATURAL ONE!""")
            elif rnum == 20:
                await message.channel.send(f"""A NATURAL 20!""")
            else:
                await message.channel.send(rnum)
        elif message.content.find(prefix + "clear") != -1:
            await message.content.send("You don't have permission to use this command.")
        if message.content.startswith(f"{prefix}data add"):
            await message.channel.send("I will prompt you for different categories that you want me to store, then I will ask for values to put under them. Please refrain from writing : and ; as it will mess up your stat block")
            await asyncio.sleep(0.5)
            await message.channel.send("Reply to this message with the category name (Remember this). It is CAPS SENSTITVE. If you want to cancel the whole process, reply 'cancel' at any time")
            Ndata = True
            Next = True
            oldUser2 = message.author
            oldchannel2 = message.channel
        if message.content.startswith(f"{prefix}data delete"):
            await message.channel.send("Reply to this message with the name of the category that you want to delete. It is CAPS SENSTITVE. If you want to cancel the whole process, reply 'cancel' at any time")
            DData = True
            DData2 = True
            oldUser3 = message.author
            oldchannel3 = message.channel
        if message.content.startswith(f"{prefix}data access"):
            await message.channel.send("Reply to this message with the name of the category that you want to access. It is CAPS SENSTITVE. If you want to cancel the whole process, reply 'cancel' at any time")
            Adata = True
            Adata1 = True
            oldUser4 = message.author
            oldchannel4 = message.channel
        # ##############################ADD NEW COMMANDS HERE#################################

def readprefix(message):
    global prfx
    global prefix
    with open('prefix.txt', 'r') as myfile:
        for myline in myfile:
            if myline.find(str(message.guild)) != -1:
                prfx = str(myline)
                prfx = prfx.replace(f"{str(message.guild)} ", "")
                prfx = prfx.replace(f"\n", "")
    if prfx != "f":
        prefix = prfx
    if prfx == "f":
        prefix = "?"



@client.event
async def on_message(message):
    global messages
    global prefix
    global oldUser, oldUser2, oldUser3, oldUser4, oldUser5, oldChannel, oldchannel2, oldchannel3, oldchannel4, oldchannel5
    global boolSW, fields, var
    global green, purple, yellow, red, blue, black
    global Bgreen, Bpurple, Byellow, Bred, Bblue, Bblack
    global calc, roll
    global Ndata, Ndata1, Ndata2, Ndata3, Next, subsectionscompleted, CategoryName, x, subsectionName, subsectionValue
    global filer, DData, DData1, confirmedUser, DData2, Adata, Adata1
    messages += 1
    readprefix(message)
    # prefix = "!"
    id = client.get_guild(693537413448073328)
    channels = ["cmd", "current-commands"]
    god_users = ["Fireye#8983", "Vasu Kedia#6141"]
    basic_users = ["bumblebee#4138"]
    # place print(message.content) here to print out all messages
    # if calc == True and boolSW == True and oldUser == str(message.author):
    if Adata is True and message.author == oldUser4 and message.content.startswith("cancel") and message.channel == oldchannel4:
        async with message.channel.typing():
            Adata = False
            Adata1 = False
            await asyncio.sleep(0.5)
            await message.channel.send(f"Process Cancelled! :)")
    if Adata is True and Adata1 is True and message.author == oldUser4 and message.channel == oldchannel4:
        with open("data.txt", "r") as f:
            file3 = f.readlines()
            file4 = f.read()
            if file4.find(message.content):
                for line in file3:
                    if line.startswith(str(message.content)):
                        fields = line.strip("\n")
                        fields = fields.split(";")
                y = len(fields) - 2
                embedh = discord.Embed(title=f"{message.content}", Description=f"{message.content}'s subsections", color=3456491)
                for i in range(y):
                    var = fields[i+2].split(":")
                    embedh.add_field(name=f"{var[0]}", value=f"{var[1]}")
                await message.channel.send(embed=embedh)
                Adata = False
                Adata1 = False
            else:
                await message.channel.send(f"Sorry! No file with that name was found. Remember that it's caps sensitive. Try again or cancel.")
    if DData is True and message.author == oldUser3 and message.content.startswith("cancel") and message.channel == oldchannel3:
        async with message.channel.typing():
            DData = False
            DData1 = False
            DData2 = False
            await asyncio.sleep(0.5)
            await message.channel.send(f"Process Cancelled! :)")
    if DData is True and DData2 is True and message.author == oldUser3 and message.channel == oldchannel3:
        with open("data.txt", "r") as f:
            file1 = f.readlines()
            file2 = f.read()
            if file2.find(message.content):
                for line in file1:
                    if line.find(str(message.author)) != -1:
                        DData1 = True
                        DData2 = False
                        confirmedUser = True
                if confirmedUser is not True:
                    await message.channel.send(f"Sorry! Looks like you don't own that category! Ask the owner to delete it.")
                    async with message.channel.typing():
                        DData = False
                        DData1 = False
                        DData2 = False
                        await asyncio.sleep(0.5)
                        await message.channel.send(f"Process Cancelled! :(")
            else:
                await message.channel.send(f"Sorry! No file with that name was found. Remember that it's caps sensitive. Try again or cancel.")
    if DData is True and DData1 is True and message.author == oldUser3 and message.channel == oldchannel3:
        with open("data.txt", "r") as f:
            file = f.read()
            lines = f.readlines()
        if file.find(message.content) != -1:
            with open("data.txt", "w") as f:
                for line in lines:
                    if line.find(message.content) == -1:
                        f.write(line)
            await asyncio.sleep(0.5)
            await message.channel.send(f"Category deleted! :)")
            DData = False
            DData1 = False
        else:
            await message.channel.send(f"Sorry! No category with that name was found. Remember that it's caps sensitive. Try again or cancel.")
    if Ndata is True and message.author == oldUser2 and message.content.startswith("cancel") and message.channel == oldchannel2:
        async with message.channel.typing():
            Ndata = False
            Ndata1 = False
            Ndata2 = False
            Ndata3 = False
            Next = False
            with open("data.txt", "r") as f:
                lines = f.readlines()
            with open("data.txt", "w") as f:
                for line in lines:
                    if line.find(CategoryName) == -1:
                        f.write(line)
            await asyncio.sleep(0.5)
            await message.channel.send(f"Process Cancelled! :)")
    if Ndata is True and Ndata3 is True and message.author == oldUser2 and message.channel == oldchannel2:
        subsectionValue = str(message.content)
        if subsectionscompleted == 1:
            with open("data.txt", "r") as f:
                filer = f.read()
        if filer.find(CategoryName) != -1:
            await message.channel.send("Sorry! This category already exists! Please try again.")
            async with message.channel.typing():
                Ndata = False
                Ndata1 = False
                Ndata2 = False
                Ndata3 = False
                Next = False
                await asyncio.sleep(0.5)
                await message.channel.send(f"Process Cancelled! :(")
        else:
            with open("data.txt", "a") as f:
                if subsectionscompleted == 1:
                    f.write(CategoryName + ";")
                    f.write(str(message.author) + ";")
                    f.write(subsectionName + ":")
                    if x != 1:
                        f.write(subsectionValue + ";")
                    else:
                        f.write(subsectionValue + "\n")
                elif subsectionscompleted == x:
                    f.write(subsectionName + ":")
                    f.write(subsectionValue + "\n")
                else:
                    f.write(subsectionName + ":")
                    f.write(subsectionValue + ";")
            Ndata1 = True
            Ndata3 = False
    if Ndata is True and Ndata2 is True and message.author == oldUser2 and message.channel == oldchannel2:
        subsectionName = str(message.content)
        await message.channel.send(f"What is subsection {subsectionscompleted}'s value? (can be a number or a sentance)")
        Ndata3 = True
        Ndata2 = False
    if Ndata is True and Ndata1 is True and message.author == oldUser2 and message.channel == oldchannel2:
        try:
            if subsectionscompleted == 0:
                x = abs(int(message.content))
            subsectionscompleted += 1
            if subsectionscompleted <= x:
                await message.channel.send(f"What is subsection {subsectionscompleted}'s name?")
                Ndata2 = True
                Ndata1 = False
            else:
                async with message.channel.typing():
                    Ndata = False
                    Ndata1 = False
                    Ndata2 = False
                    Ndata3 = False
                    Next = False
                    await asyncio.sleep(1)
                    await message.channel.send(f"Process completed! {CategoryName} has been saved")

        except ValueError:
            await message.channel.send("Sorry! that looks like a word. Try again with a number")
    if Ndata is True and Next is True and message.author == oldUser2 and message.channel == oldchannel2:
        await message.channel.send("please enter the total number of subsections")
        CategoryName = message.content
        subsectionscompleted = 0
        Ndata1 = True
        Next = False

    
    

    ###########################ROLL###################################################3
    if boolSW is True and oldUser == str(message.author) and message.content == "cancel" and message.channel == oldChannel:
        boolSW = False
        Bgreen = False
        Bpurple = False
        Byellow = False
        Bred = False
        Bblue = False
        Bblack = False
        calc = False
        roll = False
        await message.channel.send("process cancelled. :)")
    if Bblack is True and boolSW is True and oldUser == str(message.author) and message.channel == oldChannel:
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
            async with message.channel.typing():
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
                await asyncio.sleep(1)
            # await message.channel.send(f"success: {success}\nadvantage: {advantage}\nfailure: {failure}\nthreat: {threat}\ntriumph: {triumph}\ndespair: {despair}")
            sf = success - failure
            at = advantage - threat
            embedSW = discord.Embed(title=f"""Results""", Description="the results of your roll!",color=3456491)

            if sf >= 0:
                embedSW.add_field(name=f"success: ", value=f"{abs(sf)}")
            elif sf < 0:
                embedSW.add_field(name=f"failure: ", value=f"{abs(sf)}")
            if at >= 0:
                embedSW.add_field(name=f"advantage: ", value=f"{abs(at)}")
            elif at < 0:
                embedSW.add_field(name=f"threat: ", value=f"{abs(at)}")
            if triumph > 0:
                embedSW.add_field(name=f"triumph: ", value=f"{triumph}")
            if despair > 0:
                embedSW.add_field(name=f"despair: ", value=f"{despair}")
            await message.channel.send(embed=embedSW)
            boolSW = False
            calc = False
    if Bblue is True and boolSW is True and oldUser == str(message.author) and message.channel == oldChannel:
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
    if Bred is True and boolSW is True and oldUser == str(message.author) and message.channel == oldChannel:
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
    if Byellow is True and boolSW is True and oldUser == str(message.author) and message.channel == oldChannel:
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
    if Bpurple is True and boolSW is True and oldUser == str(message.author) and message.channel == oldChannel:
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
    if Bgreen is True and boolSW is True and oldUser == str(message.author) and message.channel == oldChannel:
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
    if boolSW is True and oldUser is str(message.author) and message.content == "roll" or "Roll" and message.channel == oldChannel:
        await message.channel.send("how many green dice?")
        Bgreen = True
        roll = False










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

"""
@client.event
async def on_member_join(member):
    global basic_users
    global joined
    joined += 1
    print(f"{member} has joined the server!")
    for channel in member.
        if str(channel) == "general":
            await client.send_message(f"Welcome to the server, {member.mention}! I am the almighty BotGod!)
"""

# constantly update stats
client.loop.create_task(update_stats())
# run token
client.run(token)
