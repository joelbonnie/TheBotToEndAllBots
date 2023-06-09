from dotenv import dotenv_values
import discord
import responses

# Environment Variable Test
# config = dotenv_values("variables.env")
config = dotenv_values("variablesLOCAL.env")

print(config['TOKEN'] + "")


async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        if is_private:
            if response[:7] == '!images':
                await message.author.send(file=discord.File(response[7:]))
            else:
                await message.author.send(response)
        else:
            if response[:7] == '!images':
                await message.channel.send(file=discord.File(response[7:]))
            else:
                await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        if user_message[:2] == 'yo':
            user_message = user_message[3:]
            if user_message[0] == '?':
                user_message = user_message[1::]
                await send_message(message, user_message, True)

            else:
                await send_message(message, user_message, False)



    client.run(config['TOKEN'])
