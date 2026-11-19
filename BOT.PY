import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

@bot.command()
async def hola(ctx):
    await ctx.send(f"¡Hola {ctx.author.mention}! Ya estoy en línea.")

token = os.getenv("DISCORD_TOKEN")
bot.run(token)
