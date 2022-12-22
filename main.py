import discord
import json

# Discover what have the config.json file
config_file = open('config.json')
config = json.load(config_file)

class MyClient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild=discord.Object(id=config['test_guild']))
            self.synced = True
        print(f'Logged on as {self.user}!')


client = MyClient()
tree = discord.app_commands.CommandTree(client)
testing_guild = discord.Object(id=config['test_guild'])


@tree.command(name='ping', description="Ping command", guild=testing_guild)
async def self(interaction: discord.Interaction):
    await interaction.response.send_message(f"{int(round(client.latency, 3) * 1000)} ms")

@tree.command(name='mp', description='send a mp to you', guild=testing_guild)
async def self(interaction: discord.Interaction, message: str):
    await interaction.user.send("HELO")

client.run(config['token'])