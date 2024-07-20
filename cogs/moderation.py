## ban/unban

import discord
from discord.ext import commands

class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        try:
            await member.send(f'You have been banned in {ctx.guild.name} for: {reason}')
            await ctx.send(f'User {member.mention} has been muted. Reason: {reason}')
        except Exception as e:
            await ctx.send(f'Failed to ban {member.mention}. Error: {e}')

    @ban.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have the required permissions to execute this command.")
        elif isinstance(error, commands.MemberNotFound):   
            await ctx.send("Member not found.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Invalid argument provided.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Usage: !mute <username> [reason]')

            @commands.command()
            @commands.has_permissions(ban_members=True)
            async def unban(self, ctx, *, member):
                banned_users = await ctx.guild.bans()
                member_name, member_discriminator = member.split('#')

                for ban_entry in banned_users:
                    user = ban_entry.user

                    if (user.name, user.discriminator) == (member_name, member_discriminator):
                        await ctx.guild.unban(user)
                        await ctx.send(f'Unbanned {user.mention}')
                        return

                await ctx.send('Member not found.')

            @unban.error
            async def unban_error(self, ctx, error):
                if isinstance(error, commands.MissingPermissions):
                    await ctx.send("You don't have the required permissions to execute this command.")
                elif isinstance(error, commands.MemberNotFound):
                    await ctx.send("Member not found.")
                elif isinstance(error, commands.BadArgument):
                    await ctx.send("Invalid argument provided.")
                elif isinstance(error, commands.MissingRequiredArgument):
                    await ctx.send('Usage: !unban <username> [reason]')

################################################################################################################################################################################################

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def warn(self, ctx, member: discord.Member, *, reason=None):
        try:
            await member.send(f'You have been warned in {ctx.guild.name} for: {reason}')
            await ctx.send(f'User {member.mention} has been warned. Reason: {reason}')
        except Exception as e:
            await ctx.send(f'Failed to warn {member.mention}. Error: {e}')

    @warn.error
    async def warn_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have the required permissions to execute this command.")
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send("Member not found.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Invalid argument provided.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Usage: !warn <username> [reason]')

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def unwarn(self, ctx, member: discord.Member, *, reason=None):
        try:
            await member.send(f'You have been unwarned in {ctx.guild.name} for: {reason}')
            await ctx.send(f'User {member.mention} has been unwarned. Reason: {reason}')
        except Exception as e:
            await ctx.send(f'Failed to unwarn {member.mention}. Error: {e}')

    @unwarn.error
    async def unwarn_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have the required permissions to execute this command.")
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send("Member not found.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Invalid argument provided.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Usage: !unwarn <username> [reason]')

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def clearwarns(self, ctx, member: discord.Member):
        try:
            await member.send(f'You have been cleared warns in {ctx.guild.name}')
            await ctx.send(f'User {member.mention} has been cleared warns.')
        except Exception as e:
            await ctx.send(f'Failed to clear warns for {member.mention}. Error: {e}')

    @clearwarns.error
    async def clearwarns_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have the required permissions to execute this command.")
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send("Member not found.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Invalid argument provided.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Usage: !clearwarns <username>')

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def listwarns(self, ctx, member: discord.Member):
        try:
            await ctx.send(f'User {member.mention} has {len(member.warnings)} warns.')
        except Exception as e:
            await ctx.send(f'Failed to list warns for {member.mention}. Error: {e}')

    @listwarns.error
    async def listwarns_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have the required permissions to execute this command.")
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send("Member not found.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Invalid argument provided.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Usage: !listwarns <username>')

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def getwarns(self, ctx, member: discord.Member):
        try:
            await ctx.send(f'User {member.mention} has {len(member.warnings)} warns.')
        except Exception as e:
            await ctx.send(f'Failed to get warns for {member.mention}. Error: {e}')

    @getwarns.error
    async def listwarns_error(self, ctx, error):
        if insitance(error, commands.MissingPermissions):
            await ctx.send ("You don't have the required permissions to execute this command.")
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send("Member not found.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Invalid argument provided.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Usage: !getwarns <username>')

########################################################################kick######################################################################################################################
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        try:
            await member.send(f'You have been kicked from {ctx.guild.name} for: {reason}')
            await ctx.send(f'User {member.mention} has been kicked. Reason: {reason}')
        except Exception as e:
            await ctx.send(f'Failed to kick {member.mention}. Error: {e}')

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have the required permissions to execute this command.")
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send("Member not found.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Invalid argument provided.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Usage: !kick <username> [reason]')

################################################################################################################################################################################################


    @commands.command(name="mute")
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        """Mute a member in the server"""
        mute_role = get(ctx.guild.roles, name="Muted")
        if not mute_role:
            # Create Muted role if it doesn't exist
            mute_role = await ctx.guild.create_role(name="Muted")
            for channel in ctx.guild.channels:
                await channel.set_permissions(mute_role, speak=False, send_messages=False, read_message_history=True, read_messages=False)

        await member.add_roles(mute_role, reason=reason)
        await ctx.send(f"Muted {member.mention} for reason: {reason}")

    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have the required permissions to execute this command.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Invalid argument provided.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Usage: !mute <username> [reason]')

    @commands.command(name="unmute")
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx, member: discord.Member):
        """Unmute a member in the server"""
        mute_role = get(ctx.guild.roles, name="Muted")
        if mute_role in member.roles:
            await member.remove_roles(mute_role)
            await ctx.send(f"Unmuted {member.mention}")
        else:
            await ctx.send(f"{member.mention} is not muted")

    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permission to mute members.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Member not found.")
        else:
            await ctx.send("An error occurred. Please try again.")

    @unmute.error
    async def unmute_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permission to unmute members.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Member not found.")
        else:
            await ctx.send("An error occurred. Please try again.")

################################################################################################################################################################################################


async def setup(bot):
    await bot.add_cog(moderation(bot))
