import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6686737285:AAFS95C2rwkYtwC-dipW2ePCSTJTTiXxG5Y")

API_ID = int(os.environ.get("API_ID", "21037450"))

API_HASH = os.environ.get("API_HASH", "05ac9eb7c523b83c51d89d1f2f91d58b")

STRING = os.environ.get("STRING", "1098077551")



bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
