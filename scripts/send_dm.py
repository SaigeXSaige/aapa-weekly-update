import os
# import asyncio
import requests

from twython import Twython

ROOT_PATH = os.environ['HOME']
APP_KEY = os.environ['API_KEY']
APP_SECRET = os.environ['API_KEY_SECRET']
OAUTH_TOKEN = os.environ['AAPA_ACCCESS_TOKEN']
OAUTH_TOKEN_SECRET = os.environ['AAPA_ACCCESS_TOKEN_SECRET']

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

def get_user_ids(screen_names):
    user_list = twitter.lookup_user(screen_name=screen_names)
    user_ids = [user.get("id_str") for user in user_list]
    return user_ids

def dm_users_to_battle(add_optional_text=False):
    users = input("Input users to battle: (i.e. tvnkth, chaucenosauce )\n")
    
    for recipient_id in get_user_ids(users):
        optional_text = " (Don't forget to add the AAPA account to the chat..)" if add_optional_text else ""
        text = "Reminder to DM your opponent for this week's battle!" + optional_text
        message_create = {"target": {"recipient_id": recipient_id}, "message_data": {"text": text}}
        result = twitter.send_direct_message(event={"type":'message_create', "message_create": message_create})
        print(result)
