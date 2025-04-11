# Discord Raid Bot

This Python script is a simple Discord bot that performs a series of actions on a specified Discord server. It's designed to automate tasks such as deleting existing channels, creating new channels, sending messages in those channels, and renaming the server. **Use this script responsibly and ethically. Unauthorized use against servers you do not own or have permission to modify is strictly prohibited and can have serious consequences.**

## Features

* **Server Modification:**
    * Renames the target server.
    * Deletes all existing text channels.
    * Creates a specified number of new text channels.
    * Sends a specified number of messages in each created channel.
    * Renames the created channels with strikethrough formatting.
    * Resets the channel names by removing the strikethrough formatting.
* **User Input:** Takes user inputs for the bot token, server ID, new server name, new channel name, number of channels, and messages per channel.

## Prerequisites

* Python 3.6+
* `discord.py` (install with `pip install discord.py`)
* A Discord bot token (obtained from the Discord Developer Portal).
* The ID of the Discord server to modify.

## Usage

1.  **Clone the repository (if applicable):**
    ```bash
    git clone https://github.com/LK-GONNA11/Discord-Raid-Bot-
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd Discord-Raid-Bot-
    ```
    (e.g., `cd discord-raid-bot`)
3.  **Run the Python script:**
    ```bash
    python main.py
    ```
    (Or `python3 main.py` if necessary)
4.  **Enter the information:** Follow the script's prompts.
5.  **The bot performs the actions:** Operations are automated.
6.  **Channel reset option:** Choose to reset the channel names at the end.

## Important Notes

* **Token Security:** Keep your token safe.
* **Permissions:** Ensure the bot has the necessary permissions.
* **Rate Limits:** Discord has rate limits.
* **Ethical Use:** Use this script responsibly.
* **Dependencies:** If you encounter dependency errors, make sure you have installed the discord.py module.

## Disclaimer

This script is provided for educational purposes. The author is not responsible for any misuse.
