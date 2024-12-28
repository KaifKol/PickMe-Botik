import disnake
from disnake.ext import commands

class PingCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(name="ping", description="узнать мою задержку.. o((>ω< ))o")
    async def ping(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.send_message(f"Задержка: {round(self.bot.latency * 1000)}мс （＞人＜；）")

def setup(bot: commands.Bot):
    bot.add_cog(PingCommand(bot))