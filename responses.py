import random
import discord


def get_response(message):
    given_message = message.lower()
    if given_message == 'hello':
        return 'hello friend'
    if given_message == 'roll':
        return str(random.randint(1, 6))
    if given_message == '!help':
        return '`This is a help message`'
    if given_message == 'emote verne':
        return "!images" + given_message[6:] + ".png"
    if given_message == 'emote pepe':
        return '**no**'
    return "Error 404: Command not fund"


