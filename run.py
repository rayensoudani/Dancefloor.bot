import sys
import os
import time
import traceback
from importlib import import_module
from highrise.__main__ import *

# BOT SETTINGS
bot_file_name = "main"
bot_class_name = "Bot"
room_id = "66c19c9f4cb40d6c69c799ac"
bot_token = "e9106054284a8874f91bc7877826a5dc685cca3cd2f341326ce3b9e1f2972ae1"

my_bot = BotDefinition(getattr(import_module(bot_file_name), bot_class_name)(), room_id, bot_token)

while True:
    try:
        definitions = [my_bot]
        arun(main(definitions))
    except Exception as e:
        print(f"An exception occurred: {e}")
        traceback.print_exc()
    time.sleep(5)

