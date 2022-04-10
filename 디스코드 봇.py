import discord
from discord.ext import commands
from idna import valid_contextj

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    print(bot.user.name)
    print('connection was succesful')
    await bot.change_presence(status=discord.Status.online, activity=None)
   
@bot.command()
async def 따라하기(ctx, *, text):
    await ctx.send(text)

bot.run('OTQwMTYxNDg0OTkyOTUwMzEy.YgDXnQ.sPF8S08HBLIpI4ey4jULZkG0B4o')