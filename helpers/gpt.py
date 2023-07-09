import aiohttp
import time
from config import Config

async def gptQuery(message):
    #print(Config.GPT_BODY_list(message))
    async with aiohttp.ClientSession() as session:
        async with session.post(Config.GPT_URL,json=Config.GPT_BODY_list(message)) as response:
            try:
                json_res = await response.json()
            except Exception as e:
                print(e,response.text)
                return
   
            return json_res