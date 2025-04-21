# ZynthSecuritas

🛡️ **ZynthSecuritas** is a lightweight Windows security tool built with batch scripts and Python for simple setup and basic remote control features.

## 🔒 How it works

Once installed, ZynthSecuritas runs at system startup and sends a notification to a specified Discord channel that the PC has been turned on.

You can remotely lock the system using the Discord bot command:
`/lock (username)`

This command will:
- Immediately terminate foreground apps (like Discord, browsers, or games)
- Block access to Task Manager
- Require a password to unlock the system (encrypted with a custom method)

## 🛠️ Installation

1. Clone the repository:

```bash
git clone https://github.com/Zapak69/ZynthSecuritas.git
```

2. Install [python](https://www.python.org/downloads/) and requirements from [req.txt](https://raw.githubusercontent.com/Zapak69/ZynthSecuritas/refs/heads/main/req.txt)

3. Follow the steps in [INSTALL GUIDE.txt](https://raw.githubusercontent.com/Zapak69/ZynthSecuritas/refs/heads/main/INSTALL%20GUIDE.txt).

## ⚠️ Warning
This tool is intended for advanced users – make sure you understand what each script does before running it.

Use at your own risk and always back up your data.
