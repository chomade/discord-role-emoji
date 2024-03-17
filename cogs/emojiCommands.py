import discord
import os
import json
from discord.ext import commands


class Emoji(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    default_emojis = []
    custom_emojis = []
    with open("defaultEmojis.json", encoding='utf8') as f:
        default_emojis = json.load(f)
    with open("customEmojis.json", encoding='utf8') as f:
        custom_emojis = json.load(f)
    # [커스텀 이모지 이름, 역할 이름]

    @commands.bot_has_permissions(administrator=True)
    @commands.has_permissions(administrator=True)
    @commands.hybrid_command(name="설정", description="settings")
    async def settings(self, interaction: discord.Interaction):
        embed = discord.Embed(description="역할을 선택하세요.", color=discord.Color.blurple())
        text = await interaction.channel.send(embed=embed)
        for i in self.default_emojis:
            await text.add_reaction(i['emoji'])

        # 커스텀 이모지
        for i in self.custom_emojis:
            emoji = discord.utils.get(interaction.guild.emojis, name=i["emoji_name"])
            await text.add_reaction(emoji)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        channel = self.bot.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        sender = message.author
        if str(sender) == str(self.bot.user):
            if payload.user_id == self.bot.user.id:
                return
            for i in self.default_emojis:
                if payload.emoji.name == i['emoji']:
                    role = discord.utils.get(payload.member.guild.roles, name=i["role"])
                    await payload.member.add_roles(role)

            for i in self.custom_emojis:
                if payload.emoji.name == i["emoji_name"]:
                    role = discord.utils.get(payload.member.guild.roles, name=i["role"])
                    await payload.member.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload: discord.RawReactionActionEvent):
        guild = self.bot.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)
        channel = self.bot.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        sender = message.author
        if str(sender) == str(self.bot.user):
            for i in self.default_emojis:
                if payload.emoji.name == i['emoji']:
                    role = discord.utils.get(member.guild.roles, name=i["role"])
                    await member.remove_roles(role)

            for i in self.custom_emojis:
                if payload.emoji.name == i["emoji_name"]:
                    role = discord.utils.get(member.guild.roles, name=i["role"])
                    await member.remove_roles(role)


async def setup(bot):
    await bot.add_cog(Emoji(bot))