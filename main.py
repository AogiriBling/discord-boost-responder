import discord
from discord.ext import commands
import os
from webserver import keep_alive

TOKEN = os.environ['TOKEN']
my_secret = os.environ['TOKEN']
bot_prefix = '.'

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=bot_prefix, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.event
async def on_member_update(before, after):
    guild = before.guild
    boost_channel_id = 920847057500127273  # change the channel id in which you want the message to be sent, example : Bling's boost channel

    if len(before.roles) < len(after.roles):
        for role in after.roles:
            if role.is_premium_subscriber():
                boost_channel = guild.get_channel(boost_channel_id)
                await boost_channel.send(f'**Thank you, {after.mention}, for boosting Aogiri Tree v2! <3**')

keep_alive()
bot.run(TOKEN)
