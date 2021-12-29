import os
# import asyncio
import requests

from twython import Twython

from create_post import create_rankings_status, create_custom_status

ROOT_PATH = os.environ['HOME']
APP_KEY = os.environ['API_KEY']
APP_SECRET = os.environ['API_KEY_SECRET']
OAUTH_TOKEN = os.environ['AAPA_ACCCESS_TOKEN']
OAUTH_TOKEN_SECRET = os.environ['AAPA_ACCCESS_TOKEN_SECRET']

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET) 

def upload_media(img_path):
    media = open(img_path, 'rb')
    try:
        result = twitter.upload_media(media=media)
    except Exception as exc:
        print(f'Error: {exc}')
    return result

def create_path(img_path):
    return ROOT_PATH + img_path

def send_init_post(img_path):
    status = create_rankings_status()
    response = upload_media(img_path)
    try:
        result = twitter.update_status(status=status, media_ids=[response['media_id']])
        print("\nSucceeded with response:\n", result)
    except Exception as exc:
        print(f'Error: {exc}')
    return result
    
def send_reply_post(status_id, img_paths): 
    status = create_rankings_status() if len(img_paths) == 1 else create_custom_status()
    if(len(img_paths) == 1):
        response = upload_media(img_paths[0])
        result = twitter.update_status(
            status=status, media_ids=[response['media_id']], 
            in_reply_to_status_id=status_id, auto_populate_reply_metadata=True
        )
        print("\nSucceeded with response:\n", result)
        return result
    else:
        media_list = [upload_media(img_path) for img_path in img_paths]
        media_ids = [response['media_id'] for response in media_list]
        
        result = twitter.update_status(
            status=status, media_ids=media_ids, 
            in_reply_to_status_id=status_id, auto_populate_reply_metadata=True
        )
        print("\nSucceeded with response:\n", result)
        return result
    
def send_thread(img_paths):
    first_tweet = send_init_post(img_paths[0])
    img_paths.remove(img_paths[0])
    print(f"First tweet sent. Remaining images are: {img_paths}")
    second_tweet = send_reply_post(first_tweet["id_str"], [img_paths[0]])
    img_paths.remove(img_paths[0])
    print(f"Second tweet sent. Remaining images are: {img_paths}")
    third_tweet = send_reply_post(second_tweet["id_str"], img_paths)
    print(f"Last tweet sent. Remaining images are: {img_paths}")
    
    urls = third_tweet["entities"]["urls"]
    print(f"Finished creating thread! Please view at {urls}")
    return third_tweet

# async def main(args):
#     task1 = asyncio.create_task(
#             send_init_post()
#         )

#     task2 = asyncio.create_task(
#             send_reply_post()
#         )
    
#     task3 = asyncio.create_task(
#             send_reply_post()
#         )

#     print("Started recursively posting")
    
#     await task1
#     await task2
#     await task3

#     print("Finished!")
    
# def send_posts_concurrently():
#     asyncio.run(main())