import discord
from discord.ext import commands
from discord.utils import get
from discord import channel
import string

TOKEN = 'Njk0OTYyNjkxMjkwMTY5MzU0.XoUpNA.owfpukXyNi1iqtImrLe5TSJYSwQ'
client = discord.Client()
Current_Playing = discord.Game("with numbers")
prefix = "?" #Define prefix for bot
idtoggle = False

client = commands.Bot(command_prefix ='?')
client.remove_command('help')

@client.event
async def on_ready():
    print(f'Logged in as: {client.user.name}')
    print(f'With ID: {client.user.id}')
    #await client.change_presence(activity= Current_Playing)
    #await client.change_presence(status = discord.Status.offline)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="to no one"))
"""
@client.command()
async def addrole(ctx):
    print("Adding role")
    member = ctx.message.author
    role = get(ctx.guild.roles, name="Admin_03")
    await client.add_roles(member,role)
"""  
@client.command()
async def purge(ctx,limit):
    try:
        delete = await ctx.channel.purge(limit = int(limit) + 1, bulk = True)
        await ctx.send(str(ctx.message.author) + ' Deleted {} message(s)'.format(len(delete)))
    

    except ValueError:
        await ctx.send('Invalid use of command, for help use ?help')
    

@client.command()
async def help(ctx):
    embed = discord.Embed(
        title = 'Help page',
        description = 'This is the help page (WIP)'
    )
    embed.set_image(url='https://discordemoji.com/assets/emoji/2788_stupid.png')
    embed.set_footer(text='Laget av Alexander Gnauck 3ELDEA')

    await ctx.send(embed = embed)
    pass

client.run(TOKEN)