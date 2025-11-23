# ZynthSecuritas

🛡️ **ZynthSecuritas** is a lightweight Windows security tool built with batch scripts and Python for simple setup and basic remote control features.

## 🔒 How it works

Once installed, ZynthSecuritas runs at system startup and sends a notification to a specified Discord channel that the PC has been turned on.

Command list:
`/lock (username)` - lockdown computer
`/unlock (username)` - unlock computer from lockdown
`/screenshot (username)` - take screenshot
`/live (username)` - start live stream (BETA, may not work)
`/shutdown (username)` - shutdown computer

## 🛠️ Installation

1. Clone the repository:

```bash
git clone https://github.com/Zapak69/ZynthSecuritas.git
```

2. Open `setup.bat` as administrator
   
3. Once setup install requirements, please finish setup in following 2 windows.
Set your password and BOT SETUP. And you´re done.

## ℹ️ Info
- All values **BOT TOKEN**, **CHANNEL ID**, **USER ID**, **SECURITY PASSWORD (TOKEN)** are stored in registry: `HKCU\Software\Zynth Security`
- This security program uses own special encryption type that will encrypt your password into TOKEN to not be detectable.
- If you are not connected to network, lockdown mode will automatically turn on beacuse it cant connect to discord.
- All batch scripts are encrypted to prevent reverse engineering.


## ⚠️ Warning
This tool is intended for advanced users – make sure you understand what each script does before running it.

Use at your own risk and always back up your data.
