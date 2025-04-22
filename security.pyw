import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime
import os
import subprocess
import pyautogui

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

TOKEN = 'YOUR_TOKEN_HERE'

@bot.event
async def on_ready():
    channel = bot.get_channel(YOUR_CHANNEL_ID_HERE)
    username = os.environ.get('USERNAME')

    embed = discord.Embed(
        title="The computer was on",
        description=f"**Logged user:** `{username}`\n**Time:** `{datetime.now().strftime('%H:%M:%S')}`\n**Date:** `{datetime.now().strftime('%d.%m.%Y')}`",
        color=0x00ff00
    )

    await channel.send("<@YOUR_ID_HERE> computer has been started.", embed=embed)

    try:
        synced = await bot.tree.sync()
        print(f"Slash commands synchronized: {len(synced)}")
    except Exception as e:
        print(f"Error with synchronization: {e}")

@bot.tree.command(name="lock", description="Lock user's computer.")
@app_commands.describe(username="Username")
async def lock(interaction: discord.Interaction, username: str):
    current_username = os.environ.get('USERNAME')

    if username.lower() == current_username.lower():
        try:
            temp_path = os.path.join(os.environ.get("TEMP"), "securityscr.png")
            pyautogui.screenshot(temp_path)

            file = discord.File(temp_path, filename="screenshot.png")

            embed = discord.Embed(
                title="🔒 The computer was secured",
                description=f"User `{username}` was just locked and the screen was captured.",
                color=0xff0000
            )
            embed.set_image(url="attachment://screenshot.png")

            await interaction.channel.send(embed=embed, file=file)

            os.remove(temp_path)
        except Exception as e:
            await interaction.channel.send(f"⚠️ Error creating or sending screenshot: {e}")

        try:
            subprocess.Popen(["cmd", "/c", "start", "", "C:\\security.bat"], shell=True)
        except Exception as e:
            await interaction.channel.send(f"❌ Failed to run security.bat: {e}")
    else:
        await interaction.response.send_message(f"User `{username}` not found or not authorized.", ephemeral=True)

@bot.tree.command(name="unlock", description="Unlocks user's computer.")
@app_commands.describe(username="Username")
async def unlock(interaction: discord.Interaction, username: str):
    current_username = os.environ.get('USERNAME')

    if username.lower() == current_username.lower():
        try:
            temp_path = os.path.join(os.environ.get("TEMP"), "unlockscr.png")
            pyautogui.screenshot(temp_path)

            file = discord.File(temp_path, filename="unlock.png")

            embed = discord.Embed(
                title="🔓 Počítač byl odblokován",
                description=f"User `{username}` was successfully unlocked.\nThe unlock screen was captured below.",
                color=0x00ccff
            )
            embed.set_image(url="attachment://unlock.png")

            await interaction.channel.send(embed=embed, file=file)

            os.remove(temp_path)
        except Exception as e:
            await interaction.channel.send(f"⚠️ Error creating or sending screenshot: {e}")

        try:
            subprocess.Popen(["cmd", "/c", "start", "", "C:\\security.bat", "-unlock"], shell=True)
        except Exception as e:
            await interaction.channel.send(f"❌ Failed to run security.bat {e}")
    else:
        await interaction.response.send_message(f"User `{username}` not found or not authorized.", ephemeral=True)


bot.run(TOKEN)
