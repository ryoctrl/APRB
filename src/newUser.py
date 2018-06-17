import requests
#import urllib.parse
import datetime

request_token_url = "https://api.twitter.com/oauth/request_token"
callback_url = ""

def createNewUser(api_key, api_secret):
	parameters = {
		"oauth_callback" : callback_url,
		"oauth_consumer_key" : api_key,
		"oauth_signature_method" : "HMAC-SHA1",
		"oauth_timestamp" : datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
		"oauth_nonce" : datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
		"oauth_version" : "1.0"
	}
def getUserInformation(auth):
	import requets
	
def registNewUser():
	print("input your API_KEY")
	api_key = raw_input("api_key >> ")

	print("input your API_SECRET")
	api_secret = raw_input("api_secret >> ")

	print("input your ACCESS_TOKEN")
	access_token = raw_input("access_token >> ")

	print("input your ACCESS_TOKEN_SECRET")
	access_token_secret = raw_input("access_token_secret >> ")
	
	
