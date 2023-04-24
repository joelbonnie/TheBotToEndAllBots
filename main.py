from dotenv import dotenv_values

config = dotenv_values("variables.env")
print(config['TOKEN']+"")
