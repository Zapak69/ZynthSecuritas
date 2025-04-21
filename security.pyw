import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime
import os
import subprocess

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

TOKEN = 'YOUR_TOKEN_HERE'

@bot.event
async def on_ready():
    channel = bot.get_channel(YOUR_CHANNEL_ID_HERE)
    
    username = os.environ.get('USERNAME')
    
    embed = discord.Embed(
        title="Počítač byl zapnut",
        description=f"**Přihlášený uživatel:** `{username}`\n**Čas:** `{datetime.now().strftime('%H:%M:%S')}`\n**Datum:** `{datetime.now().strftime('%d.%m.%Y')}`",
        color=0x00ff00
    )

    await channel.send("<@YOUR_ID_HERE> počítač byl zapnut.", embed=embed)

    # Synchronizace slash příkazů
    try:
        synced = await bot.tree.sync()
        print(f"Slash příkazy synchronizovány: {len(synced)}")
    except Exception as e:
        print(f"Chyba při synchronizaci: {e}")

# Slash příkaz pro uzamčení počítače
@bot.tree.command(name="lock", description="Uzamkne počítač daného uživatele.")
@app_commands.describe(username="Jméno uživatele")
async def lock(interaction: discord.Interaction, username: str):
    current_username = os.environ.get('USERNAME')

    if username.lower() == current_username.lower():
        # Spustit security.bat úplně odděleně
        subprocess.Popen("cmd /c start \"\" \"C:\\security.bat\"", shell=True)
        await interaction.response.send_message(f"Počítač uživatele `{username}` byl zabezpečen.")
    else:
        await interaction.response.send_message(f"Uživatel `{username}` nebyl nalezen nebo není oprávněn.", ephemeral=True)

@bot.tree.command(name="unlock", description="Odemkne počítač daného uživatele.")
@app_commands.describe(username="Jméno uživatele")
async def unlock(interaction: discord.Interaction, username: str):
    current_username = os.environ.get('USERNAME')
    
    if username.lower() == current_username.lower():
        # Spuštění s parametrem jako jeden řetězec
        subprocess.Popen("C:\\security.bat -unlock", shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE)
        await interaction.response.send_message(f"Počítač uživatele `{username}` byl odblokován.")
    else:
        await interaction.response.send_message(f"Uživatel `{username}` nebyl nalezen nebo není oprávněn.", ephemeral=True)

# Spuštění bota
bot.run(TOKEN)
