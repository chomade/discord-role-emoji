import discord
import traceback
import os
import sys

from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Context
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents)

initial_extensions = ['cogs.emojiCommands']


@bot.event
async def on_ready():
    print(1)
    for extension in initial_extensions:
        try:
            await bot.load_extension(extension)
            print(f"Loaded {extension}")
        except Exception as e:
            print(f"Failed to load extension {extension}. Caused py {e}.", file=sys.stderr)
            traceback.print_exc()
    print(2)
    print(3)
    print("Bot is ready!")


@bot.event
async def on_command_error(context: Context, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(description="권한이 없습니다.", color=discord.Color.red())
        await context.send(embed=embed, ephemeral=True)
    elif isinstance(error, commands.BotMissingPermissions):
        embed = discord.Embed(description="봇이 권한이 없습니다.", color=discord.Color.red())
        await context.send(embed=embed, ephemeral=True)
    elif isinstance(error, commands.NotOwner):
        embed = discord.Embed(description="봇 소유자만 사용할 수 있는 명령어입니다.", color=discord.Color.red())
        await context.send(embed=embed, ephemeral=True)
    elif isinstance(error, commands.CommandOnCooldown):
        minutes, seconds = divmod(error.retry_after, 60)
        hours, minutes = divmod(minutes, 60)
        hours = hours % 24
        embed = discord.Embed(
            description=f" {f'{round(hours)} 시간' if round(hours) > 0 else ''}"
                        f" {f'{round(minutes)} 분' if round(minutes) > 0 else ''}"
                        f" {f'{round(seconds)} 초' if round(seconds) > 0 else ''} 뒤에 사용 하실 수 있습니다.",
            color=discord.Color.red()
        )
        await context.send(embed=embed, ephemeral=True)
    elif isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, app_commands.errors.CommandNotFound):
        return
    elif isinstance(error, commands.MissingRequiredArgument):
        if error.param.name == "amount":
            embed = discord.Embed(description="청소할 메시지의 수를 입력해주세요.", color=discord.Color.red())
            await context.send(embed=embed, ephemeral=True)
        else:
            embed = discord.Embed(title="Error!", description=str(error).capitalize(), color=discord.Color.red())
            await context.send(embed=embed, ephemeral=True)
    else:
        raise error

bot.run(os.getenv("TOKEN"))
