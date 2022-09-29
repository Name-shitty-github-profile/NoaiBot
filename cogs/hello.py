from nextcord.ext import commands
import nextcord
import psutil
class Hello(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @nextcord.slash_command(name = "hello", description = "Te donne les specs eletronique du bot")
  async def helloslash(self, interaction: nextcord.Interaction, ephemeral: bool = nextcord.SlashOption(name="ephemeral", description="Est ce que tu veux que la visibilitée de cette commande soit seulement pour toi?", required=False)):
    await interaction.response.send_message(embed=nextcord.Embed(title='World !', description=f"**[Source](https://github.com/Name-shitty-github-profile/NoaiBot)**\n**Language** : Python\n**CPU** : {int(psutil.cpu_percent())}\n**Ram**: {int(psutil.virtual_memory().percent)}\n**Ping** : `{int(self.bot.latency*1000)} ms`", color=0x9b59b6), ephemeral=ephemeral is True)

def setup(bot):
  bot.add_cog(Hello(bot))
