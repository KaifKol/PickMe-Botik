import disnake
from disnake.ext import commands
import os
from dotenv import load_dotenv
load_dotenv() 

#TODO: начальная настройка
bot = commands.Bot(command_prefix="?")
bot.remove_command("help")

#TODO: действия при запуске
@bot.event
async def on_ready():
    print("Я запущена!!! ^_^")

    activity = disnake.Activity(
        name="Я ПИКМИ!!! (｡･∀･)ﾉﾞ",
        type=disnake.ActivityType.playing,
    )

    await bot.change_presence(status=disnake.Status.idle, activity=activity)




#TODO: чистить
bot.load_extension("commands.clear")

#TODO: 

    
#TODO: запуск
bot.run(os.getenv("DISCORD_TOKEN"))