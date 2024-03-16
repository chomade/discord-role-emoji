# Discord Role Emoji

This is a simple bot that allows you to assign roles to users by reacting to a message with an emoji.

## Features

- Assign roles to users by reacting to a message with an emoji
- Remove roles from users by removing the reaction
- Supports multiple emojis

## Setup

1. Clone the repository
2. Install the required packages with `pip install -r requirements.txt`
3. Create a `.env` file in the root directory and add the following:
   ```
   TOKEN='your_token'
   ```
4. Change the `defaultEmoji.json` file to the emoji you want to use
    ```json
    [
      {
        "emoji": "YOUR_EMOJI",
        "role": "YOUR_ROLE"
      },
      {
        "emoji": "YOUR_EMOJI",
        "role": "YOUR_ROLE"
      }
    ]
    ```
5. Change the `customEmoji.json` file to the emoji you want to use
    ```json
    [
      {
        "emoji_name": "YOUR_EMOJI",
        "role": "YOUR_ROLE"
      },
      {
        "emoji_name": "YOUR_EMOJI",
        "role": "YOUR_ROLE"
      }
    ]
    ```
6. Run the bot with `python bot.py`

## commands
- `!설정` : Make a message to add a role

## License
