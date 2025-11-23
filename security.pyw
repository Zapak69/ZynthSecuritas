import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime
import os
import subprocess
import pyautogui
import winreg



temp_path = os.path.join(os.getenv("TEMP"), "restart7488593.dll")
if os.path.isfile(temp_path):
    subprocess.Popen([r"C:\security.bat", "-restart"], shell=True)

def has_internet():
    try:
        # -n 1 (Windows) = jeden ping, -w 1000 = timeout 1s
        result = subprocess.run(
            ["ping", "8.8.8.8", "-n", "1", "-w", "1000"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return result.returncode == 0
    except:
        return False
if not has_internet():
    subprocess.Popen([r"C:\security.bat", "-nonetwork"], shell=True)


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

try:
    key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r"Software\Zynth Security",
        0,
        winreg.KEY_READ
    )
    TOKEN, _ = winreg.QueryValueEx(key, "BOTTOKEN")
    winreg.CloseKey(key)

except FileNotFoundError:
    TOKEN = None

try:
    key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r"Software\Zynth Security",
        0,
        winreg.KEY_READ
    )
    userid, _ = winreg.QueryValueEx(key, "USERID")
    winreg.CloseKey(key)

except FileNotFoundError:
    userid = None

try:
    key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r"Software\Zynth Security",
        0,
        winreg.KEY_READ
    )
    channelid, _ = winreg.QueryValueEx(key, "CHANNELID")
    winreg.CloseKey(key)

except FileNotFoundError:
    channelid = None


@bot.event
async def on_ready():
    channel = bot.get_channel(int(channelid))
    username = os.environ.get('USERNAME')

    embed = discord.Embed(
        title="Počítač byl zapnut",
        description=f"**Přihlášený uživatel:** `{username}`\n**Čas:** `{datetime.now().strftime('%H:%M:%S')}`\n**Datum:** `{datetime.now().strftime('%d.%m.%Y')}`",
        color=0x00ff00
    )

    await channel.send(f"<@{userid}> počítač byl zapnut.", embed=embed)

    # >>> TADY nastavení statusu bota:
    await bot.change_presence(
        activity=discord.Game(name="🖥️ Počítač je zapnutý!")
    )

    try:
        synced = await bot.tree.sync()
        print(f"Slash příkazy synchronizovány: {len(synced)}")
    except Exception as e:
        print(f"Chyba při synchronizaci: {e}")

@bot.tree.command(name="lock", description="Uzamkne počítač daného uživatele.")
@app_commands.describe(username="Jméno uživatele")
async def lock(interaction: discord.Interaction, username: str):
    current_username = os.environ.get('USERNAME')

    if username.lower() == current_username.lower():
        await interaction.response.defer()

        try:
            temp_path = os.path.join(os.environ.get("TEMP"), "securityscr.png")
            pyautogui.screenshot(temp_path)

            file = discord.File(temp_path, filename="screenshot.png")

            embed = discord.Embed(
                title="🔒 Počítač byl zabezpečen",
                description=f"Uživatel `{username}` byl právě uzamčen a obrazovka byla zachycena.",
                color=0xff0000
            )
            embed.set_image(url="attachment://screenshot.png")

            await interaction.followup.send(embed=embed, file=file)
            os.remove(temp_path)
        except Exception as e:
            await interaction.followup.send(f"⚠️ Chyba při tvorbě nebo odeslání screenshotu: {e}")

        try:
            subprocess.Popen(["cmd", "/c", "start", "", "C:\\security.bat"], shell=True)
        except Exception as e:
            await interaction.followup.send(f"❌ Nepodařilo se spustit security.bat: {e}")
    else:
        await interaction.response.send_message(f"Uživatel `{username}` nebyl nalezen nebo není oprávněn.", ephemeral=True)

@bot.tree.command(name="unlock", description="Odemkne počítač daného uživatele.")
@app_commands.describe(username="Jméno uživatele")
async def unlock(interaction: discord.Interaction, username: str):
    current_username = os.environ.get('USERNAME')

    if username.lower() == current_username.lower():
        await interaction.response.defer()

        try:
            temp_path = os.path.join(os.environ.get("TEMP"), "unlockscr.png")
            pyautogui.screenshot(temp_path)

            file = discord.File(temp_path, filename="unlock.png")

            embed = discord.Embed(
                title="🔓 Počítač byl odblokován",
                description=f"Počítač uživatele `{username}` byl úspěšně odemčen.\nObrazovka při odemčení byla zachycena níže.",
                color=0x00ccff
            )
            embed.set_image(url="attachment://unlock.png")

            await interaction.followup.send(embed=embed, file=file)
            os.remove(temp_path)
        except Exception as e:
            await interaction.followup.send(f"⚠️ Chyba při tvorbě nebo odeslání screenshotu: {e}")

        try:
            subprocess.Popen(["cmd", "/c", "start", "", "C:\\security.bat", "-unlock"], shell=True)
        except Exception as e:
            await interaction.followup.send(f"❌ Nepodařilo se spustit security.bat s parametrem -unlock: {e}")
    else:
        await interaction.response.send_message(f"Uživatel `{username}` nebyl nalezen nebo není oprávněn.", ephemeral=True)

@bot.tree.command(name="screenshot", description="Screenshot obrazovky uživatele.")
@app_commands.describe(username="Jméno uživatele")
async def screenshot(interaction: discord.Interaction, username: str):
    current_username = os.environ.get('USERNAME')

    if username.lower() == current_username.lower():
        await interaction.response.defer()

        try:
            temp_path = os.path.join(os.environ.get("TEMP"), "checkscr.png")
            pyautogui.screenshot(temp_path)

            file = discord.File(temp_path, filename="check.png")

            embed = discord.Embed(
                title="📸 Screenshot byl pořízen",
                color=0x00ccff
            )
            embed.set_image(url="attachment://check.png")

            await interaction.followup.send(embed=embed, file=file)
            os.remove(temp_path)
        except Exception as e:
            await interaction.followup.send(f"⚠️ Chyba při tvorbě nebo odeslání screenshotu: {e}")
    else:
        await interaction.response.send_message(f"Uživatel `{username}` nebyl nalezen nebo není oprávněn.", ephemeral=True)

bot.run(TOKEN)