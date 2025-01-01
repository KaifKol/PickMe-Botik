import disnake
from disnake.ext import commands

from datetime import datetime

import os
from dotenv import load_dotenv
load_dotenv() 

intents = disnake.Intents.all()

#TODO: начальная настройка
bot = commands.Bot(command_prefix=commands.when_mentioned, intents=intents, reload=True)
bot.remove_command("help")

#TODO: действия при запуске
@bot.event
async def on_ready():
    launch_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Я запущена!!! ^_^ Время запуска: {launch_time}")

    activity = disnake.Activity(
        name="Я ПИКМИ!!! (｡･∀･)ﾉﾞ",
        type=disnake.ActivityType.playing,
    )

    await bot.change_presence(status=disnake.Status.idle, activity=activity)




#TODO: чистить
bot.load_extension("commands.clear")

#TODO: пинг
bot.load_extension("commands.ping")

#TODO: погода
bot.load_extension("commands.weather")
    
#TODO: запуск
bot.run(os.getenv("DISCORD_TOKEN"))