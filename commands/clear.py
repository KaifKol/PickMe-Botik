import disnake
from disnake.ext import commands
from utils.has_role import has_role_by_id
from styles import color

class ClearCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(name="clear", description="удалить сооооообщениеее!")
    async def clear(self, interaction: disnake.ApplicationCommandInteraction, limit: int = commands.Param(name="кол-вооо", default=0)):
        if not has_role_by_id(interaction, role_id=1322300234235383939):
            await interaction.response.send_message("У тебя нету разрешения на использование этой командыыы {(>_<)} ", ephemeral=True)
            return
        if limit < 1:
            await interaction.response.send_message("Ты не указал число! Укажи его (❁´◡`❁)", ephemeral=True)
            return
        await interaction.response.defer()
        count_deleted = await interaction.channel.purge(limit=limit)
        
        clearembed = disnake.Embed(
            title=f"Покааа!!! - {len(count_deleted)-1} сообщений  ╰(*°▽°*)╯",
            color=color.primary
        )

        await interaction.channel.send(embed=clearembed, delete_after=3)


def setup(bot: commands.Bot):
    bot.add_cog(ClearCommand(bot))