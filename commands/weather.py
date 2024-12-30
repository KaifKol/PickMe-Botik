import disnake

from disnake.ext import commands
from styles import color

import requests

import os
from dotenv import load_dotenv
load_dotenv() 

class WeatherCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot



    @commands.slash_command(description="Узнать текущую погоду в указанном городе. (Работает хуево)")
    async def weather(interaction: disnake.ApplicationCommandInteraction, city: str):
        await interaction.response.defer()  # Отложенный ответ

        API_KEY = os.getenv("WEATHER_API")
        BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric",
            "lang": "ru"
        }
        try:
            response = requests.get(BASE_URL, params=params)
            response.raise_for_status()
            data = response.json()

            if data.get("cod") == "404":
                await interaction.followup.send(f"Город '{city}' не найден. Попробуйте указать точное название.")
                return

            #print(f"Данные API: {data}")

            weather_desc = data["weather"][0]["description"].capitalize()
            temp = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

            embed = disnake.Embed(
                title=f"Погода в городе {city.capitalize()}",
                description=f"{weather_desc}",
                color=color.primary
            )
            embed.add_field(name="Температура", value=f"{temp}°C", inline=True)
            embed.add_field(name="Ощущается как", value=f"{feels_like}°C", inline=True)
            embed.add_field(name="Влажность", value=f"{humidity}%", inline=True)
            embed.add_field(name="Скорость ветра", value=f"{wind_speed} м/с", inline=True)
            embed.set_footer(text="Данные предоставлены OpenWeatherMap")

            await interaction.followup.send(embed=embed)
        except requests.exceptions.RequestException as e:
            await interaction.followup.send("Ошибка при запросе данных погоды. Попробуйте позже.")
            print(f"Ошибка API: {e}")
        except Exception as e:
            await interaction.followup.send("Произошла неизвестная ошибка.")
            print(f"Неизвестная ошибка: {e}")


def setup(bot: commands.Bot):
    bot.add_cog(WeatherCommand(bot))