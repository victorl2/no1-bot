import requests
import json
import config
from message import Message

class TelegramBot:
  def __init__(self):
    self.update_id = None
    self.request_timeout = 100

  def start(self):
    while True:
      update_data = self.get_messages(self.update_id)
      raw_msg_data = update_data['result'] 

      if raw_msg_data:
        messages = self._parse_messages(raw_msg_data)
        
        for msg in messages:
          self.update_id = msg.update_id
          self._process_msg(msg)
          reply_msg = self.create_reply_message(msg)
          msg.send_reply(reply_msg)

  def get_messages(self, update_id):
    request_url = f'{config.url_base}/getUpdates?timeout={self.request_timeout}'
    
    if update_id:
      id_latest_message = update_id + 1
      request_url = f'{request_url}&offset={id_latest_message}'
    response = requests.get(request_url)
    return json.loads(response.content)


  def create_reply_message(self, msg):
    if msg.content == '/start':
      return 'Welcome NO1 crypto bot'

  def _process_msg(self, msg):
    pass
  
  def _parse_messages(self, messages):
    return [Message(data) for data in messages]
  

bot = TelegramBot()
bot.start()