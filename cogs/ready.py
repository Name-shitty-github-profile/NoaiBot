from nextcord.ext import commands
from nextcord import Game
from random import randint
from secret_things import statuslist as status
stlen = len(status)
def randomst(client) -> str:
  return 'Made with love, not like the author'
  try:
    return status[randint(0, stlen)]
  except:
    return f"{len(client.guilds)} serveurs"

class Ready(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener('on_ready')
  async def ready(self):
    print("online")
    while True:
      await self.bot.change_presence(activity=Game(randomst(self.bot)))

def setup(bot):
  bot.add_cog(Ready(bot))
