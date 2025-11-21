# discord-extras

A small utility library that adds extra helper functions for Discord bots built with **discord.py**.

## Features

### ✔️ Automatic bot permission checking  
Before performing actions like banning, kicking, or deleting messages, `discord-extras` ensures that the bot has the required permissions.

---

## Installation

Install directly from GitHub:

pip install git+https://github.com/ValkPy/discord-extras.git


---

## Usage Example

```python
from discord_extras import check_permissions
from discord import app_commands

@bot.tree.command(name="ban")
async def ban_user(interaction: discord.Interaction, member: discord.Member):
    if not await check_permissions(interaction, "ban"):
        return

    await member.ban(reason=f"Banned by {interaction.user}")
    await interaction.response.send_message(f"{member} has been banned.")
```