from nextcord.ext import commands
import nextcord
class Ping(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @nextcord.slash_command(name = "ping", description = "Te donne le ping du bot")
  async def pingslash(self, interaction: nextcord.Interaction, ephemeral: bool = nextcord.SlashOption(name="ephemeral", description="Est ce que tu veux que la visibilitée de cette commande soit seulement pour toi?", required=False)):
    await interaction.response.send_message(embed=nextcord.Embed(title='Pong !', description=f"Ping : `{int(self.bot.latency*1000)} ms`", color=0x9b59b6), ephemeral=ephemeral is True)

def setup(bot):
  bot.add_cog(Ping(bot))
