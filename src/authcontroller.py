import readdata
import requests
from requests_oauthlib import OAuth1

def createNewAuth(username):
	api_key, api_secret, access_token, access_token_secret = readdata.getUserinfo(username)

	return OAuth1(api_key, api_secret, access_token, access_token_secret)
