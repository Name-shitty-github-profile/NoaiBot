from nextcord.ext import commands
import nextcord
class Serverinfo(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @nextcord.slash_command(name = "serveurinfo", description = "Te donne les informations du serveur")
  async def serverinfoslash(self, interaction: nextcord.Interaction, ephemeral: bool = nextcord.SlashOption(name="ephemeral", description="Est ce que tu veux que la visibilitée de cette commande soit seulement pour toi?", required=False)):
    server = interaction.guild
    roles = [x.name for x in server.roles]
    role_length = len(roles)
    if role_length > 50:
      roles = len(roles)
    else:
      roles = ', '.join(roles)
    join = nextcord.Embed(title = f'Information de {server.name}', color = 0x9b59b6);
    join.set_thumbnail(url = server.icon.url);
    join.add_field(name = 'Propriétaire', value = f'{server.owner.name} ({server.owner.id})')
    join.add_field(name = 'Id', value=  str(server.id))
    join.add_field(name = 'Membres', value = str(server.member_count))
    join.add_field(name = 'Salons', value = str(len(server.channels)))
    join.add_field(name = 'Roles', value = str(roles))
    join.set_footer(text = f'Création: {str(server.created_at).split(" ")[0]}')
    await interaction.response.send_message(embed=join, ephemeral = ephemeral is True)

def setup(bot):
  bot.add_cog(Serverinfo(bot))
