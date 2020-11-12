import os 
token_key_name = 'telegrambot_token'

if token_key_name not in os.environ
  raise Exception('The environment variable "telegrambot_token" was not found on the system')

token= os.environ.get(token_key_name)
url_base = f'https://api.telegram.org/bot{token}'/