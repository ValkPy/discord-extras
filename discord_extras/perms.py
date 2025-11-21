import discord

async def check_permissions(interaction: discord.Interaction, action: str):
    """
    Checks whether the bot has the necessary permission to perform a given action.
    Supported actions: ban, kick, manage_messages, manage_channels, mute
    """

    # Slash commands require a guild context to check permissions
    if not interaction.guild:
        await interaction.response.send_message(
            "❌ This command must be used inside a server.",
            ephemeral=True
        )
        return False

    bot_member = interaction.guild.me  # The bot's Member object
    perms = bot_member.guild_permissions

    action = action.lower()

    # Map of supported actions to Discord.py permission attributes
    required_permissions = {
        "ban": ("ban_members", "ban members"),
        "kick": ("kick_members", "kick members"),
        "manage_messages": ("manage_messages", "manage messages"),
        "manage_channels": ("manage_channels", "manage channels"),
        "mute": ("moderate_members", "timeout members"),
    }

    # Unknown action → dev error
    if action not in required_permissions:
        raise ValueError(f"Unknown action: {action}")

    perm_attr, readable_name = required_permissions[action]

    # Check if the bot actually has the required permission
    if not getattr(perms, perm_attr):
        # Send a private error message (only visible to the command user)
        await interaction.response.send_message(
            f"❌ I don't have permission to **{readable_name}**.",
            ephemeral=True
        )
        return False

    return True
