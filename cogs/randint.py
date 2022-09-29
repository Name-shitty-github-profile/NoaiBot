from nextcord.ext import commands
import nextcord
from random import randint
class Randint(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @nextcord.slash_command(name = "randint", description = "Te genere un nombre au hazard")
  async def randintslash(self, interaction: nextcord.Interaction, min: int = nextcord.SlashOption(name="minimum", description="Le nombre minimum"), max: int = nextcord.SlashOption(name="maximum", description="Le nombre maximum"), ephemeral: bool = nextcord.SlashOption(name="ephemeral", description="Est ce que tu veux que la visibilitée de cette commande soit seulement pour toi?", required=False)):
    if min > max:
      await interaction.response.send_message(content = f"Ton nombre minimum ({min}) est plus gros que ton nombre maximum ({max})", ephemeral = True)
      return None
    await interaction.response.send_message(embed=nextcord.Embed(title=f'Nombre au hazard entre {min} et {max}', description=str(randint(min, max)), color=0x9b59b6), ephemeral=ephemeral is True)

def setup(bot):
  bot.add_cog(Randint(bot))
