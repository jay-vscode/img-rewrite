import discord
from discord.ext import commands
import asyncio
from themes import coloring

async def type(ctx):
    async with ctx.typing():
            await asyncio.sleep(0.2)

class IMGBRANDING(discord.ui.View):
    @discord.ui.button(label="IMG", style=discord.ButtonStyle.blurple, disabled=True)
    async def IMGButton1(self, button, interaction):
        await interaction.response.send_message("Woah how did you click this button") 

    @discord.ui.button(label="@w3mbu", style=discord.ButtonStyle.green, disabled=True)
    async def MIDDLE(self, button, interaction):
        await interaction.response.send_message("Woah how did you click this button") 

class Developer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def ping(self, ctx):
        await type(ctx)
        embed = discord.Embed(title='Pong!', description=f'Pong! {round(self.bot.latency * 1000)}ms', color=coloring.GRAY)
        await ctx.send(embed=embed, view=IMGBRANDING())

    @commands.command()
    @commands.is_owner()
    async def guilds(self, ctx):
        guild_info = []
        for guild in self.bot.guilds:
            bot_member = guild.get_member(self.bot.user.id)
            join_date = bot_member.joined_at.strftime('%m/%d/%Y') if bot_member else 'N/A'
            bot_role = discord.utils.get(guild.roles, name='Your Bot Role Name')  # replace with your bot role name
            
            guild_info.append(f"{guild.name:<25} {guild.id:<20} {join_date:<20} {bot_role.name if bot_role else 'N/A'}")
        
        file_content = '\n'.join(guild_info)
        with open('tmp/guilds_info.txt', 'w', encoding='utf-8') as file:
            file.write(file_content)
        
        await ctx.send(file=discord.File('tmp/guilds_info.txt'))
                              
async def setup(bot):
    await bot.add_cog(Developer(bot))