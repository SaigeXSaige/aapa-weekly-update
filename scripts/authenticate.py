#!/usr/bin/python

from twython import Twython
import os
import requests

APP_KEY = os.environ['API_KEY']
APP_SECRET = os.environ['API_KEY_SECRET']
print("Key: ", APP_KEY, "\nSecret: ", APP_SECRET)
twitter = Twython(APP_KEY, APP_SECRET)
auth = twitter.get_authentication_tokens()
OAUTH_TOKEN = auth['oauth_token']
OAUTH_TOKEN_SECRET = auth['oauth_token_secret']
oauth_verifier_url = auth['auth_url']
oauth_verifier = requests.get(oauth_verifier_url)
print("Verifier URL is:" + oauth_verifier_url)
print("OAUTH_TOKEN is:" + OAUTH_TOKEN)
print("OAUTH TOKEN SECRET is:" + OAUTH_TOKEN_SECRET)