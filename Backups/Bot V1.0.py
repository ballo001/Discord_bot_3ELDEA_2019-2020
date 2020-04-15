import discord
import string
from discord import channel
TOKEN = ''
client = discord.Client()
Current_Playing = discord.Game("with numbers")
prefix = "?" #Define prefix for bot
idtoggle = False

@client.event
async def on_ready():
    print(f'Logged in as: {client.user.name}')
    print(f'With ID: {client.user.id}')
    #await client.change_presence(activity= Current_Playing)
    #await client.change_presence(status = discord.Status.offline)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="to no one"))

@client.event
async def on_message(message):
    global idtoggle
    if message.author == client.user:
        return
    
    if idtoggle == True:
        await message.channel.send("Message id is: " + str(message.id))
        pass

    if message.content.startswith(prefix): #Check if command

        if "purge" in message.content.lower():
            try:
                message_int = int(''.join(filter(str.isdigit, message.content)))
                print("Deleting " + str(message_int) + " messages")
                delete = await message.channel.purge(limit=message_int+1, bulk = True)
                await message.channel.send(str(message.author) + ' Deleted {} message(s)'.format(len(delete)))
            except ValueError:
                await message.channel.purge(limit=1)
                await message.channel.send("Invalid syntax, example usage of command is '?Purge 1' \nfor more help see '?help'")
            return

        if "toggleid" in message.content.lower():
            if idtoggle == True:
                idtoggle = False
                print("Not showing message id")
                await message.channel.purge(limit=2,bulk=True)
                await message.channel.send("No longer showing message id",delete_after=5)
                pass
            else:
                idtoggle = True
                print("Now showing message id")
                await message.channel.purge(limit=1)
                await message.channel.send("Now showing message id",delete_after=5)
                pass

        if "help" in message.content.lower():
            await message.channel.purge(limit=1)
            await message.channel.send("The bot prefix is '?' and the following Commands are availabe:\n?help wil display this message\n?toggleid wil toggle the the bot from sending message id`s \n?purge (num) where num is a number between 0 - 99 this will delete (num) ammount of messages")
            pass
    return 
client.run(TOKEN)