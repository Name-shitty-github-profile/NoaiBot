from nextcord.ext import commands
import nextcord
from utils import checkperm
class Clear(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @nextcord.slash_command(name = "clear", description = "Supprime des messages")
  async def clearslash(self, interaction: nextcord.Interaction, nombre: int = nextcord.SlashOption(name="nombre", description='le nombre de message a supprimer'), ephemeral: bool = nextcord.SlashOption(name="ephemeral", description="Est ce que tu veux que la visibilitée de cette commande soit seulement pour toi?", required=False)):
    if checkperm(interaction.user, ['manage']) is False:
      await interaction.response.send_message(content="Tu dois avoir la permission pour faire ctte commande", ephemeral=True)
      return None
    await interaction.channel.purge(limit=nombre)
    await interaction.response.send_message(content=f"{nombre} messages supprimés", ephemeral=ephemeral is True)
    return None

def setup(bot):
  bot.add_cog(Clear(bot))
