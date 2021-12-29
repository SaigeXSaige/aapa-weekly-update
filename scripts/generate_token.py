from twython import Twython
import sys
import requests

APP_KEY = sys.argv[1]
APP_SECRET = sys.argv[2]
AUTH_TOKEN = sys.argv[3]
AUTH_TOKEN_SECRET = sys.argv[4]
AUTH_CODE = sys.argv[5]
twitter = Twython(APP_KEY, APP_SECRET)
twitter = Twython(APP_KEY, APP_SECRET, AUTH_TOKEN, AUTH_TOKEN_SECRET)
final_step = twitter.get_authorized_tokens(AUTH_TOKEN)
OAUTH_TOKEN = final_step['oauth_token']
OAUTH_TOKEN_SECRET = final_step['oauth_token_secret']
print('Token:' + OAUTH_TOKEN)
print('Secret:' + OAUTH_TOKEN_SECRET)