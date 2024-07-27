import discord
from discord.ext import commands

class add_roles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def add_role(self, ctx, member: discord.Member, role: discord.Role):
        await member.add_roles(role)
        await ctx.send(f"{member.mention} has been given the role {role.mention}.")

    @add_role.error
    async def add_role_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have the required permissions to execute this command.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Invalid argument provided.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Usage: !add_role <username> <role>')
            if instantanceof(error, commands.rolenotfounderror):
                await ctx.send('Role not found.')


    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def remove_role(self, ctx, member: discord.Member, role: discord.Role):
        await member.remove_roles(role)
        await ctx.send(f"{member.mention} has been removed from the role {role.mention}.")

    @remove_role.error
    async def remove_role_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have the required permissions to execute this command.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Invalid argument provided.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Usage: !remove_role <username> <role>')

async def setup(bot):
    await bot.add_cog(add_roles(bot))