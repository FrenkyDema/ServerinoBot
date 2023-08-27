<h1 align="center">Welcome to ServerinoBot 👋</h1>
<p>
  <a href="https://github.com/FrenkyDema/ServerinoBot/blob/main/LICENSE" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
</p>

> Discord Bot for displaying Minecraft server information and managing it

## Introduction

ServerinoBot is a powerful Discord Bot designed to streamline monitoring and communication with your Minecraft server. By creating an Ngrok tunnel and connecting to the Minecraft world, the bot ensures server functionality and sends informative embeds to your Discord channel. Read on to understand how it works.

## How It Works

ServerinoBot operates through the following steps:

1. **Ngrok Tunnel Creation**: The bot initiates the process by creating an Ngrok tunnel. Ngrok exposes a local server to the public network, making it accessible externally. This is a crucial step for verifying the status of the Minecraft server.

2. **Minecraft Server Verification**: The bot connects to your Minecraft server through the previously created Ngrok tunnel. This step is essential to confirm the server's status and functionality.

3. **Embed Sent to Discord Channel**: Once the active status of the Minecraft server is confirmed, the bot sends an embed to the predefined Discord channel. The embed contains essential server information, such as the IP and port for players to connect.

4. **Updating Online Players**: The bot constantly monitors the number of players connected to the Minecraft server. Periodically, it updates the embed message in the Discord channel with the current number of online players.

## Initial Setup

Before using our Discord Bot, you need to perform an initial setup:

1. **Bot Token**: Ensure you have your Discord bot token, which you can obtain through the Discord Developer Portal. Insert the token into the appropriate variable in the bot's code.

2. **Discord Channel ID**: Obtain the ID of the Discord channel where you want the bot to send updates. Insert this ID into the appropriate variable in the bot's code.

3. **Minecraft Server and Ngrok**: Properly configure your Minecraft server and Ngrok to ensure the bot can connect and verify the server's status.

4. **Ngrok and Minecraft Configuration Variables**: Modify the variables as follows:
   - `NGROK_TOKEN`: Token for authenticating with Ngrok.
   - `NGROK_REGION`: Region for the Ngrok tunnel.
   - `MC_SERVER_IP`: IP address of the Minecraft server.
   - `MC_SERVER_PORT`: Port of the Minecraft server.

## Author

👤 **FrenkyDema**

* Website: https://francescodema.dev/
* Github: [@FrenkyDema](https://github.com/FrenkyDema)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/FrenkyDema/ServerinoBot/issues/new/choose). You can also take a look at the [contributing guide](https://github.com/FrenkyDema/ServerinoBot/blob/main/.github/CODE_OF_CONDUCT.md).

## Show your support

Give a ⭐️ if this project helped you!

## 📝 License

Copyright © 2023 [FrenkyDema](https://github.com/FrenkyDema).<br />
This project is [MIT](https://github.com/FrenkyDema/ServerinoBot/blob/main/LICENSE) licensed.

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
