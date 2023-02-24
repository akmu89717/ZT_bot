import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = '[')

@bot.event
async def on_ready():
    print(">>Bot is onlone")

bot.run('MTA3ODY2NzM4MTkxNzg5NjcyNw.GkslB6.C-w5BwE8YGm9yW5AKsqTYF7OCiL5eGfFnvThYM')