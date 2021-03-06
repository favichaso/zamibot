from discord.ext import commands


class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        print("greet init")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('Welcome {0.mention}.'.format(member))

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content == "あほ":
            member = message.author
            channel = member.guild.system_channel
            if channel is not None:
                await channel.send('Welcome {0.mention}.'.format(member))

    @commands.command()
    async def hello(self, ctx):
        """helloと言う"""
        member = ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send('Hello {0.name}~'.format(member))
        else:
            await ctx.send('Hello {0.name}... This feels familiar.'.format(member))
        self._last_member = member


def setup(bot):
    bot.add_cog(Greetings(bot))


def setconfig(config):
    # greetings.config = config
    pass
