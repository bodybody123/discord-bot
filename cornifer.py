import discord
from discord.ext import commands

client = commands.Bot(command_prefix='c!')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def ping(ctx):
    await print(f'pong {round(client.latency * 1000)}ms')

@client.command()
async def test(ctx, arg):
    await ctx.send(arg)

client.run('OTI4NTM2Mjg2MDE5NTk2MzE5.YdaMzQ.gU0glq9NtLjjfhI9M4W6nAqe3zk')
