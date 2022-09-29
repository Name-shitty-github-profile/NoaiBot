from nextcord.ext import commands
import nextcord
import requests
from random import randint
from json import loads
from os import environ
class Image(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @nextcord.slash_command(name = "image", description = "Te donne un image de quelque chose au hazard selon ton theme")
  async def imageslash(self, interaction: nextcord.Interaction, theme: str = nextcord.SlashOption(name="theme", description="Le theme de l'image"), ephemeral: bool = nextcord.SlashOption(name="ephemeral", description="Est ce que tu veux que la visibilitée de cette commande soit seulement pour toi?", required=False)):
    r = requests.get(f'https://api.pexels.com/v1/search?query={theme}', headers={"Authorization": environ['pexel']})
    content = loads(r.content.decode('utf-8'))
    try:
      await interaction.response.send_message(embed=nextcord.Embed(title=f"Photo de {theme}", color=0x3498db).set_image(content['photos'][randint(0, len(content['photos']))]['src']['original']), ephemeral=ephemeral is True)
    except:
      await interaction.response.send_message(f"Aucun resultat pour {theme}", ephemeral=ephemeral is True)

def setup(bot):
  bot.add_cog(Image(bot))
