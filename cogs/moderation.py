from discord.ext import commands
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ban")
    @has_permissions(ban_members=True)
    async def ban(self, ctx, member: Member, *, reason=None):
        """Ban a member from the server"""
        try:
            await member.ban(reason=reason)
            await ctx.send(f'{member.mention} has been banned for: {reason}')
        except Exception as e:
            await ctx.send(f'Failed to ban {member.mention}: {e}')

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("You don't have the permission to ban members.")

async def setup(bot):
    await bot.add_cog(Moderation(bot))