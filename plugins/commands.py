from pyrogram import Client, filters
from helpers.gpt import gptQuery
from config import Config

@Client.on_message(filters.text & filters.private & filters.chat(Config.ALLOWED_USERS))
async def chat(client,message):
    if message.from_user.id == Config.ME_ID:
        return
   
    msg_build = []
    async for message in client.get_chat_history(chat_id = message.chat.id,limit=5):
        if message.from_user.id == Config.ME_ID:
            if not message.text:
                continue
            msg_build.append({'role':'assistant','content':message.text})
        else:
            if not message.text:
                continue
            msg_build.append({'role':'user','content':message.text})


    gptres = await gptQuery(msg_build)
    try:
        msg = gptres['choices'][0]['message']['content']
    except:
        msg = "I'm sorry I'm busy can I'll talk to you later"
    await client.send_message(
        chat_id=message.chat.id,
        text=gptres['choices'][0]['message']['content'])

