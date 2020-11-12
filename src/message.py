import requests
import config

class Message:
  def __init__(self, data):
    self.update_id = data['update_id']
    self.content = data['message']['text']
    self.chat_id = data['message']['from']['id']
    self.author = data['message']['from']['first_name'] + data['message']['from']['last_name']
    
  def send_reply(self, reply_msg):
    reply_url = f'{config.url_base}/sendMessage?chat_id={self.chat_id}&text={reply_msg}'
    requests.get(reply_url)