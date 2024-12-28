import discord
import openai

# Définir directement les clés API ici
openai.api_key = "sk-sqVXcIuoD-iMTr4vkY3VvSTVyq-CHay7ozaQCtl4sET3BlbkFJe0zujexM1IEMqGIMCN1a9W9CDoNL04y5hap8FBZ64A"
discord_token = "fc5fff58c5617de6613736fa288ebc0b1abe4c84ab2993f20a235cef4ef521d1"

client = discord.Client()

@client.event
async def on_ready():
    print(f'Nous sommes connectés en tant que {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!bonjour'):
        prompt = message.content[len('!bonjour '):]
        response = openai.Completion.create(
            engine="text-davinci-003",  # Ou une autre version du modèle
            prompt=prompt,
            max_tokens=150
        )
        await message.channel.send(response.choices[0].text.strip())

# Lancer le bot Discord avec le token
client.run(discord_token)
