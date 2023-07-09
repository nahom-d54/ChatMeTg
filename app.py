from pyrogram import Client
from config import Config


api_id = Config.api_id
api_hash = Config.api_hash

app = Client(
    "gpt_tg_chat",
    api_id=api_id, 
    api_hash=api_hash,
    session_string=Config.session_string,
    plugins=dict(root='plugins'))

if __name__ == '__main__':
    print('app started')
    app.run()